"""Theme switcher component"""

from reflex.components.component import Component, memo
from reflex.components.core.cond import cond
from reflex.components.el import Button, Div
from reflex.style import LiteralColorMode, color_mode, set_color_mode

from reflex_ui.components.icons.hugeicon import hi
from reflex_ui.utils.twmerge import cn


def theme_switcher_item(mode: LiteralColorMode, icon: str) -> Component:
    active_cn = "text-secondary-12 shadow-small bg-secondary-1"
    unactive_cn = "hover:text-secondary-12 text-secondary-9"
    return Button.create(
        hi(icon, class_name="shrink-0", size=14),
        on_click=set_color_mode(mode),
        class_name=(
            "flex items-center cursor-pointer justify-center rounded-sm transition-color size-6",
            cond(mode == color_mode, active_cn, unactive_cn),
        ),
        aria_label=f"Switch to {mode} mode",
    )


@memo
def theme_switcher(class_name: str = "") -> Component:
    """Theme switcher component"""
    return Div.create(
        theme_switcher_item("system", "ComputerIcon"),
        theme_switcher_item("light", "Sun01Icon"),
        theme_switcher_item("dark", "Moon02Icon"),
        class_name=cn(
            "flex flex-row items-center bg-secondary-3 p-1 rounded-md w-fit",
            class_name,
        ),
    )
