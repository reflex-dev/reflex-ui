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
        ui.navigation_menu.root(
            ui.navigation_menu.list(
                ui.navigation_menu.item(
                    ui.navigation_menu.trigger(
                        "Overview",
                        ui.navigation_menu.icon("▼"),
                    ),
                    ui.navigation_menu.content(
                        rx.el.ul(
                            rx.el.li(
                                ui.navigation_menu.link(
                                    rx.el.h3("Quick Start", class_name="font-medium text-sm"),
                                    rx.el.p("Install and assemble your first component.", class_name="text-xs text-secondary-11"),
                                    href="/quick-start",
                                    on_click=lambda: rx.toast.success("Quick Start clicked"),
                                    class_name="block p-3 rounded hover:bg-secondary-3",
                                )
                            ),
                            rx.el.li(
                                ui.navigation_menu.link(
                                    rx.el.h3("Accessibility", class_name="font-medium text-sm"),
                                    rx.el.p("Learn how we build accessible components.", class_name="text-xs text-secondary-11"),
                                    href="/accessibility",
                                    on_click=lambda: rx.toast.success("Accessibility clicked"),
                                    class_name="block p-3 rounded hover:bg-secondary-3",
                                )
                            ),
                            rx.el.li(
                                ui.navigation_menu.link(
                                    rx.el.h3("Releases", class_name="font-medium text-sm"),
                                    rx.el.p("See what's new in the latest versions.", class_name="text-xs text-secondary-11"),
                                    href="/releases",
                                    on_click=lambda: rx.toast.success("Releases clicked"),
                                    class_name="block p-3 rounded hover:bg-secondary-3",
                                )
                            ),
                            class_name="grid grid-cols-2 gap-2 w-96 p-2",
                        )
                    ),
                ),
                ui.navigation_menu.item(
                    ui.navigation_menu.trigger(
                        "Handbook",
                        ui.navigation_menu.icon("▼"),
                    ),
                    ui.navigation_menu.content(
                        rx.el.ul(
                            rx.el.li(
                                ui.navigation_menu.link(
                                    rx.el.h3("Styling", class_name="font-medium text-sm"),
                                    rx.el.p("Components can be styled with CSS, Tailwind, or CSS-in-JS.", class_name="text-xs text-secondary-11"),
                                    href="/styling",
                                    on_click=lambda: rx.toast.success("Styling clicked"),
                                    class_name="block p-3 rounded hover:bg-secondary-3",
                                )
                            ),
                            rx.el.li(
                                ui.navigation_menu.link(
                                    rx.el.h3("Animation", class_name="font-medium text-sm"),
                                    rx.el.p("Components can be animated with CSS or JavaScript.", class_name="text-xs text-secondary-11"),
                                    href="/animation",
                                    on_click=lambda: rx.toast.success("Animation clicked"),
                                    class_name="block p-3 rounded hover:bg-secondary-3",
                                )
                            ),
                            class_name="flex flex-col gap-2 w-80 p-2",
                        )
                    ),
                ),
                ui.navigation_menu.item(
                    ui.navigation_menu.link(
                        "GitHub",
                        href="https://github.com/reflex-dev/reflex-ui",
                        on_click=lambda: rx.toast.success("GitHub clicked"),
                    ),
                ),
            ),
            ui.navigation_menu.portal(
                ui.navigation_menu.positioner(
                    ui.navigation_menu.popup(
                        ui.navigation_menu.arrow(),
                        ui.navigation_menu.viewport(),
                    ),
                    side_offset=10,
                ),
            ),
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
