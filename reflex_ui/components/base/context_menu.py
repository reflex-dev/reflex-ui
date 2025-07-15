"""Custom context menu component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOpenChangeReason = Literal[
    "arrowKey",
    "escapeKey",
    "select",
    "hover",
    "click",
    "focus",
    "dismiss",
    "typeahead",
    "tab",
]
LiteralMenuOrientation = Literal["vertical", "horizontal"]
LiteralSide = Literal["top", "right", "bottom", "left"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]
LiteralCollisionAvoidance = Literal["flip", "shift", "auto"]


class ClassNames:
    """Class names for context menu components."""

    TRIGGER = "cursor-context-menu"
    PORTAL = "relative"
    BACKDROP = "fixed inset-0 z-40"
    POPUP = "group/popup max-h-[17.25rem] overflow-y-auto origin-(--transform-origin) p-1 border border-secondary-a4 bg-secondary-1 shadow-large transition-[transform,scale,opacity] data-[ending-style]:scale-95 data-[starting-style]:scale-95 data-[ending-style]:opacity-0 data-[starting-style]:opacity-0 outline-none scrollbar-thin scrollbar-thumb-secondary-9 scrollbar-track-transparent"
    ITEM = "grid min-w-(--anchor-width) grid-cols-[1fr_auto] items-center gap-2 text-sm select-none font-medium text-secondary-12 cursor-pointer outline-none data-[highlighted]:bg-secondary-3 scroll-m-1 text-start"
    SEPARATOR = "-mx-1 my-1 h-px bg-muted"
    ARROW = "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] data-[side=top]:rotate-180"
    POSITIONER = "outline-none"
    GROUP = "p-1"
    GROUP_LABEL = "px-2 py-1.5 text-sm font-semibold"
    RADIO_GROUP = ""
    RADIO_ITEM = "grid min-w-(--anchor-width) grid-cols-[1fr_auto] items-center gap-2 text-sm select-none font-[450] text-secondary-11 cursor-pointer outline-none data-[highlighted]:bg-secondary-3 scroll-m-1"
    RADIO_ITEM_INDICATOR = "text-current"
    CHECKBOX_ITEM = "grid min-w-(--anchor-width) grid-cols-[1fr_auto] items-center gap-2 text-sm select-none font-[450] text-secondary-11 cursor-pointer outline-none data-[highlighted]:bg-secondary-3 scroll-m-1"
    CHECKBOX_ITEM_INDICATOR = "text-current"
    SUBMENU_TRIGGER = "grid min-w-(--anchor-width) grid-cols-[1fr_auto] items-center gap-2 text-sm select-none font-[450] text-secondary-11 cursor-pointer outline-none data-[highlighted]:bg-secondary-3 scroll-m-1"


class ContextMenuBaseComponent(BaseUIComponent):
    """Base component for context menu components."""

    library = f"{PACKAGE_NAME}/context-menu"

    @property
    def import_var(self):
        """Return the import variable for the context menu component."""
        return ImportVar(tag="ContextMenu", package_path="", install=False)


class ContextMenuRoot(ContextMenuBaseComponent):
    """Groups all parts of the context menu. Doesn't render its own HTML element."""

    tag = "ContextMenu.Root"

    # Whether the context menu is initially open. To render a controlled context menu, use the open prop instead. Defaults to False.
    default_open: Var[bool]
    # Whether the context menu is currently open.
    open: Var[bool]
    # Event handler called when the context menu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    action_ref: Var[str]
    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]
    # Event handler called after any animations complete when the context menu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu root component."""
        props["data-slot"] = "context-menu"
        return super().create(*children, **props)


class ContextMenuTrigger(ContextMenuBaseComponent):
    """A component that opens the context menu when right-clicked. Renders a <div> element."""

    tag = "ContextMenu.Trigger"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu trigger component."""
        props["data-slot"] = "context-menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class ContextMenuPortal(ContextMenuBaseComponent):
    """A portal element that moves the popup to a different part of the DOM. By default, the portal element is appended to <body>."""

    tag = "ContextMenu.Portal"

    # A parent element to render the portal element into. Defaults to document.body.
    container: Var[str]
    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu portal component."""
        props["data-slot"] = "context-menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class ContextMenuBackdrop(ContextMenuBaseComponent):
    """A backdrop element that covers the entire viewport when the context menu is open. Renders a <div> element."""

    tag = "ContextMenu.Backdrop"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu backdrop component."""
        props["data-slot"] = "context-menu-backdrop"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class ContextMenuPositioner(ContextMenuBaseComponent):
    """Positions the context menu popup against the trigger. Renders a <div> element."""

    tag = "ContextMenu.Positioner"

    # Determines how to handle collisions when positioning the popup. Defaults to True.
    collision_avoidance: Var[bool | LiteralCollisionAvoidance]
    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]
    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]
    # Which side of the anchor element to align the popup against. May automatically change to avoid collisions. Defaults to "bottom".
    side: Var[LiteralSide]
    # Distance between the anchor and the popup in pixels. Defaults to 4.
    side_offset: Var[int]
    # Minimum distance to maintain between the arrow and the edges of the popup. Defaults to 5.
    arrow_padding: Var[int]
    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int]
    # An element or a rectangle that delimits the area that the popup is confined to. Defaults to "clipping-ancestors".
    collision_boundary: Var[str]
    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]
    # Whether the popup tracks any layout shift of its positioning anchor. Defaults to True.
    track_anchor: Var[bool]
    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPositionMethod]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu positioner component."""
        props["data-slot"] = "context-menu-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class ContextMenuPopup(ContextMenuBaseComponent):
    """A container for the context menu items. Renders a <div> element."""

    tag = "ContextMenu.Popup"

    # Determines the element to focus when the context menu is closed. By default, focus returns to the trigger.
    final_focus: Var[str]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu popup component."""
        props["data-slot"] = "context-menu-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class ContextMenuArrow(ContextMenuBaseComponent):
    """Displays an element positioned against the context menu anchor. Renders a <div> element."""

    tag = "ContextMenu.Arrow"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu arrow component."""
        props["data-slot"] = "context-menu-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class ContextMenuItem(ContextMenuBaseComponent):
    """An individual interactive item in the context menu. Renders a <div> element."""

    tag = "ContextMenu.Item"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]
    # Whether to close the context menu when the item is clicked. Defaults to True.
    close_on_click: Var[bool]
    # Whether the component renders a native button element when replacing it via the render prop. Defaults to False.
    native_button: Var[bool]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu item component."""
        props["data-slot"] = "context-menu-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class ContextMenuSeparator(ContextMenuBaseComponent):
    """A separator element accessible to screen readers. Renders a <div> element."""

    tag = "ContextMenu.Separator"

    # The orientation of the separator. Defaults to "horizontal".
    orientation: Var[LiteralMenuOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu separator component."""
        props["data-slot"] = "context-menu-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ContextMenuGroup(ContextMenuBaseComponent):
    """Groups related context menu items with the corresponding label. Renders a <div> element."""

    tag = "ContextMenu.Group"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu group component."""
        props["data-slot"] = "context-menu-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class ContextMenuGroupLabel(ContextMenuBaseComponent):
    """An accessible label that is automatically associated with its parent group. Renders a <div> element."""

    tag = "ContextMenu.GroupLabel"

    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu group label component."""
        props["data-slot"] = "context-menu-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class ContextMenuRadioGroup(ContextMenuBaseComponent):
    """Groups related radio items. Renders a <div> element."""

    tag = "ContextMenu.RadioGroup"

    default_value: Var[str | int]
    # The controlled value of the radio group.
    value: Var[str | int]
    # Event handler called when the value changes.
    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio group component."""
        props["data-slot"] = "context-menu-radio-group"
        cls.set_class_name(ClassNames.RADIO_GROUP, props)
        return super().create(*children, **props)


class ContextMenuRadioItem(ContextMenuBaseComponent):
    """A context menu item that works like a radio button in a given group. Renders a <div> element."""

    tag = "ContextMenu.RadioItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]
    value: Var[str | int]
    # Whether to close the context menu when the item is clicked. Defaults to True.
    close_on_click: Var[bool]
    # Whether the component renders a native button element when replacing it via the render prop. Defaults to False.
    native_button: Var[bool]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio item component."""
        props["data-slot"] = "context-menu-radio-item"
        cls.set_class_name(ClassNames.RADIO_ITEM, props)
        return super().create(*children, **props)


class ContextMenuRadioItemIndicator(ContextMenuBaseComponent):
    """Indicates whether the radio item is selected. Renders a <div> element."""

    tag = "ContextMenu.RadioItemIndicator"

    # Whether to keep the indicator mounted in the DOM when the radio item is not checked. Defaults to False.
    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu radio item indicator component."""
        props["data-slot"] = "context-menu-radio-item-indicator"
        cls.set_class_name(ClassNames.RADIO_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItem(ContextMenuBaseComponent):
    """A context menu item that toggles a setting on or off. Renders a <div> element."""

    tag = "ContextMenu.CheckboxItem"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]
    default_checked: Var[bool]
    # The controlled checked state of the checkbox item.
    checked: Var[bool]
    # Event handler called when the checked state changes.
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]
    # Whether to close the context menu when the item is clicked. Defaults to True.
    close_on_click: Var[bool]
    # Whether the component renders a native button element when replacing it via the render prop. Defaults to False.
    native_button: Var[bool]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu checkbox item component."""
        props["data-slot"] = "context-menu-checkbox-item"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM, props)
        return super().create(*children, **props)


class ContextMenuCheckboxItemIndicator(ContextMenuBaseComponent):
    """Indicates whether the checkbox item is ticked. Renders a <div> element."""

    tag = "ContextMenu.CheckboxItemIndicator"

    # Whether to keep the indicator mounted in the DOM when the checkbox item is not checked. Defaults to False.
    keep_mounted: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu checkbox item indicator component."""
        props["data-slot"] = "context-menu-checkbox-item-indicator"
        cls.set_class_name(ClassNames.CHECKBOX_ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ContextMenuSubmenuRoot(ContextMenuBaseComponent):
    """Groups all parts of a submenu. Doesn't render its own HTML element."""

    tag = "ContextMenu.SubmenuRoot"

    # Whether the submenu is initially open. To render a controlled submenu, use the open prop instead. Defaults to False.
    default_open: Var[bool]
    # Whether the submenu is currently open.
    open: Var[bool]
    # Event handler called when the submenu is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    # When in a submenu, determines whether pressing the Escape key closes the entire menu, or only the current child menu. Defaults to True.
    close_parent_on_esc: Var[bool]
    # Event handler called after any animations complete when the submenu is closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]
    # Whether the submenu opens when the trigger is hovered. Defaults to False.
    open_on_hover: Var[bool]
    # The delay in milliseconds before the submenu opens when hovering. Defaults to 0.
    delay: Var[int]
    # The delay in milliseconds before the submenu closes when no longer hovering. Defaults to 0.
    close_delay: Var[int]
    # Whether keyboard navigation should loop around when reaching the end of the items. Defaults to False.
    loop: Var[bool]
    # The orientation of the submenu. Defaults to "vertical".
    orientation: Var[LiteralMenuOrientation]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu submenu root component."""
        props["data-slot"] = "context-menu-submenu-root"
        return super().create(*children, **props)


class ContextMenuSubmenuTrigger(ContextMenuBaseComponent):
    """A context menu item that opens a submenu."""

    tag = "ContextMenu.SubmenuTrigger"

    # Overrides the text label to use when the item is matched during keyboard text navigation.
    label: Var[str]
    # Whether the component renders a native button element when replacing it via the render prop. Defaults to False.
    native_button: Var[bool]
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu submenu trigger component."""
        props["data-slot"] = "context-menu-submenu-trigger"
        cls.set_class_name(ClassNames.SUBMENU_TRIGGER, props)
        return super().create(*children, **props)


class ContextMenu(ComponentNamespace):
    """Namespace for ContextMenu components."""

    root = staticmethod(ContextMenuRoot.create)
    trigger = staticmethod(ContextMenuTrigger.create)
    portal = staticmethod(ContextMenuPortal.create)
    backdrop = staticmethod(ContextMenuBackdrop.create)
    positioner = staticmethod(ContextMenuPositioner.create)
    popup = staticmethod(ContextMenuPopup.create)
    arrow = staticmethod(ContextMenuArrow.create)
    item = staticmethod(ContextMenuItem.create)
    separator = staticmethod(ContextMenuSeparator.create)
    group = staticmethod(ContextMenuGroup.create)
    group_label = staticmethod(ContextMenuGroupLabel.create)
    radio_group = staticmethod(ContextMenuRadioGroup.create)
    radio_item = staticmethod(ContextMenuRadioItem.create)
    radio_item_indicator = staticmethod(ContextMenuRadioItemIndicator.create)
    checkbox_item = staticmethod(ContextMenuCheckboxItem.create)
    checkbox_item_indicator = staticmethod(ContextMenuCheckboxItemIndicator.create)
    submenu_root = staticmethod(ContextMenuSubmenuRoot.create)
    submenu_trigger = staticmethod(ContextMenuSubmenuTrigger.create)


context_menu = ContextMenu()
