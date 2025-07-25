"""Stub file for reflex_ui/components/base/gradient_profile.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from collections.abc import Mapping, Sequence
from typing import Any

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType, PointerEventInfo
from reflex.vars.base import Var

from reflex_ui.components.component import CoreComponent

DEFAULT_CLASS_NAME = "size-4 pointer-events-none rounded-full"

class GradientProfile(CoreComponent):
    @classmethod
    def create(
        cls,
        *children,
        seed: Var[int | str] | int | str | None = None,
        available_colors: Var[list[str]] | list[str] | None = None,
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
    ) -> GradientProfile:
        """Create the gradient profile component."""

gradient_profile = GradientProfile.create
