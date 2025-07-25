"""Stub file for reflex_ui/components/base/toggle_group.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from collections.abc import Mapping, Sequence
from typing import Any, Literal

from reflex.components.component import Component
from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType, PointerEventInfo
from reflex.vars.base import Var

from reflex_ui.components.base_ui import BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]

class ClassNames:
    ROOT = "inline-flex items-center gap-1 p-1 rounded-ui-md bg-secondary-3 data-[orientation=vertical]:flex-col data-[disabled]:opacity-50 data-[disabled]:cursor-not-allowed"

class ToggleGroupBaseComponent(BaseUIComponent):
    @property
    def import_var(self): ...
    @classmethod
    def create(
        cls,
        *children,
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
    ) -> ToggleGroupBaseComponent:
        """Create the component.

        Args:
            *children: The children of the component.
            unstyled: Whether the component should be unstyled
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            ref: The Var to pass as the ref to the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """

class ToggleGroupRoot(ToggleGroupBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        default_value: Var[list[int | str]] | list[int | str] | None = None,
        value: Var[list[int | str]] | list[int | str] | None = None,
        toggle_multiple: Var[bool] | bool | None = None,
        disabled: Var[bool] | bool | None = None,
        loop: Var[bool] | bool | None = None,
        orientation: Literal["horizontal", "vertical"]
        | Var[Literal["horizontal", "vertical"]]
        | None = None,
        render_: Component | Var[Component] | None = None,
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
        on_value_change: EventType[()]
        | EventType[list[str | int]]
        | EventType[list[str | int], dict]
        | None = None,
        **props,
    ) -> ToggleGroupRoot:
        """Create the toggle group root component."""

toggle_group = ToggleGroupRoot.create
