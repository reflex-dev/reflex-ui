"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui
from .simple_icon import simple_icon_demo

class State(rx.State):
    seed: int = 0


def index() -> rx.Component:
    return rx.el.div(
        # Left: Column of UI components
        rx.el.div(
            ui.tooltip(
                ui.button(
                    ui.icon("SmileIcon"),
                    "Click me",
                    on_click=rx.toast.success(
                        "You are cool :)",
                        position="top-center",
                    ),
                ),
                content="Seriously, click me",
            ),
            ui.checkbox(
                label="Click me",
                on_checked_change=lambda value: rx.toast.success(f"Value: {value}"),
            ),
            ui.slider(
                value=State.seed,
                on_value_change=State.set_seed,
                on_value_committed=lambda value: rx.toast.success(f"Value: {value}"),
                class_name="max-w-xs",
            ),
            ui.gradient_profile(
                seed=State.seed,
                class_name="size-10",
            ),
            ui.switch(
                on_checked_change=lambda value: rx.toast.success(f"Value: {value}"),
            ),
            ui.select(
                items=[f"Item {i}" for i in range(1, 11)],
                name="select",
                default_value="Select an item",
                on_value_change=lambda value: rx.toast.success(f"Value: {value}"),
                on_open_change=lambda value: rx.toast.success(f"Open: {value}"),
            ),
            class_name="flex flex-col gap-y-6 justify-center items-center",
        ),

        # Right: Icon demo
        rx.el.div(
            simple_icon_demo(),
            class_name="flex justify-center items-center",
        ),

        # Theme switcher (floating top-right)
        ui.theme_switcher(class_name="absolute top-4 right-4"),

        # Parent container: center everything horizontally & vertically
        class_name="flex flex-row gap-16 justify-center items-center h-screen bg-secondary-1 relative",
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
