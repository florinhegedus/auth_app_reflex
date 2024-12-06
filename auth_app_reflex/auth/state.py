"""The authentication state."""
import re
import reflex as rx
from sqlmodel import select
from typing import Optional

from .db_model import User
from .encrypt import hash_password, verify_password
from ..navigation import NavState


class State(rx.State):
    """The base state for the app."""

    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return NavState.to_home()

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return NavState.to_login()

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
    password_string: str

    def register(self):
        """Register a user."""
        with rx.session() as session:
            if not self.checked_terms:
                return rx.window_alert("To continue, read and accept the terms and conditions.")
            self.user = User(username=self.username, password=hash_password(self.password))
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            self.reset()
            return NavState.to_login()

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and verify_password(self.password, user.password):
                self.user = user
                return NavState.to_profile()
            else:
                return rx.window_alert("Invalid username or password.")
            
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
        if not self.is_password_secure():
            self.password_string = "Password is not secure enough."
        else:
            self.password_string = ""

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


    def is_password_secure(self) -> bool:
        """ Check password to be secure """
        if not self.password:
            return True
        
        min_length = 8
        if len(self.password) < min_length:
            return False

        if not any(char.islower() for char in self.password):
            return False

        if not any(char.isupper() for char in self.password):
            return False

        if not any(char.isdigit() for char in self.password):
            return False

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password):
            return False
        
        return True
