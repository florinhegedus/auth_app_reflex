"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from . import pages, navigation


app = rx.App()
app.add_page(
    pages.home_page,
    route=navigation.routes.HOME_ROUTE,
)
app.add_page(
    pages.login_page,
    route=navigation.routes.LOGIN_ROUTE,
)
app.add_page(
    pages.signup_page,
    route=navigation.routes.SIGNUP_ROUTE,
)
app.add_page(
    pages.reset_password_page,
    route=navigation.routes.RESET_PASSWORD,
)
