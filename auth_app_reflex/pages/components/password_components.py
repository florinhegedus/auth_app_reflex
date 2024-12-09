import reflex as rx

from ...auth.state import AuthState


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