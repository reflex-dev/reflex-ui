"""Checkbox component from base-ui components."""

from __future__ import annotations

from reflex.components.component import Component, ComponentNamespace
from reflex.components.el import Label
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent
from reflex_ui.components.icons.hugeicon import hi
from reflex_ui.utils.twmerge import cn


class ClassNames:
    """Class names for the checkbox component."""

    ROOT = "flex size-4 items-center justify-center rounded-[4px] data-[checked]:bg-primary-9 data-[unchecked]:border data-[unchecked]:border-secondary-8 data-[disabled]:cursor-not-allowed data-[disabled]:border data-[disabled]:border-secondary-4 data-[disabled]:bg-secondary-3 hover:bg-secondary-3 transition-colors cursor-default"
    INDICATOR = (
        "flex text-white data-[unchecked]:hidden data-[disabled]:text-secondary-8"
    )
    LABEL = "text-sm text-secondary-12 font-medium flex items-center gap-2"
    CONTAINER = "flex flex-row items-center gap-2"


class CheckboxBaseComponent(BaseUIComponent):
    """Base component for checkbox components."""

    library = f"{PACKAGE_NAME}/checkbox"

    @property
    def import_var(self):
        """Return the import variable for the checkbox component."""
        return ImportVar(tag="Checkbox", package_path="", install=False)


class CheckboxRoot(CheckboxBaseComponent):
    """The root checkbox component."""

    tag = "Checkbox.Root"

    # Whether the checkbox is initially ticked. To render a controlled checkbox, use the checked prop instead. Defaults to False.
    default_checked: Var[bool]

    # Whether the checkbox is currently ticked. To render an uncontrolled checkbox, use the default_checked prop instead.
    checked: Var[bool]

    # Event handler called when the checkbox is ticked or unticked.
    on_checked_change: EventHandler[passthrough_event_spec(bool, dict)]

    # Whether the checkbox is in a mixed state: neither ticked, nor unticked. Defaults to False.
    indeterminate: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the checkbox is required. Defaults to False.
    required: Var[bool]

    # Identifies the field when a form is submitted.
    name: Var[str]

    # The value of the selected checkbox.
    value: Var[str]

    # Whether the component renders a native <button> element when replacing it via the render prop. Set to false if the rendered element is not a button (e.g. <div>). Defaults to True.
    native_button: Var[bool]

    # Whether the checkbox controls a group of child checkboxes. Must be used in a Checkbox Group. Defaults to False.
    parent: Var[bool]

    # Whether the user should be unable to tick or untick the checkbox. Defaults to False.
    read_only: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the checkbox root component."""
        props["data-slot"] = "checkbox"
        cls.set_class_name(ClassNames.ROOT, props)
        return super().create(*children, **props)


class CheckboxIndicator(CheckboxBaseComponent):
    """The indicator that shows whether the checkbox is checked."""

    tag = "Checkbox.Indicator"

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the checkbox indicator component."""
        if len(children) == 0:
            children = (hi("Tick02Icon", size=14),)
        props["data-slot"] = "checkbox-indicator"
        cls.set_class_name(ClassNames.INDICATOR, props)
        return super().create(*children, **props)


class HighLevelCheckbox(CheckboxRoot):
    """High level wrapper for the Checkbox component."""

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create a high level checkbox component.

        Args:
            *children: The content of the checkbox.
            **props: Additional properties to apply to the checkbox component.

        Returns:
            The checkbox component and its indicator.
        """
        class_name = props.pop("class_name", "")
        if label := props.pop("label", None):
            return Label.create(
                CheckboxRoot.create(
                    CheckboxIndicator.create(),
                    *children,
                    **props,
                ),
                label,
                class_name=cn(ClassNames.LABEL, class_name),
            )
        return CheckboxRoot.create(
            CheckboxIndicator.create(),
            *children,
            **props,
            class_name=class_name,
        )


class CheckboxNamespace(ComponentNamespace):
    """Namespace for Checkbox components."""

    root = staticmethod(CheckboxRoot.create)
    indicator = staticmethod(CheckboxIndicator.create)
    high_level = staticmethod(HighLevelCheckbox.create)
    __call__ = staticmethod(HighLevelCheckbox.create)


checkbox = CheckboxNamespace()
