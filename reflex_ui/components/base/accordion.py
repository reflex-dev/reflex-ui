"""Accordion component from base-ui components."""

from typing import Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent

LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for accordion components."""

    ROOT = "flex flex-col"
    ITEM = "border-b border-secondary-a4 last:border-b-0"
    HEADER = ""
    TRIGGER = "flex w-full items-center justify-between py-4 text-left font-medium transition-all hover:underline [&[data-open]>svg]:rotate-180"
    PANEL = "overflow-hidden text-sm transition-all data-[ending-style]:animate-accordion-up data-[starting-style]:animate-accordion-down"


class AccordionBaseComponent(BaseUIComponent):
    """Base component for accordion components."""

    library = f"{PACKAGE_NAME}/accordion"

    @property
    def import_var(self):
        """Return the import variable for the accordion component."""
        return ImportVar(tag="Accordion", package_path="", install=False)


class AccordionRoot(AccordionBaseComponent):
    """Groups all parts of the accordion."""

    tag = "Accordion.Root"

    default_value: Var[str]

    value: Var[str]

    on_value_change: EventHandler[passthrough_event_spec(str)]

    # Allows the browser's built-in page search to find and expand the panel contents. Overrides the `keepMounted` prop and uses `hidden="until-found"` to hide the element without removing it from the DOM.
    hidden_until_found: Var[bool]

    multiple: Var[bool]

    # Whether the component should ignore user interaction.
    disabled: Var[bool]

    orientation: Var[LiteralOrientation]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion root component."""
        props["data-slot"] = "accordion"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class AccordionItem(AccordionBaseComponent):
    """Groups an accordion header with the corresponding panel."""

    tag = "Accordion.Item"

    value: Var[str]

    disabled: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion item component."""
        props["data-slot"] = "accordion-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class AccordionHeader(AccordionBaseComponent):
    """A heading that labels the corresponding panel."""

    tag = "Accordion.Header"

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion header component."""
        props["data-slot"] = "accordion-header"
        cls.set_class_name(ClassNames.HEADER, props)
        return super().create(*children, **props)


class AccordionTrigger(AccordionBaseComponent):
    """A button that opens and closes the corresponding panel."""

    tag = "Accordion.Trigger"

    # Whether the component renders a native `<button>` element when replacing it via the `render` prop. Set to `false` if the rendered element is not a button (e.g. `<div>`).
    native_button: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion trigger component."""
        props["data-slot"] = "accordion-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class AccordionPanel(AccordionBaseComponent):
    """A collapsible panel with the accordion item contents."""

    tag = "Accordion.Panel"

    # Allows the browser's built-in page search to find and expand the panel contents. Overrides the `keepMounted` prop and uses `hidden="until-found"` to hide the element without removing it from the DOM.
    hidden_until_found: Var[bool]

    # Whether to keep the element in the DOM while the panel is closed. This prop is ignored when `hiddenUntilFound` is used.
    keep_mounted: Var[bool]

    # The render prop.
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the accordion panel component."""
        props["data-slot"] = "accordion-panel"
        cls.set_class_name(ClassNames.PANEL, props)
        return super().create(*children, **props)


class HighLevelAccordion(AccordionRoot):
    """High level wrapper for the Accordion component."""

    trigger: Var[str] | Component

    content: Var[str] | Component

    item_value: Var[str]

    @classmethod
    def create(
        cls,
        trigger: str | Component | None = None,
        content: str | Component | None = None,
        **props,
    ) -> BaseUIComponent:
        """Create a high level accordion component.

        Args:
            trigger: The content to display in the trigger.
            content: The content to display in the panel.
            **props: Additional properties to apply to the accordion component.

        Returns:
            The accordion component with all necessary subcomponents.
        """
        # Extract content from props if provided there
        if trigger is None and "trigger" in props:
            trigger = props.pop("trigger")
        if content is None and "content" in props:
            content = props.pop("content")

        item_value = props.pop("item_value", "item-1")

        return AccordionRoot.create(
            AccordionItem.create(
                AccordionHeader.create(
                    AccordionTrigger.create(trigger),
                ),
                AccordionPanel.create(content),
                value=item_value,
            ),
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "trigger",
            "content",
            "item_value",
        ]


class Accordion(ComponentNamespace):
    """Namespace for Accordion components."""

    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    header = staticmethod(AccordionHeader.create)
    trigger = staticmethod(AccordionTrigger.create)
    panel = staticmethod(AccordionPanel.create)
    __call__ = staticmethod(HighLevelAccordion.create)


accordion = Accordion()
