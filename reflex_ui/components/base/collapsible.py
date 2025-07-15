"""Custom collapsible component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent


class ClassNames:
    """Class names for collapsible components."""

    ROOT = ""
    TRIGGER = "cursor-pointer focus:outline-none focus-visible:ring-1 focus-visible:ring-primary-4"
    PANEL = "overflow-hidden transition-all duration-200 data-[state=closed]:animate-collapse-up data-[state=open]:animate-collapse-down"


class CollapsibleBaseComponent(BaseUIComponent):
    """Base component for collapsible components."""

    library = f"{PACKAGE_NAME}/collapsible"

    @property
    def import_var(self):
        """Return the import variable for the collapsible component."""
        return ImportVar(tag="Collapsible", package_path="", install=False)


class CollapsibleRoot(CollapsibleBaseComponent):
    """Groups all parts of the collapsible. Doesn't render its own HTML element."""

    tag = "Collapsible.Root"

    default_open: Var[bool]

    open: Var[bool]

    on_open_change: EventHandler[passthrough_event_spec(bool)]

    # Whether the component should ignore user interaction.
    disabled: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible root component."""
        props["data-slot"] = "collapsible"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CollapsibleTrigger(CollapsibleBaseComponent):
    """A button that opens and closes the collapsible panel. Renders a <button> element."""

    tag = "Collapsible.Trigger"

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible trigger component."""
        props["data-slot"] = "collapsible-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class CollapsiblePanel(CollapsibleBaseComponent):
    """A panel with the collapsible contents. Renders a <div> element."""

    tag = "Collapsible.Panel"

    hidden_until_found: Var[bool]

    keep_mounted: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible panel component."""
        props["data-slot"] = "collapsible-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class HighLevelCollapsible(CollapsibleRoot):
    """High level collapsible component."""

    trigger: Var[Component | None]
    content: Var[str | Component | None]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the collapsible component."""
        trigger = props.pop("trigger", None)
        content = props.pop("content", None)
        class_name = props.pop("class_name", "")

        return CollapsibleRoot.create(
            CollapsibleTrigger.create(render_=trigger) if trigger else None,
            CollapsiblePanel.create(
                content,
                *children,
                class_name=class_name,
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "trigger",
            "content",
        ]


class Collapsible(ComponentNamespace):
    """Namespace for Collapsible components."""

    root = staticmethod(CollapsibleRoot.create)
    trigger = staticmethod(CollapsibleTrigger.create)
    panel = staticmethod(CollapsiblePanel.create)
    __call__ = staticmethod(HighLevelCollapsible.create)


collapsible = Collapsible()
