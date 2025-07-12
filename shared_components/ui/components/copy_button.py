import reflex as rx
from reflex.experimental import ClientStateVar

from shared_components.ui.components import button
from shared_components.ui.components.icons import hi


@rx.memo
def integration_copy_button(text: str | rx.Var[str], class_name: str = ""):
    copied = ClientStateVar.create("is_copied", default=False, global_ref=False)
    return button.button(
        text,
        rx.cond(
            copied.value,
            hi(
                "tick-02",
            ),
            hi("copy-01"),
        ),
        variant="transparent",
        size="icon-md",
        on_click=[
            rx.call_function(copied.set_value(True)),
            rx.set_clipboard(text),
        ],
        on_mouse_down=rx.call_function(copied.set_value(False)).debounce(1500),
        class_name=class_name,
    )
