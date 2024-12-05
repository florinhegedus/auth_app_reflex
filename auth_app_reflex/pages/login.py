import reflex as rx

from .. import navigation
from ..components import login_single_thirdparty


def login_page() -> rx.Component:
    login_box = rx.center(
        login_single_thirdparty(),
        padding="1em",
    )
    return login_box
