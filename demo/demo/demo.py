"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui


class State(rx.State):
    seed: int = 0


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.el.div(
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
            items=[
                "Item 1",
                "Item 2",
                "Item 3",
                "Item 4",
                "Item 5",
                "Item 6",
                "Item 7",
                "Item 8",
                "Item 9",
                "Item 10",
            ],
            name="select",
            default_value="Select an item",
            on_value_change=lambda value: rx.toast.success(f"Value: {value}"),
            on_open_change=lambda value: rx.toast.success(f"Open: {value}"),
        ),
        ui.preview_card(
            trigger=ui.button("Hover for preview", variant="outline"),
            content=rx.el.div(
                rx.el.h3("Preview Card", class_name="text-lg font-semibold mb-2"),
                rx.el.p("This is a preview card component that shows content on hover.", class_name="text-sm text-secondary-11"),
                class_name="p-4"
            ),
            delay=300,
            close_delay=100,
        ),
        ui.theme_switcher(class_name="absolute top-4 right-4"),
        class_name=ui.cn(
            "flex flex-col gap-6 items-center justify-center h-screen", "bg-secondary-1"
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
