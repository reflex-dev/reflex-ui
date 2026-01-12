"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog
from reflex_ui.blocks.telemetry.default import get_default_telemetry_script


class State(rx.State):
    seed: int = 0

    @rx.event
    def set_seed(self, seed: int):
        self.seed = seed


def index() -> rx.Component:
    return rx.el.div(
        demo_form_dialog(ui.button("Test")),
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
            cros_sorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400..700&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400..700&display=swap",
            rel="stylesheet",
        ),
        get_default_telemetry_script(),
    ],
)
app.add_page(index)
