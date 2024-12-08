import reflex as rx

from .. import navigation


def login_needed_page() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Log in needed"),
            rx.text("You need to login to continue"),
            rx.hstack(
                rx.button("Go to home page", on_click=rx.redirect(navigation.routes.HOME_ROUTE)),
                rx.button("Go to login page", on_click=rx.redirect(navigation.routes.LOGIN_ROUTE))
            )
        )
    )