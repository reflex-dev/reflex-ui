"""Stub file for reflex_ui/components/base/tooltip.py"""

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

LiteralSide = Literal["top", "right", "bottom", "left", "inline-end", "inline-start"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]
LiteralTrackCursorAxis = Literal["none", "bottom", "x", "y"]

class ClassNames:
    TRIGGER = "inline-flex items-center justify-center"
    POPUP = "z-50 rounded-ui-sm bg-secondary-12 px-2.5 py-1.5 text-balance text-sm font-medium text-secondary-1 shadow-small transition-all duration-150 data-[ending-style]:scale-90 data-[ending-style]:opacity-0 data-[starting-style]:scale-90 data-[starting-style]:opacity-0"
    ARROW = "data-[side=bottom]:top-[-7.5px] data-[side=left]:right-[-12.5px] data-[side=left]:rotate-90 data-[side=right]:left-[-12.5px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-7.5px] data-[side=top]:rotate-180"

class TooltipBaseComponent(BaseUIComponent):
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
    ) -> TooltipBaseComponent:
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

class TooltipRoot(TooltipBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        open: Var[bool] | bool | None = None,
        default_open: Var[bool] | bool | None = None,
        track_cursor_axis: Literal["bottom", "none", "x", "y"]
        | Var[Literal["bottom", "none", "x", "y"]]
        | None = None,
        disabled: Var[bool] | bool | None = None,
        delay: Var[int] | int | None = None,
        close_delay: Var[int] | int | None = None,
        hoverable: Var[bool] | bool | None = None,
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
        on_open_change: EventType[()]
        | EventType[bool]
        | EventType[bool, dict]
        | EventType[bool, dict, str]
        | None = None,
        on_open_change_complete: EventType[()] | EventType[bool] | None = None,
        on_scroll: EventType[()] | None = None,
        on_scroll_end: EventType[()] | None = None,
        on_unmount: EventType[()] | None = None,
        **props,
    ) -> TooltipRoot:
        """Create the tooltip root component."""

class TooltipProvider(TooltipBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        delay: Var[int] | int | None = None,
        close_delay: Var[int] | int | None = None,
        timeout: Var[int] | int | None = None,
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
    ) -> TooltipProvider:
        """Create the tooltip provider component."""

class TooltipTrigger(TooltipBaseComponent):
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
    ) -> TooltipTrigger:
        """Create the tooltip trigger component."""

class TooltipPortal(TooltipBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        container: Var[str] | str | None = None,
        keep_mounted: Var[bool] | bool | None = None,
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
    ) -> TooltipPortal:
        """Create the tooltip portal component."""

class TooltipPositioner(TooltipBaseComponent):
    @classmethod
    def create(
        cls,
        *children,
        align: Literal["center", "end", "start"]
        | Var[Literal["center", "end", "start"]]
        | None = None,
        align_offset: Var[int] | int | None = None,
        side: Literal["bottom", "inline-end", "inline-start", "left", "right", "top"]
        | Var[Literal["bottom", "inline-end", "inline-start", "left", "right", "top"]]
        | None = None,
        side_offset: Var[int] | int | None = None,
        arrow_padding: Var[int] | int | None = None,
        anchor: Var[str] | str | None = None,
        collision_boundary: Var[str] | str | None = None,
        collision_padding: Var[int] | int | None = None,
        sticky: Var[bool] | bool | None = None,
        position_method: Literal["absolute", "fixed"]
        | Var[Literal["absolute", "fixed"]]
        | None = None,
        track_anchor: Var[bool] | bool | None = None,
        collision_avoidance: Var[str] | str | None = None,
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
    ) -> TooltipPositioner:
        """Create the tooltip positioner component."""

class TooltipPopup(TooltipBaseComponent):
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
    ) -> TooltipPopup:
        """Create the tooltip popup component."""

class TooltipArrow(TooltipBaseComponent):
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
    ) -> TooltipArrow:
        """Create the tooltip arrow component."""

class HighLevelTooltip(TooltipRoot):
    @classmethod
    def create(
        cls,
        *children,
        content: Component | Var[str] | str = None,
        open: Var[bool] | bool | None = None,
        default_open: Var[bool] | bool | None = None,
        track_cursor_axis: Literal["bottom", "none", "x", "y"]
        | Var[Literal["bottom", "none", "x", "y"]]
        | None = None,
        disabled: Var[bool] | bool | None = None,
        delay: Var[int] | int | None = None,
        close_delay: Var[int] | int | None = None,
        hoverable: Var[bool] | bool | None = None,
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
        on_open_change: EventType[()]
        | EventType[bool]
        | EventType[bool, dict]
        | EventType[bool, dict, str]
        | None = None,
        on_open_change_complete: EventType[()] | EventType[bool] | None = None,
        on_scroll: EventType[()] | None = None,
        on_scroll_end: EventType[()] | None = None,
        on_unmount: EventType[()] | None = None,
        **props,
    ) -> HighLevelTooltip:
        """Create a high level tooltip component.

        Args:
            trigger_component: The component that triggers the tooltip.
            content: The content to display in the tooltip.
            content: Content to display in the tooltip
            open: Whether the tooltip is currently open.
            default_open: Whether the tooltip is initially open. To render a controlled tooltip, use the open prop instead. Defaults to False.
            on_open_change: Event handler called when the tooltip is opened or closed.
            on_open_change_complete: Event handler called after any animations complete when the tooltip is opened or closed.
            track_cursor_axis: Determines which axis the tooltip should track the cursor on. Defaults to "None".
            disabled: Whether the tooltip is disabled. Defaults to False.
            delay: How long to wait before opening the tooltip. Specified in milliseconds. Defaults to 600.
            close_delay: How long to wait before closing the tooltip. Specified in milliseconds. Defaults to 0.
            hoverable: Whether the tooltip contents can be hovered without closing the tooltip. Defaults to True.
            unstyled: Whether the component should be unstyled
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            ref: The Var to pass as the ref to the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the tooltip component.

        Returns:
            The tooltip component with all necessary subcomponents.
        """

class Tooltip(ComponentNamespace):
    provider = staticmethod(TooltipProvider.create)
    root = staticmethod(TooltipRoot.create)
    trigger = staticmethod(TooltipTrigger.create)
    portal = staticmethod(TooltipPortal.create)
    positioner = staticmethod(TooltipPositioner.create)
    popup = staticmethod(TooltipPopup.create)
    arrow = staticmethod(TooltipArrow.create)

    @staticmethod
    def __call__(
        *children,
        content: Component | Var[str] | str = None,
        open: Var[bool] | bool | None = None,
        default_open: Var[bool] | bool | None = None,
        track_cursor_axis: Literal["bottom", "none", "x", "y"]
        | Var[Literal["bottom", "none", "x", "y"]]
        | None = None,
        disabled: Var[bool] | bool | None = None,
        delay: Var[int] | int | None = None,
        close_delay: Var[int] | int | None = None,
        hoverable: Var[bool] | bool | None = None,
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
        on_open_change: EventType[()]
        | EventType[bool]
        | EventType[bool, dict]
        | EventType[bool, dict, str]
        | None = None,
        on_open_change_complete: EventType[()] | EventType[bool] | None = None,
        on_scroll: EventType[()] | None = None,
        on_scroll_end: EventType[()] | None = None,
        on_unmount: EventType[()] | None = None,
        **props,
    ) -> HighLevelTooltip:
        """Create a high level tooltip component.

        Args:
            trigger_component: The component that triggers the tooltip.
            content: The content to display in the tooltip.
            content: Content to display in the tooltip
            open: Whether the tooltip is currently open.
            default_open: Whether the tooltip is initially open. To render a controlled tooltip, use the open prop instead. Defaults to False.
            on_open_change: Event handler called when the tooltip is opened or closed.
            on_open_change_complete: Event handler called after any animations complete when the tooltip is opened or closed.
            track_cursor_axis: Determines which axis the tooltip should track the cursor on. Defaults to "None".
            disabled: Whether the tooltip is disabled. Defaults to False.
            delay: How long to wait before opening the tooltip. Specified in milliseconds. Defaults to 600.
            close_delay: How long to wait before closing the tooltip. Specified in milliseconds. Defaults to 0.
            hoverable: Whether the tooltip contents can be hovered without closing the tooltip. Defaults to True.
            unstyled: Whether the component should be unstyled
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            ref: The Var to pass as the ref to the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Additional properties to apply to the tooltip component.

        Returns:
            The tooltip component with all necessary subcomponents.
        """

tooltip = Tooltip()
