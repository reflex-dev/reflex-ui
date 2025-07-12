"""Custom accordion component."""

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, no_args_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars import Var
from collections.abc import Sequence
from typing import Any, ClassVar, Literal

from .base.base_ui import PACKAGE_NAME, BaseUIComponent
from calendar import c

LiteralAccordionOrientation = Literal["vertical", "horizontal"]

class AccordionBaseComponent(BaseUIComponent):
    """Base component for avatar components."""

    library = f"{PACKAGE_NAME}/accordion"

    @property
    def import_var(self):
        return ImportVar(tag="Accordion", package_path="", install=False)


def on_value_change(value: Var[str | list[str]]) -> tuple[Var[str | list[str]]]:
    """Handle the on_value_change event.

    Args:
        value: The value of the event.

    Returns:
        The value of the event.
    """
    return (value,)

class AccordionRoot(AccordionBaseComponent):
    """"""

    tag = "Accordion.Root"

    # The value of the item to expand.
    value: Var[str | Sequence[str]]

    # The default value of the item to expand.
    default_value: Var[str | Sequence[str]]

    # Fired when the opened the accordions changes.
    on_value_change: EventHandler[on_value_change]

    # Allows the browser’s built-in page search to find and expand the panel contents.
    hidden_until_found: Var[bool] = Var.create(False)

    # Whether multiple items can be open at the same time.
    open_multiple: Var[bool] = Var.create(True)

    # Whether the component should ignore user interaction.
    disabled: Var[bool] = Var.create(False)

    # Whether to loop keyboard focus back to the first item when the end of the list is reached while using the arrow keys.
    loop: Var[bool] = Var.create(True)

    # The visual orientation of the accordion. Controls whether roving focus uses left/right or up/down arrow keys.
    orientation: Var[LiteralAccordionOrientation] = Var.create("vertical")

    # Whether to keep the element in the DOM while the panel is closed. This prop is ignored when hiddenUntilFound is used.
    keep_mounted: Var[bool] = Var.create(False)

    # The component to render
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the accordion root component."""
        return super().create(*children, **props)


class AccordionItem(AccordionBaseComponent):
    """An accordion item component."""

    tag = "Accordion.Item"

    # A unique identifier for the item.
    value: Var[str]

    # When true, prevents the user from interacting with the item.
    disabled: Var[bool] = Var.create(False)

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the accordion item component."""
        return super().create(*children, **props)


class AccordionTrigger(AccordionBaseComponent):
    """The accordion trigger component that toggles the item."""

    tag = "Accordion.Trigger"

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the accordion trigger component."""
        return super().create(*children, **props)


class AccordionContent(AccordionBaseComponent):
    """The accordion content component that contains the collapsible content."""

    tag = "Accordion.Content"

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the accordion content component."""
        return super().create(*children, **props)


# Create the namespace for easy access
class Accordion(ComponentNamespace):
    """Accordion component namespace."""

    root = staticmethod(AccordionRoot.create)
    item = staticmethod(AccordionItem.create)
    trigger = staticmethod(AccordionTrigger.create)
    content = staticmethod(AccordionContent.create)


# For backward compatibility / alternative access
accordion = Accordion()
