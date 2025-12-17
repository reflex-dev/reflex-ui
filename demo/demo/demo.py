"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog
from reflex_ui.blocks.telemetry.unify import get_unify_trackers
from reflex_ui.blocks.calcom import calcom_popup_embed


class State(rx.State):
    seed: int = 0

    @rx.event
    def set_seed(self, seed: int):
        self.seed = seed


def index() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Book a Demo Form Test",
                class_name="text-xl sm:text-2xl font-bold text-secondary-12 px-4",
            ),
            demo_form_dialog(
                trigger=ui.button("Open Demo Form Dialog"),
            ),
            class_name="flex flex-col gap-y-4 sm:gap-y-6 justify-center items-center py-6 sm:py-12 w-full",
        ),
        ui.theme_switcher(class_name="absolute top-4 right-4 z-10"),
        class_name="flex flex-col justify-center items-center min-h-screen bg-secondary-1 relative",
    )


app = rx.App(
    stylesheets=["css/globals.css"],
    extra_app_wraps={
        (55, "Calcom Popup Embed"): lambda _: calcom_popup_embed(),
    },
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
        # Unify tracking script
        get_unify_trackers(),
    ],
)
app.add_page(index)
