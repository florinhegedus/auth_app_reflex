"""The authentication state."""
import re
import reflex as rx
from sqlmodel import select
from typing import Optional

from .db_model import User
from .encrypt import hash_password, verify_password
from .. import navigation


class State(rx.State):
    """The base state for the app."""

    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect(navigation.routes.HOME_ROUTE)

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect(navigation.routes.LOGIN_ROUTE)

    @rx.var
    def logged_in(self) -> bool:
        """Check if a user is logged in."""
        return self.user is not None


class AuthState(State):
    """The authentication state for register and login page."""
    username: str
    password: str

    checked_terms: bool = False
    email_string: str
    password_rules: list[str]

    def register(self):
        """Register a user."""
        with rx.session() as session:
            if self.email_string != "" or self.any_password_rules:
                return rx.window_alert("Provide a valid mail and password.")
            if not self.checked_terms:
                return rx.window_alert("To continue accept the terms and conditions.")
            self.user = User(username=self.username, password=hash_password(self.password))
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            self.reset()
            return rx.redirect(navigation.routes.LOGIN_ROUTE)

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and verify_password(self.password, user.password):
                self.user = user
                return rx.redirect(navigation.routes.PROFILE_ROUTE)
            else:
                return rx.window_alert("Invalid username or password.")
            
    def reset_and_go_to_login_page(self):
        """ Redirect to login page and reset state. """
        self.reset()
        return rx.redirect(navigation.routes.LOGIN_ROUTE)

    def reset_and_go_to_register_page(self):
        """ Redirect to register page and reset state. """
        self.reset()
        return rx.redirect(navigation.routes.REGISTER_ROUTE)
            
    def set_and_check_username(self, username):
        self.username = username
        if not self.is_mail_valid():
            self.email_string = "Please provide a valid email address."
        elif not self.is_mail_available():
            self.email_string = "Email address already in use."
        else:
            self.email_string = ""
        
    def set_and_check_password(self, password):
        self.password = password
        self.password_rules = ["Password should: "]

        min_length = 8
        if len(self.password) < min_length:
            self.password_rules.append("  be at least 8 characters long.")

        if not any(char.islower() for char in self.password):
            self.password_rules.append("  contain at least one lowercase letter.")

        if not any(char.isupper() for char in self.password):
            self.password_rules.append("  contain at least one uppercase letter.")

        if not any(char.isdigit() for char in self.password):
            self.password_rules.append("  contain at least one digit.")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            self.password_rules.append("  contain at least one special character.")

    def is_mail_valid(self) -> bool:
        """ Check mail syntax to be valid """
        if not self.username:
            return True
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, self.username) is not None
    
    def is_mail_available(self) -> bool:
        with rx.session() as session:
            if session.exec(select(User).where(User.username == self.username)).first():
                return False
        return True
    
    @rx.var
    def any_password_rules(self) -> bool:
        rx.console_log(len(self.password_rules))
        if len(self.password_rules) > 1:
            return True
        return False
