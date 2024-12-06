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

    def register(self):
        """Register a user."""
        with rx.session() as session:
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = User(username=self.username, password=hash_password(self.password))
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
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
            
    def set_username(self, username):
        """ Set the username. """
        self.username = username

    def set_password(self, password):
        """ Set the password. """
        self.password = password

    @rx.var
    def check_mail_validity(self) -> bool:
        if not self.username:
            return True
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, self.username) is not None
