import reflex as rx
from ..auth import State, State, require_login
from .. import navigation


@require_login
def profile_page() -> rx.Component:
    profile_box = rx.center(
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.heading(
                            "Profile",
                            size="6",
                            as_="h2",
                            text_align="left",
                            width="100%",
                    ),
                    rx.text(
                        State.user.username
                    ),
                    rx.text(
                        State.user.password
                    ),
                    rx.button(
                        "Reset password",
                        on_click=rx.redirect(navigation.routes.RESET_PASSWORD_ROUTE)
                    ),
                    rx.button(
                        "Log out",
                        on_click=State.logout
                    ),
                    direction="column",
                    justify="start",
                    spacing="4",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
        ),
        padding="1em",
    )
    return profile_box