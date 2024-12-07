import reflex as rx
from . import routes
from ..auth import AuthState


class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_login(self):
        return rx.redirect(routes.LOGIN_ROUTE)
    
    def to_register(self):
        AuthState.reset()
        return rx.redirect(routes.REGISTER_ROUTE)
    
    def to_profile(self):
        return rx.redirect(routes.PROFILE_ROUTE)
    
    def to_password_reset(self):
        return rx.redirect(routes.RESET_PASSWORD_ROUTE)
