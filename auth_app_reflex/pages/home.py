import reflex as rx


def home_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Home Page"),
        rx.logo(),
    )
