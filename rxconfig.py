import reflex as rx

config = rx.Config(
    app_name="reflex_ui",
    telemetry_enabled=False,
    show_built_with_reflex=False,
    plugins=[rx.plugins.TailwindV4Plugin()],
)
