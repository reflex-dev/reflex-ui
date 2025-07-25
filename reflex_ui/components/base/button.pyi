"""Stub file for reflex_ui/components/base/button.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from collections.abc import Mapping, Sequence
from typing import Any, Literal

from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import Button as BaseButton
from reflex.event import EventType, PointerEventInfo
from reflex.vars.base import Var

from reflex_ui.components.component import CoreComponent

LiteralButtonVariant = Literal[
    "primary", "destructive", "outline", "secondary", "ghost", "link", "dark"
]
LiteralButtonSize = Literal[
    "xs", "sm", "md", "lg", "xl", "icon-xs", "icon-sm", "icon-md", "icon-lg", "icon-xl"
]
DEFAULT_CLASS_NAME = "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-colors disabled:cursor-not-allowed disabled:border disabled:border-secondary-4/80 disabled:bg-secondary-3 disabled:text-secondary-8 shrink-0 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 text-medium cursor-pointer box-border"
BUTTON_VARIANTS = {
    "variant": {
        "primary": "bg-primary-9 text-white hover:bg-primary-10",
        "destructive": "bg-destructive-9 hover:bg-destructive-10 text-white",
        "outline": "border border-secondary-a4 bg-secondary-1 hover:bg-secondary-3 text-secondary-12",
        "secondary": "bg-secondary-4 text-secondary-12 hover:bg-secondary-5",
        "ghost": "hover:bg-secondary-3 text-secondary-12",
        "link": "text-secondary-12 underline-offset-4 hover:underline",
        "dark": "bg-secondary-12 text-secondary-1 hover:bg-secondary-12/80",
    },
    "size": {
        "xs": "px-1.5 h-7 rounded-ui-xs gap-1.5",
        "sm": "px-2 h-8 rounded-ui-sm gap-2",
        "md": "px-2.5 h-9 rounded-ui-md gap-2",
        "lg": "px-3 h-10 rounded-ui-lg gap-2.5",
        "xl": "px-3.5 h-12 rounded-ui-xl gap-3",
        "icon-xs": "size-7 rounded-ui-xs",
        "icon-sm": "size-8 rounded-ui-sm",
        "icon-md": "size-9 rounded-ui-md",
        "icon-lg": "size-10 rounded-ui-lg",
        "icon-xl": "size-12 rounded-ui-xl",
    },
}

class Button(BaseButton, CoreComponent):
    @classmethod
    def create(
        cls,
        *children,
        variant: Literal[
            "dark", "destructive", "ghost", "link", "outline", "primary", "secondary"
        ]
        | Var[
            Literal[
                "dark",
                "destructive",
                "ghost",
                "link",
                "outline",
                "primary",
                "secondary",
            ]
        ]
        | None = None,
        size: Literal[
            "icon-lg",
            "icon-md",
            "icon-sm",
            "icon-xl",
            "icon-xs",
            "lg",
            "md",
            "sm",
            "xl",
            "xs",
        ]
        | Var[
            Literal[
                "icon-lg",
                "icon-md",
                "icon-sm",
                "icon-xl",
                "icon-xs",
                "lg",
                "md",
                "sm",
                "xl",
                "xs",
            ]
        ]
        | None = None,
        loading: Var[bool] | bool | None = None,
        auto_focus: Var[bool] | bool | None = None,
        disabled: Var[bool] | bool | None = None,
        form: Var[str] | str | None = None,
        form_action: Var[str] | str | None = None,
        form_enc_type: Var[str] | str | None = None,
        form_method: Var[str] | str | None = None,
        form_no_validate: Var[bool] | bool | None = None,
        form_target: Var[str] | str | None = None,
        name: Var[str] | str | None = None,
        type: Literal["button", "reset", "submit"]
        | Var[Literal["button", "reset", "submit"]]
        | None = None,
        value: Var[float | int | str] | float | int | str | None = None,
        access_key: Var[str] | str | None = None,
        auto_capitalize: Literal[
            "characters", "none", "off", "on", "sentences", "words"
        ]
        | Var[Literal["characters", "none", "off", "on", "sentences", "words"]]
        | None = None,
        content_editable: Literal["inherit", "plaintext-only", False, True]
        | Var[Literal["inherit", "plaintext-only", False, True]]
        | None = None,
        context_menu: Var[str] | str | None = None,
        dir: Var[str] | str | None = None,
        draggable: Var[bool] | bool | None = None,
        enter_key_hint: Literal[
            "done", "enter", "go", "next", "previous", "search", "send"
        ]
        | Var[Literal["done", "enter", "go", "next", "previous", "search", "send"]]
        | None = None,
        hidden: Var[bool] | bool | None = None,
        input_mode: Literal[
            "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
        ]
        | Var[
            Literal[
                "decimal", "email", "none", "numeric", "search", "tel", "text", "url"
            ]
        ]
        | None = None,
        item_prop: Var[str] | str | None = None,
        lang: Var[str] | str | None = None,
        role: Literal[
            "alert",
            "alertdialog",
            "application",
            "article",
            "banner",
            "button",
            "cell",
            "checkbox",
            "columnheader",
            "combobox",
            "complementary",
            "contentinfo",
            "definition",
            "dialog",
            "directory",
            "document",
            "feed",
            "figure",
            "form",
            "grid",
            "gridcell",
            "group",
            "heading",
            "img",
            "link",
            "list",
            "listbox",
            "listitem",
            "log",
            "main",
            "marquee",
            "math",
            "menu",
            "menubar",
            "menuitem",
            "menuitemcheckbox",
            "menuitemradio",
            "navigation",
            "none",
            "note",
            "option",
            "presentation",
            "progressbar",
            "radio",
            "radiogroup",
            "region",
            "row",
            "rowgroup",
            "rowheader",
            "scrollbar",
            "search",
            "searchbox",
            "separator",
            "slider",
            "spinbutton",
            "status",
            "switch",
            "tab",
            "table",
            "tablist",
            "tabpanel",
            "term",
            "textbox",
            "timer",
            "toolbar",
            "tooltip",
            "tree",
            "treegrid",
            "treeitem",
        ]
        | Var[
            Literal[
                "alert",
                "alertdialog",
                "application",
                "article",
                "banner",
                "button",
                "cell",
                "checkbox",
                "columnheader",
                "combobox",
                "complementary",
                "contentinfo",
                "definition",
                "dialog",
                "directory",
                "document",
                "feed",
                "figure",
                "form",
                "grid",
                "gridcell",
                "group",
                "heading",
                "img",
                "link",
                "list",
                "listbox",
                "listitem",
                "log",
                "main",
                "marquee",
                "math",
                "menu",
                "menubar",
                "menuitem",
                "menuitemcheckbox",
                "menuitemradio",
                "navigation",
                "none",
                "note",
                "option",
                "presentation",
                "progressbar",
                "radio",
                "radiogroup",
                "region",
                "row",
                "rowgroup",
                "rowheader",
                "scrollbar",
                "search",
                "searchbox",
                "separator",
                "slider",
                "spinbutton",
                "status",
                "switch",
                "tab",
                "table",
                "tablist",
                "tabpanel",
                "term",
                "textbox",
                "timer",
                "toolbar",
                "tooltip",
                "tree",
                "treegrid",
                "treeitem",
            ]
        ]
        | None = None,
        slot: Var[str] | str | None = None,
        spell_check: Var[bool] | bool | None = None,
        tab_index: Var[int] | int | None = None,
        title: Var[str] | str | None = None,
        unstyled: Var[bool] | bool | None = None,
        style: Sequence[Mapping[str, Any]]
        | Mapping[str, Any]
        | Var[Mapping[str, Any]]
        | Breakpoints
        | None = None,
        key: Any | None = None,
        id: Any | None = None,
        ref: Var | None = None,
        class_name: Any | None = None,
        autofocus: bool | None = None,
        custom_attrs: dict[str, Var | Any] | None = None,
        on_blur: EventType[()] | None = None,
        on_click: EventType[()] | EventType[PointerEventInfo] | None = None,
        on_context_menu: EventType[()] | EventType[PointerEventInfo] | None = None,
        on_double_click: EventType[()] | EventType[PointerEventInfo] | None = None,
        on_focus: EventType[()] | None = None,
        on_mount: EventType[()] | None = None,
        on_mouse_down: EventType[()] | None = None,
        on_mouse_enter: EventType[()] | None = None,
        on_mouse_leave: EventType[()] | None = None,
        on_mouse_move: EventType[()] | None = None,
        on_mouse_out: EventType[()] | None = None,
        on_mouse_over: EventType[()] | None = None,
        on_mouse_up: EventType[()] | None = None,
        on_scroll: EventType[()] | None = None,
        on_scroll_end: EventType[()] | None = None,
        on_unmount: EventType[()] | None = None,
        **props,
    ) -> Button:
        """Create the button component."""

    @staticmethod
    def validate_variant(variant: LiteralButtonVariant): ...
    @staticmethod
    def validate_size(size: LiteralButtonSize): ...

button = Button.create
