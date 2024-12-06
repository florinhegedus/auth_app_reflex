import reflex as rx

from ..auth import AuthState


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
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="user@reflex.dev",
                    on_blur=AuthState.set_username,
                    type="email",
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Enter new password",
                        size="3",
                        weight="medium",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter password",
                    on_blur=AuthState.set_password,
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Reset password", 
                      on_click=AuthState.logout,
                      size="3", 
                      width="100%"),
        ),
        size="4",
        max_width="28em",
        width="100%",
    )


def reset_password_page() -> rx.Component:
    reset_password_box = rx.center(
        reset_password(),
        padding="1em",
    )
    return reset_password_box
