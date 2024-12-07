import reflex as rx

from .. import navigation
from ..auth.state import AuthState


def render_item(item: rx.Var[str]):
    """Render a single item."""
    # Note that item here is a Var, not a str!
    return rx.text(item, color="red", white_space="pre")


def display_password_rules() -> rx.Component:
    return rx.cond(AuthState.any_password_rules,
                rx.box(
                    rx.foreach(AuthState.password_rules, render_item),
                ),
                rx.text(""))


def register_single_thirdparty() -> rx.Component:
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
                    "Create an account",
                    size="6",
                    as_="h2",
                    text_align="left",
                    width="100%",
                ),
                rx.hstack(
                    rx.text(
                        "Already registered?",
                        size="3",
                        text_align="left",
                    ),
                    rx.link("Sign in", on_click=navigation.NavState.to_login, size="3"),
                    spacing="2",
                    opacity="0.8",
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
                    on_blur=AuthState.set_and_check_username,
                    type="email",
                    size="3",
                    width="100%",
                ),
                rx.text(
                        AuthState.email_string,
                        color="red",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Password",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Enter your password",
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
            rx.box(
                rx.checkbox(
                    "Agree to Terms and Conditions",
                    default_checked=False,
                    on_change=AuthState.set_checked_terms,
                    spacing="2",
                ),
                width="100%",
            ),
            rx.button("Register", size="3", width="100%", on_click=AuthState.register),
            rx.hstack(
                rx.divider(margin="0"),
                rx.text(
                    "Or continue with",
                    white_space="nowrap",
                    weight="medium",
                ),
                rx.divider(margin="0"),
                align="center",
                width="100%",
            ),
            rx.button(
                rx.icon(tag="mail"),
                "Sign in with Google",
                on_click=navigation.NavState.to_home(),
                variant="outline",
                size="3",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )


def register_page() -> rx.Component:
    register_box = rx.center(
        register_single_thirdparty(),
        padding="1em",
    )
    return register_box
