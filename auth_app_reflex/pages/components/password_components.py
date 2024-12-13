import reflex as rx

from ...auth.state import State


def render_item(item: rx.Var[str]):
    """Render a single item."""
    # Note that item here is a Var, not a str!
    return rx.text(item, color="red", white_space="pre")


def display_password_rules() -> rx.Component:
    return rx.cond(State.any_password_rules,
                rx.box(
                    rx.foreach(State.password_rules, render_item),
                ),
                rx.text(""))