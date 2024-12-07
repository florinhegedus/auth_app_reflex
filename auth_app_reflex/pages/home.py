import reflex as rx
from ..auth.state import AuthState
from .. import navigation


def home_component() -> rx.Component:
    home_box = rx.cond(
        AuthState.logged_in,
        rx.container(
            rx.hstack(
                rx.text("Logged in user: " + AuthState.username),
                rx.button("Log out", on_click=AuthState.logout),
            ),
        ),
        rx.container(
            rx.hstack(
                rx.text("User is not logged in."),
                rx.button("Go to login page", on_click=rx.redirect(navigation.routes.LOGIN_ROUTE)),
            ),
        ),
    )
    return home_box


def home_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Home Page"),
        home_component(),
        rx.logo(),
    )
