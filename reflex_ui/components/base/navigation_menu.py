"""Custom navigation menu component."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent

LiteralNavigationMenuOrientation = Literal["horizontal", "vertical"]
LiteralSide = Literal["top", "right", "bottom", "left"]
LiteralAlign = Literal["start", "center", "end"]
LiteralPositionMethod = Literal["absolute", "fixed"]
LiteralCollisionAvoidance = Literal["flip", "shift", "auto"]


class ClassNames:
    """Class names for navigation menu components."""

    ROOT = "relative"
    LIST = "flex items-center gap-1"
    ITEM = "relative"
    TRIGGER = "flex items-center gap-2 px-4 py-2 text-sm font-medium rounded-md hover:bg-secondary-3 focus:outline-none focus-visible:ring-1 focus-visible:ring-primary-4 cursor-pointer select-none transition-colors"
    CONTENT = "absolute top-full left-0 mt-2 min-w-64 origin-top-left border border-secondary-a4 bg-secondary-1 shadow-large rounded-lg p-2 z-50 transition-[transform,scale,opacity] data-[ending-style]:scale-95 data-[starting-style]:scale-95 data-[ending-style]:opacity-0 data-[starting-style]:opacity-0"
    LINK = "block px-3 py-2 text-sm text-secondary-12 hover:bg-secondary-3 rounded-md cursor-pointer select-none outline-none focus:bg-secondary-3 transition-colors"
    ICON = "size-4 text-secondary-10 transition-transform data-[popup-open]:rotate-180"
    PORTAL = "relative"
    POSITIONER = "outline-none"
    POPUP = "outline-none"
    VIEWPORT = "relative overflow-hidden rounded-lg"
    ARROW = "fill-secondary-1 stroke-secondary-a4 data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] data-[side=top]:rotate-180"
    BACKDROP = "fixed inset-0 z-40"


class NavigationMenuBaseComponent(BaseUIComponent):
    """Base component for navigation menu components."""

    library = f"{PACKAGE_NAME}/navigation-menu"

    @property
    def import_var(self):
        """Return the import variable for the navigation menu component."""
        return ImportVar(tag="NavigationMenu", package_path="", install=False)


class NavigationMenuRoot(NavigationMenuBaseComponent):
    """Groups all parts of the navigation menu. Renders a <nav> element."""

    tag = "NavigationMenu.Root"

    value: Var[str]

    default_value: Var[str]

    on_value_change: EventHandler[passthrough_event_spec(str, dict)]

    orientation: Var[LiteralNavigationMenuOrientation]

    delay: Var[int]

    close_delay: Var[int]

    actions_ref: Var[str]

    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu root component."""
        props["data-slot"] = "navigation-menu"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class NavigationMenuList(NavigationMenuBaseComponent):
    """Contains a list of navigation menu items. Renders a <div> element."""

    tag = "NavigationMenu.List"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu list component."""
        props["data-slot"] = "navigation-menu-list"
        cls.set_class_name(ClassNames.LIST, props)
        return super().create(*children, **props)


class NavigationMenuItem(NavigationMenuBaseComponent):
    """An individual navigation menu item. Renders a <div> element."""

    tag = "NavigationMenu.Item"

    value: Var[str]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu item component."""
        props["data-slot"] = "navigation-menu-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class NavigationMenuTrigger(NavigationMenuBaseComponent):
    """Opens the navigation menu popup when hovered or clicked, revealing the associated content. Renders a <button> element."""

    tag = "NavigationMenu.Trigger"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu trigger component."""
        props["data-slot"] = "navigation-menu-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class NavigationMenuContent(NavigationMenuBaseComponent):
    """A container for the content of the navigation menu item that is moved into the popup when the item is active. Renders a <div> element."""

    tag = "NavigationMenu.Content"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu content component."""
        props["data-slot"] = "navigation-menu-content"
        cls.set_class_name(ClassNames.CONTENT, props)
        return super().create(*children, **props)


class NavigationMenuLink(NavigationMenuBaseComponent):
    """A link in the navigation menu that can be used to navigate to a different page or section. Renders an <a> element."""

    tag = "NavigationMenu.Link"

    active: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu link component."""
        props["data-slot"] = "navigation-menu-link"
        cls.set_class_name(ClassNames.LINK, props)
        return super().create(*children, **props)


class NavigationMenuIcon(NavigationMenuBaseComponent):
    """An icon that indicates that the trigger button opens a menu. Renders a <span> element."""

    tag = "NavigationMenu.Icon"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu icon component."""
        props["data-slot"] = "navigation-menu-icon"
        cls.set_class_name(ClassNames.ICON, props)
        return super().create(*children, **props)


class NavigationMenuPortal(NavigationMenuBaseComponent):
    """A portal element that moves the content to a different part of the DOM."""

    tag = "NavigationMenu.Portal"

    # A parent element to render the portal element into.
    container: Var[str]

    # Whether to keep the portal mounted in the DOM while the content is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu portal component."""
        props["data-slot"] = "navigation-menu-portal"
        cls.set_class_name(ClassNames.PORTAL, props)
        return super().create(*children, **props)


class NavigationMenuPositioner(NavigationMenuBaseComponent):
    """Positions the content against the trigger. Renders a <div> element."""

    tag = "NavigationMenu.Positioner"

    # Determines how to handle collisions when positioning the content.
    collision_avoidance: Var[bool | LiteralCollisionAvoidance]

    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the content against. May automatically change to avoid collisions. Defaults to "bottom".
    side: Var[LiteralSide]

    # Distance between the anchor and the content in pixels. Defaults to 0.
    side_offset: Var[int]

    # Minimum distance to maintain between the arrow and the edges of the content. Use it to prevent the arrow element from hanging out of the rounded corners of a content. Defaults to 5.
    arrow_padding: Var[int]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int]

    # An element or a rectangle that delimits the area that the content is confined to. Defaults to the "clipping-ancestors".
    collision_boundary: Var[str]

    sticky: Var[bool]

    track_anchor: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPositionMethod]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu positioner component."""
        props["data-slot"] = "navigation-menu-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class NavigationMenuPopup(NavigationMenuBaseComponent):
    """A container for the navigation menu content. Renders a <div> element."""

    tag = "NavigationMenu.Popup"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu popup component."""
        props["data-slot"] = "navigation-menu-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class NavigationMenuViewport(NavigationMenuBaseComponent):
    """An optional viewport element that masks the content when it overflows. Renders a <div> element."""

    tag = "NavigationMenu.Viewport"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu viewport component."""
        props["data-slot"] = "navigation-menu-viewport"
        cls.set_class_name(ClassNames.VIEWPORT, props)
        return super().create(*children, **props)


class NavigationMenuArrow(NavigationMenuBaseComponent):
    """Displays an element positioned against the navigation menu anchor. Renders a <div> element."""

    tag = "NavigationMenu.Arrow"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu arrow component."""
        props["data-slot"] = "navigation-menu-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class NavigationMenuBackdrop(NavigationMenuBaseComponent):
    """An optional backdrop element that can be used to close the navigation menu. Renders a <div> element."""

    tag = "NavigationMenu.Backdrop"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the navigation menu backdrop component."""
        props["data-slot"] = "navigation-menu-backdrop"
        cls.set_class_name(ClassNames.BACKDROP, props)
        return super().create(*children, **props)


class NavigationMenu(ComponentNamespace):
    """Namespace for NavigationMenu components."""

    root = staticmethod(NavigationMenuRoot.create)
    list = staticmethod(NavigationMenuList.create)
    item = staticmethod(NavigationMenuItem.create)
    trigger = staticmethod(NavigationMenuTrigger.create)
    content = staticmethod(NavigationMenuContent.create)
    link = staticmethod(NavigationMenuLink.create)
    icon = staticmethod(NavigationMenuIcon.create)
    portal = staticmethod(NavigationMenuPortal.create)
    positioner = staticmethod(NavigationMenuPositioner.create)
    popup = staticmethod(NavigationMenuPopup.create)
    viewport = staticmethod(NavigationMenuViewport.create)
    arrow = staticmethod(NavigationMenuArrow.create)
    backdrop = staticmethod(NavigationMenuBackdrop.create)


navigation_menu = NavigationMenu()
