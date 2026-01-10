"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form, demo_form_dialog


class State(rx.State):
    seed: int = 0

    @rx.event
    def set_seed(self, seed: int):
        self.seed = seed


def index() -> rx.Component:
    return rx.el.div(
        demo_form(),
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
        rx.el.script(
            """!function(e,t){var _=0;e.__default__=e.__default__||{},e.__default__.form_id=268792,e.__default__.team_id=654,e.__default__.listenToIds=[],function e(){var o=t.createElement("script");o.async=!0,o.src="https://import-cdn.default.com",o.onload=function(){!0,console.info("[Default.com] Powered by Default.com")},o.onerror=function(){++_<=3&&setTimeout(e,1e3*_)},t.head.appendChild(o)}()}(window,document);"""
        ),
    ],
)
app.add_page(index)
