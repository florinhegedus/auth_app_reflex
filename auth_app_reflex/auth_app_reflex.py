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
    pages.register_page,
    route=navigation.routes.REGISTER_ROUTE,
)
app.add_page(
    pages.reset_password_page,
    route=navigation.routes.RESET_PASSWORD,
)
app.add_page(
    pages.profile_page,
    route=navigation.routes.PROFILE_ROUTE,
)

