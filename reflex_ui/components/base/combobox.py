"""Custom combobox component."""

from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.foreach import foreach
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base.button import button
from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent
from reflex_ui.components.icons.hugeicon import hi
from reflex_ui.components.icons.others import select_arrow
from reflex_ui.utils.twmerge import cn

LiteralComboboxSize = Literal["xs", "sm", "md", "lg", "xl"]
LiteralAlign = Literal["start", "center", "end"]
LiteralSide = Literal["bottom", "inline-end", "inline-start", "left", "right", "top"]
LiteralPosition = Literal["absolute", "fixed"]
LiteralOrientation = Literal["horizontal", "vertical"]


class ClassNames:
    """Class names for combobox components."""

    INPUT = (
        "outline-none bg-transparent text-secondary-12 placeholder:text-secondary-9 text-sm "
        "leading-normal peer disabled:text-secondary-8 disabled:placeholder:text-secondary-8 "
        "w-full data-[disabled]:pointer-events-none font-medium"
    )
    TRIGGER = (
        "flex min-w-48 items-center justify-between gap-3 select-none text-sm [&>span]:line-clamp-1 "
        "cursor-pointer focus:outline-none focus-visible:ring-1 focus-visible:ring-primary-4 group/trigger"
    )
    VALUE = "flex-1 text-left"
    ICON = "flex size-4 text-secondary-10 group-data-[disabled]/trigger:text-current"
    POPUP = (
        "group/popup max-h-[17.25rem] overflow-y-auto origin-(--transform-origin) p-1 border "
        "border-secondary-a4 bg-secondary-1 shadow-large transition-[transform,scale,opacity] "
        "data-[ending-style]:scale-95 data-[starting-style]:scale-95 data-[ending-style]:opacity-0 "
        "data-[starting-style]:opacity-0 outline-none scrollbar-thin scrollbar-thumb-secondary-9 "
        "scrollbar-track-transparent"
    )
    ITEM = (
        "grid min-w-(--anchor-width) grid-cols-[1fr_auto] items-center gap-2 text-sm select-none font-[450] "
        "group-data-[side=none]/popup:min-w-[calc(var(--anchor-width)+1rem)] data-[selected]:text-secondary-12 "
        "text-secondary-11 cursor-pointer placeholder:text-secondary-9 data-[selected]:font-medium outline-none "
        "data-[highlighted]:bg-secondary-3 scroll-m-1"
    )
    ITEM_INDICATOR = "text-current"
    ITEM_TEXT = "text-start"
    GROUP = "p-1"
    GROUP_LABEL = "px-2 py-1.5 text-sm font-semibold"
    SEPARATOR = "-mx-1 my-1 h-[0.5px] bg-secondary-a4"
    ARROW = (
        "data-[side=bottom]:top-[-8px] data-[side=left]:right-[-13px] data-[side=left]:rotate-90 "
        "data-[side=right]:left-[-13px] data-[side=right]:-rotate-90 data-[side=top]:bottom-[-8px] "
        "data-[side=top]:rotate-180"
    )
    POSITIONER = "outline-none"


class ComboboxBaseComponent(BaseUIComponent):
    """Base component for combobox components."""

    library = f"{PACKAGE_NAME}/combobox"

    @property
    def import_var(self):
        """Return the import variable for the combobox component."""
        return ImportVar(tag="Combobox", package_path="", install=False)


class ComboboxRoot(ComboboxBaseComponent):
    """Groups all parts of the combobox. Doesn't render its own HTML element."""

    tag = "Combobox.Root"

    # Identifies the field when a form is submitted.
    name: Var[str]

    # The uncontrolled selected value of the combobox when it's initially rendered.
    # To render a controlled combobox, use the value prop instead.
    default_value: Var[Any]

    # The selected value of the combobox. Use when controlled.
    value: Var[Any]

    # Callback fired when the selected value of the combobox changes.
    on_value_change: EventHandler[passthrough_event_spec(str | dict)]

    # Whether the popup is initially open. To render a controlled popup, use open instead.
    default_open: Var[bool]

    # Whether the popup is currently open.
    open: Var[bool]

    # Event handler called when the popup is opened or closed.
    on_open_change: EventHandler[passthrough_event_spec(bool)]

    # Determines if the combobox enters a modal state when open. Defaults to True.
    modal: Var[bool]

    # Whether multiple items can be selected. Defaults to False.
    multiple: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the user should be unable to choose a different option from the combobox. Defaults to False.
    read_only: Var[bool]

    # Whether the user must choose a value before submitting a form. Defaults to False.
    required: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox root component."""
        props["data-slot"] = "combobox"
        return super().create(*children, **props)


class ComboboxInput(ComboboxBaseComponent):
    """The editable input that filters items."""

    tag = "Combobox.Input"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox input component."""
        props["data-slot"] = "combobox-input"
        cls.set_class_name(ClassNames.INPUT, props)
        return super().create(*children, **props)


class ComboboxClear(ComboboxBaseComponent):
    """A button that clears the input value."""

    tag = "Combobox.Clear"

    # The render prop
    render_: Var[Component]


class ComboboxTrigger(ComboboxBaseComponent):
    """A button that opens the combobox popup."""

    tag = "Combobox.Trigger"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox trigger component."""
        props["data-slot"] = "combobox-trigger"
        cls.set_class_name(ClassNames.TRIGGER, props)
        return super().create(*children, **props)


class ComboboxValue(ComboboxBaseComponent):
    """Text label of the currently selected item."""

    tag = "Combobox.Value"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox value component."""
        props["data-slot"] = "combobox-value"
        cls.set_class_name(ClassNames.VALUE, props)
        return super().create(*children, **props)


class ComboboxBackdrop(ComboboxBaseComponent):
    """An overlay displayed beneath the combo popup."""

    tag = "Combobox.Backdrop"

    # The render prop
    render_: Var[Component]


class ComboboxPortal(ComboboxBaseComponent):
    """A portal element that moves the popup to a different part of the DOM."""

    tag = "Combobox.Portal"

    # A parent element to render the portal element into.
    container: Var[str]


class ComboboxIcon(ComboboxBaseComponent):
    """An icon that indicates the trigger opens a popup."""

    tag = "Combobox.Icon"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox icon component."""
        props["data-slot"] = "combobox-icon"
        cls.set_class_name(ClassNames.ICON, props)
        return super().create(*children, **props)


class ComboboxPositioner(ComboboxBaseComponent):
    """Positions the combobox popup."""

    tag = "Combobox.Positioner"

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against.
    side: Var[LiteralSide]

    # Minimum distance to maintain between the arrow and the edges of the popup.
    arrow_padding: Var[int]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int | list[int]]

    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPosition]

    # Whether the popup tracks any layout shift of its positioning anchor. Defaults to True.
    track_anchor: Var[bool]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[str]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox positioner component."""
        props["data-slot"] = "combobox-positioner"
        props.setdefault("side_offset", 4)
        cls.set_class_name(ClassNames.POSITIONER, props)
        return super().create(*children, **props)


class ComboboxPopup(ComboboxBaseComponent):
    """A container for the combobox items."""

    tag = "Combobox.Popup"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox popup component."""
        props["data-slot"] = "combobox-popup"
        cls.set_class_name(ClassNames.POPUP, props)
        return super().create(*children, **props)


class ComboboxList(ComboboxBaseComponent):
    """A scrollable list container for items."""

    tag = "Combobox.List"

    # The render prop
    render_: Var[Component]


class ComboboxEmpty(ComboboxBaseComponent):
    """Renders its children only when the list is empty."""

    tag = "Combobox.Empty"

    # The render prop
    render_: Var[Component]


class ComboboxItem(ComboboxBaseComponent):
    """An individual option in the combobox menu."""

    tag = "Combobox.Item"

    # Overrides the text label to use on the trigger when this item is selected and when matched during keyboard text navigation.
    label: Var[str]

    # A unique value that identifies this combobox item.
    value: Var[Any]

    # Whether the component should ignore user interaction.
    disabled: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox item component."""
        props["data-slot"] = "combobox-item"
        cls.set_class_name(ClassNames.ITEM, props)
        return super().create(*children, **props)


class ComboboxItemText(ComboboxBaseComponent):
    """A text label of the combobox item."""

    tag = "Combobox.ItemText"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox item text component."""
        props["data-slot"] = "combobox-item-text"
        cls.set_class_name(ClassNames.ITEM_TEXT, props)
        return super().create(*children, **props)


class ComboboxItemIndicator(ComboboxBaseComponent):
    """Indicates whether the combobox item is selected."""

    tag = "Combobox.ItemIndicator"

    # Whether to keep the HTML element in the DOM when the item is not selected. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox item indicator component."""
        props["data-slot"] = "combobox-item-indicator"
        cls.set_class_name(ClassNames.ITEM_INDICATOR, props)
        return super().create(*children, **props)


class ComboboxSeparator(ComboboxBaseComponent):
    """A separator element accessible to screen readers."""

    tag = "Combobox.Separator"

    # The orientation of the separator. Defaults to "horizontal".
    orientation: Var[LiteralOrientation]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox separator component."""
        props["data-slot"] = "combobox-separator"
        cls.set_class_name(ClassNames.SEPARATOR, props)
        return super().create(*children, **props)


class ComboboxGroup(ComboboxBaseComponent):
    """Groups related items with the corresponding label."""

    tag = "Combobox.Group"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox group component."""
        props["data-slot"] = "combobox-group"
        cls.set_class_name(ClassNames.GROUP, props)
        return super().create(*children, **props)


class ComboboxGroupLabel(ComboboxBaseComponent):
    """An accessible label associated with its parent group."""

    tag = "Combobox.GroupLabel"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox group label component."""
        props["data-slot"] = "combobox-group-label"
        cls.set_class_name(ClassNames.GROUP_LABEL, props)
        return super().create(*children, **props)


class ComboboxArrow(ComboboxBaseComponent):
    """Displays an element positioned against the combobox anchor."""

    tag = "Combobox.Arrow"

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox arrow component."""
        props["data-slot"] = "combobox-arrow"
        cls.set_class_name(ClassNames.ARROW, props)
        return super().create(*children, **props)


class ComboboxStatus(ComboboxBaseComponent):
    """Displays a status message announced to screen readers."""

    tag = "Combobox.Status"

    # The render prop
    render_: Var[Component]


class ComboboxChips(ComboboxBaseComponent):
    """Container for chips in multiselectable input."""

    tag = "Combobox.Chips"

    # The render prop
    render_: Var[Component]


class ComboboxChip(ComboboxBaseComponent):
    """An individual chip representing a selected value."""

    tag = "Combobox.Chip"

    # The render prop
    render_: Var[Component]


class ComboboxChipRemove(ComboboxBaseComponent):
    """A button to remove a chip."""

    tag = "Combobox.ChipRemove"

    # The render prop
    render_: Var[Component]


class ComboboxRow(ComboboxBaseComponent):
    """Displays a single row of items in a grid list."""

    tag = "Combobox.Row"

    # The render prop
    render_: Var[Component]


class ComboboxCollection(ComboboxBaseComponent):
    """Renders filtered list items (function child)."""

    tag = "Combobox.Collection"


class HighLevelCombobox(ComboboxRoot):
    """High level wrapper for the Combobox component."""

    # The list of items to display in the combobox dropdown
    items: Var[list[str]]

    # The placeholder text to display when no item is selected
    placeholder: Var[str]

    # The size of the combobox component. Defaults to "md".
    size: Var[LiteralComboboxSize]

    # Props for different component parts
    _trigger_props = {"placeholder", "size"}
    _items_props = {"items"}
    _positioner_props = {
        "align",
        "align_offset",
        "side",
        "arrow_padding",
        "collision_padding",
        "sticky",
        "position_method",
        "track_anchor",
        "side_offset",
        "collision_avoidance",
    }
    _portal_props = {"container"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a combobox component."""
        # Extract props for different parts
        trigger_props = {k: props.pop(k) for k in cls._trigger_props & props.keys()}
        items_props = {k: props.pop(k) for k in cls._items_props & props.keys()}
        positioner_props = {
            k: props.pop(k) for k in cls._positioner_props & props.keys()
        }
        portal_props = {k: props.pop(k) for k in cls._portal_props & props.keys()}

        # Get extracted values with defaults
        size = trigger_props.get("size", "md")
        items = items_props.get("items", [])

        # Create the items children
        if isinstance(items, Var):
            items_children = foreach(
                items,
                lambda item: ComboboxItem.create(
                    render_=button(
                        ComboboxItemText.create(item),
                        ComboboxItemIndicator.create(
                            hi(
                                "Tick02Icon",
                                class_name="size-4",
                            ),
                        ),
                        variant="ghost",
                        size=size,
                        type="button",
                        class_name=ClassNames.ITEM,
                        disabled=props.get("disabled", False),
                    ),
                    value=item,
                    key=item,
                ),
            )
        else:
            items_children = [
                ComboboxItem.create(
                    render_=button(
                        ComboboxItemText.create(item),
                        ComboboxItemIndicator.create(
                            hi(
                                "Tick02Icon",
                                class_name="size-4",
                            ),
                        ),
                        variant="ghost",
                        size=size,
                        type="button",
                        class_name=ClassNames.ITEM,
                    ),
                    value=item,
                    key=item,
                )
                for item in items
            ]

        return ComboboxRoot.create(
            ComboboxTrigger.create(
                render_=button(
                    ComboboxValue.create(),
                    select_arrow(class_name="size-4 text-secondary-9"),
                    variant="outline",
                    size=size,
                    type="button",
                    class_name=ClassNames.TRIGGER,
                    disabled=props.get("disabled", False),
                ),
            ),
            ComboboxPortal.create(
                ComboboxPositioner.create(
                    ComboboxPopup.create(
                        ComboboxList.create(items_children),
                        class_name=cn(
                            ClassNames.POPUP,
                            f"rounded-[calc(var(--radius-ui-{size})+0.25rem)]",
                        ),
                    ),
                    **positioner_props,
                ),
                **portal_props,
            ),
            *children,
            **props,
        )


class Combobox(ComponentNamespace):
    """Namespace for Combobox components."""

    root = staticmethod(ComboboxRoot.create)
    trigger = staticmethod(ComboboxTrigger.create)
    value = staticmethod(ComboboxValue.create)
    icon = staticmethod(ComboboxIcon.create)
    backdrop = staticmethod(ComboboxBackdrop.create)
    portal = staticmethod(ComboboxPortal.create)
    positioner = staticmethod(ComboboxPositioner.create)
    popup = staticmethod(ComboboxPopup.create)
    empty = staticmethod(ComboboxEmpty.create)
    list = staticmethod(ComboboxList.create)
    input = staticmethod(ComboboxInput.create)
    clear = staticmethod(ComboboxClear.create)
    item = staticmethod(ComboboxItem.create)
    item_text = staticmethod(ComboboxItemText.create)
    item_indicator = staticmethod(ComboboxItemIndicator.create)
    arrow = staticmethod(ComboboxArrow.create)
    status = staticmethod(ComboboxStatus.create)
    group = staticmethod(ComboboxGroup.create)
    group_label = staticmethod(ComboboxGroupLabel.create)
    separator = staticmethod(ComboboxSeparator.create)
    chips = staticmethod(ComboboxChips.create)
    chip = staticmethod(ComboboxChip.create)
    chip_remove = staticmethod(ComboboxChipRemove.create)
    row = staticmethod(ComboboxRow.create)
    collection = staticmethod(ComboboxCollection.create)
    class_names = ClassNames
    __call__ = staticmethod(HighLevelCombobox.create)


combobox = Combobox()
