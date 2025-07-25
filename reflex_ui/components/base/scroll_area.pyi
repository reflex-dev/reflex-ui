"""Stub file for reflex_ui/components/base/scroll_area.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from collections.abc import Mapping, Sequence
from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType, PointerEventInfo
from reflex.vars.base import Var

from reflex_ui.components.base_ui import BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]

class ClassNames:
    ROOT = "h-full outline-none focus:outline-none"
    VIEWPORT = "h-full overscroll-contain"
    CONTENT = ""
    SCROLLBAR_BASE = "flex touch-none p-0.5 opacity-0 transition-[colors,opacity] delay-200 select-none data-hovering:opacity-100 data-hovering:delay-0 data-hovering:duration-100 data-scrolling:opacity-100 data-scrolling:delay-0 data-scrolling:duration-100"
    SCROLLBAR_VERTICAL = "w-2"
    SCROLLBAR_HORIZONTAL = "h-2"
    THUMB = "w-full rounded-full bg-secondary-a5"
    CORNER = "bg-secondary-a3"

class ScrollAreaBaseComponent(BaseUIComponent):
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
    ) -> ScrollAreaBaseComponent:
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

class ScrollAreaRoot(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
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
        **props,
    ) -> ScrollAreaRoot:
        """Create the scroll area root component."""

class ScrollAreaViewport(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
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
        **props,
    ) -> ScrollAreaViewport:
        """Create the scroll area viewport component."""

class ScrollAreaContent(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
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
        **props,
    ) -> ScrollAreaContent:
        """Create the scroll area content component."""

class ScrollAreaScrollbar(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        orientation: Literal["horizontal", "vertical"]
        | Var[Literal["horizontal", "vertical"]]
        | None = None,
        keep_mounted: Var[bool] | bool | None = None,
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
        **props,
    ) -> ScrollAreaScrollbar:
        """Create the scroll area scrollbar component."""

class ScrollAreaThumb(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
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
        **props,
    ) -> ScrollAreaThumb:
        """Create the scroll area thumb component."""

class ScrollAreaCorner(ScrollAreaBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
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
        **props,
    ) -> ScrollAreaCorner:
        """Create the scroll area corner component."""

class HighLevelScrollArea(ScrollAreaRoot):
    @classmethod
    def create(
        cls,
        *children,
        orientation: Literal["horizontal", "vertical"]
        | Var[Literal["horizontal", "vertical"]]
        | None = None,
        keep_mounted: Var[bool] | bool | None = None,
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
        **props,
    ) -> HighLevelScrollArea:
        """Create a high level scroll area component.

        Args:
            *children: The content to be scrollable.
            orientation: Orientation of the scroll area
            keep_mounted: Whether to keep the HTML element in the DOM when the viewport isn't scrollable
            render_: Render prop
            unstyled: Whether the component should be unstyled
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            ref: The Var to pass as the ref to the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the scroll area component.

        Returns:
            The scroll area component.
        """

class ScrollArea(ComponentNamespace):
    root = staticmethod(ScrollAreaRoot.create)
    viewport = staticmethod(ScrollAreaViewport.create)
    content = staticmethod(ScrollAreaContent.create)
    scrollbar = staticmethod(ScrollAreaScrollbar.create)
    thumb = staticmethod(ScrollAreaThumb.create)
    corner = staticmethod(ScrollAreaCorner.create)

    @staticmethod
    def __call__(
        *children,
        orientation: Literal["horizontal", "vertical"]
        | Var[Literal["horizontal", "vertical"]]
        | None = None,
        keep_mounted: Var[bool] | bool | None = None,
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
        **props,
    ) -> HighLevelScrollArea:
        """Create a high level scroll area component.

        Args:
            *children: The content to be scrollable.
            orientation: Orientation of the scroll area
            keep_mounted: Whether to keep the HTML element in the DOM when the viewport isn't scrollable
            render_: Render prop
            unstyled: Whether the component should be unstyled
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            ref: The Var to pass as the ref to the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the scroll area component.

        Returns:
            The scroll area component.
        """

scroll_area = ScrollArea()
