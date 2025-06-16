"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.el.div(
        ui.button(
            ui.icon("SmileIcon"),
            "Click me",
            on_click=rx.toast.success(
                "You are cool :)",
                position="top-center",
            ),
        ),
        ui.theme_switcher(class_name="absolute top-4 right-4"),
        class_name=ui.cn(
            "flex flex-col items-center justify-center h-screen", "bg-secondary-1"
        ),
    )


app = rx.App(
    stylesheets=["css/globals.css"],
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400..700&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400..700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
