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

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    action_ref: Var[str]
    close_parent_on_esc: Var[bool]
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the context menu root component."""
        props["data-slot"] = "context-menu"
        return super().create(*children, **props)


class ContextMenuTrigger(ContextMenuBaseComponent):
    """A component that opens the context menu when right-clicked. Renders a <div> element."""

    tag = "ContextMenu.Trigger"

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

    container: Var[str]
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

    collision_avoidance: Var[bool | LiteralCollisionAvoidance]
    align: Var[LiteralAlign]
    align_offset: Var[int]
    side: Var[LiteralSide]
    side_offset: Var[int]
    arrow_padding: Var[int]
    collision_padding: Var[int]
    collision_boundary: Var[str]
    sticky: Var[bool]
    track_anchor: Var[bool]
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

    label: Var[str]
    close_on_click: Var[bool]
    native_button: Var[bool]
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
    value: Var[str | int]
    on_value_change: EventHandler[passthrough_event_spec(str | int, dict)]
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

    label: Var[str]
    value: Var[str | int]
    close_on_click: Var[bool]
    native_button: Var[bool]
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

    label: Var[str]
    default_checked: Var[bool]
    checked: Var[bool]
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]
    close_on_click: Var[bool]
    native_button: Var[bool]
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

    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventHandler[passthrough_event_spec(bool, dict)]
    close_parent_on_esc: Var[bool]
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]
    disabled: Var[bool]
    open_on_hover: Var[bool]
    delay: Var[int]
    close_delay: Var[int]
    loop: Var[bool]
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

    label: Var[str]
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
