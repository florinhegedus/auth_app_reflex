import reflex as rx

from .. import navigation
from ..auth import State


def logout_needed_page() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Log out needed"),
            rx.text(f"Currently logged in: {State.username}"),
            rx.text("You need to logout to continue"),
            rx.hstack(
                rx.button("Go to home page", on_click=rx.redirect(navigation.routes.HOME_ROUTE)),
                rx.button("Logout", on_click=State.logout)
            )
        )
    )