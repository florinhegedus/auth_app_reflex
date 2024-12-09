import reflex as rx

from ..auth import AuthState, require_login
from .components import display_password_rules


def reset_password() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.flex(
                rx.image(
                    src="/logo.png",
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Reset password",
                    size="6",
                    as_="h2",
                    text_align="left",
                    width="100%",
                ),
                direction="column",
                justify="start",
                spacing="4",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "New password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter password",
                    on_change=AuthState.set_and_check_password,
                    type="password",
                    size="3",
                    width="100%",
                ),
                display_password_rules(),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Confirm new password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter password",
                    on_change=AuthState.set_password_confirm,
                    type="password",
                    size="3",
                    width="100%",
                ),
                rx.cond(AuthState.passwords_match,
                        rx.text(""),
                        rx.text("Passwords do not match")
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.button("Reset password", 
                      on_click=AuthState.reset_password,
                      size="3", 
                      width="100%"),
        ),
        size="4",
        max_width="28em",
        width="100%",
    )


@require_login
def reset_password_page() -> rx.Component:
    reset_password_box = rx.center(
        reset_password(),
        padding="1em",
    )
    return reset_password_box
