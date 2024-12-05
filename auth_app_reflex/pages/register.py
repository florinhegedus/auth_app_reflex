import reflex as rx

from .. import navigation
from ..components import register_single_thirdparty


def register_page() -> rx.Component:
    register_box = rx.center(
        register_single_thirdparty(),
        padding="1em",
    )
    return register_box