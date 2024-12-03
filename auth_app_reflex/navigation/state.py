import reflex as rx
from . import routes


class NavState(rx.State):
    def to_home():
        return rx.redirect(routes.HOME_ROUTE)
