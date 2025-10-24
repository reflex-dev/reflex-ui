"""Custom combobox component."""

from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventHandler, passthrough_event_spec
from reflex.utils.imports import ImportVar
from reflex.vars.base import Var

from reflex_ui.components.base_ui import PACKAGE_NAME, BaseUIComponent
from reflex_ui.components.icons.hugeicon import hi

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

    # A ref to imperative actions. When specified, the combobox will not be unmounted when closed.
    actions_ref: Var[str]

    # Whether to automatically highlight the first item while filtering. Defaults to False.
    auto_highlight: Var[bool]

    # The uncontrolled input value when initially rendered. To render a controlled input, use the inputValue prop instead.
    default_input_value: Var[str]

    # Filter function used to match items vs input query.
    filter: Var[Any]

    # Whether list items are presented in a grid layout. Defaults to False.
    grid: Var[bool]

    # The input value of the combobox. Use when controlled.
    input_value: Var[str]

    # Custom comparison logic used to determine if a combobox item value matches the current selected value.
    is_item_equal_to_value: Var[Any]

    # When the item values are objects, this function converts the object value to a string representation for display in the input.
    item_to_string_label: Var[Any]

    # When the item values are objects, this function converts the object value to a string representation for form submission.
    item_to_string_value: Var[Any]

    # The items to be displayed in the list. Can be either a flat array of items or an array of groups with items.
    items: Var[Any]

    # The maximum number of items to display in the list. Defaults to -1 (unlimited).
    limit: Var[int]

    # The locale to use for string comparison. Defaults to the user's runtime locale.
    locale: Var[str]

    # Determines if the combobox enters a modal state when open. Defaults to False.
    modal: Var[bool]

    # Whether multiple items can be selected. Defaults to False.
    multiple: Var[bool]

    # Callback fired when the input value of the combobox changes.
    on_input_value_change: EventHandler[passthrough_event_spec(str)]

    # Callback fired when the user navigates the list and highlights an item.
    on_item_highlighted: EventHandler[passthrough_event_spec(dict)]

    # Event handler called after any animations complete when the popup is opened or closed.
    on_open_change_complete: EventHandler[passthrough_event_spec(bool)]

    # Whether the popup opens when clicking the input. Defaults to True.
    open_on_input_click: Var[bool]

    # Whether the items are being externally virtualized. Defaults to False.
    virtualized: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the user should be unable to choose a different option from the combobox. Defaults to False.
    read_only: Var[bool]

    # Whether the user must choose a value before submitting a form. Defaults to False.
    required: Var[bool]

    # A ref to the hidden input element.
    input_ref: Var[str]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox root component."""
        props["data-slot"] = "combobox"
        return super().create(*children, **props)


class ComboboxInput(ComboboxBaseComponent):
    """The editable input that filters items."""

    tag = "Combobox.Input"

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

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

    # Whether the component renders a native <button> element when replacing it via the render prop. Defaults to True.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
    disabled: Var[bool]

    # Whether the component should remain mounted in the DOM when not visible. Defaults to False.
    keep_mounted: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox clear component."""
        props["data-slot"] = "combobox-clear"
        return super().create(*children, **props)


class ComboboxTrigger(ComboboxBaseComponent):
    """A button that opens the combobox popup."""

    tag = "Combobox.Trigger"

    # Whether the component renders a native <button> element when replacing it via the render prop. Defaults to True.
    native_button: Var[bool]

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

    # Whether to keep the portal mounted in the DOM while the popup is hidden. Defaults to False.
    keep_mounted: Var[bool]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox portal component."""
        props["data-slot"] = "combobox-portal"
        return super().create(*children, **props)


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

    # Determines how to handle collisions when positioning the popup.
    collision_avoidance: Var[str]

    # How to align the popup relative to the specified side. Defaults to "center".
    align: Var[LiteralAlign]

    # Additional offset along the alignment axis in pixels. Defaults to 0.
    align_offset: Var[int]

    # Which side of the anchor element to align the popup against. Defaults to "bottom".
    side: Var[LiteralSide]

    # Distance between the anchor and the popup in pixels. Defaults to 0.
    side_offset: Var[int]

    # Minimum distance to maintain between the arrow and the edges of the popup. Defaults to 5.
    arrow_padding: Var[int]

    # An element to position the popup against. By default, the popup will be positioned against the trigger.
    anchor: Var[str]

    # An element or a rectangle that delimits the area that the popup is confined to. Defaults to "clipping-ancestors".
    collision_boundary: Var[str]

    # Additional space to maintain from the edge of the collision boundary. Defaults to 5.
    collision_padding: Var[int | list[int]]

    # Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. Defaults to False.
    sticky: Var[bool]

    # Determines which CSS position property to use. Defaults to "absolute".
    position_method: Var[LiteralPosition]

    # Whether the popup tracks any layout shift of its positioning anchor. Defaults to True.
    track_anchor: Var[bool]

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

    # Determines the element to focus when the popup is opened.
    initial_focus: Var[Any]

    # Determines the element to focus when the popup is closed.
    final_focus: Var[Any]

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


class ComboboxListWithFunctionChild(ComboboxBaseComponent):
    """Special list component that renders items using function child pattern for filtering.

    This component wraps Combobox.List and automatically generates the function child
    that Base UI needs to properly filter items.
    """

    tag = "Combobox.List"

    def _get_custom_code(self) -> str | None:
        """Generate custom JSX for function child pattern."""
        # Return the opening of the function child
        return "{(item_rx_state_) => ("

    def render(self):
        """Render with function child wrapper."""
        rendered = super().render()

        # Wrap children in function child pattern
        if self.children:
            # Add function wrapper opening
            rendered["function_child_start"] = "{(item_rx_state_) => ("
            rendered["function_child_end"] = ")}"

        return rendered


class ComboboxEmpty(ComboboxBaseComponent):
    """Renders its children only when the list is empty."""

    tag = "Combobox.Empty"

    # The render prop
    render_: Var[Component]


class ComboboxItem(ComboboxBaseComponent):
    """An individual option in the combobox menu."""

    tag = "Combobox.Item"

    # A unique value that identifies this combobox item.
    value: Var[Any]

    # The index of the item in the list. Improves performance when specified.
    index: Var[int]

    # Whether the component renders a native <button> element when replacing it via the render prop. Defaults to False.
    native_button: Var[bool]

    # Whether the component should ignore user interaction. Defaults to False.
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

    # Items to be rendered within this group. When provided, child Collection components will use these items.
    items: Var[Any]

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

    # Whether the component renders a native <button> element when replacing it via the render prop. Defaults to True.
    native_button: Var[bool]

    # The render prop
    render_: Var[Component]

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create the combobox chip remove component."""
        props["data-slot"] = "combobox-chip-remove"
        return super().create(*children, **props)


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

    # The label text to display above the input
    label: Var[str]

    # The message to display when no items are found
    empty_message: Var[str]

    # The ID for the input element
    input_id: Var[str]

    # Props for different component parts
    _high_level_props = {"placeholder", "label", "empty_message", "input_id"}
    _items_props = {"items"}
    _positioner_props = {
        "collision_avoidance",
        "align",
        "align_offset",
        "side",
        "side_offset",
        "arrow_padding",
        "anchor",
        "collision_boundary",
        "collision_padding",
        "sticky",
        "position_method",
        "track_anchor",
    }
    _portal_props = {"container", "keep_mounted"}

    @classmethod
    def create(cls, *children, **props) -> BaseUIComponent:
        """Create a combobox component."""
        from reflex import box

        from reflex_ui.utils.iterable_list import function_child

        # Extract props for different parts
        high_level_props = {
            k: props.pop(k) for k in cls._high_level_props & props.keys()
        }
        items_props = {k: props.pop(k) for k in cls._items_props & props.keys()}
        positioner_props = {
            k: props.pop(k) for k in cls._positioner_props & props.keys()
        }
        portal_props = {k: props.pop(k) for k in cls._portal_props & props.keys()}

        # Get extracted values with defaults
        items = items_props.get("items", [])
        placeholder = high_level_props.get("placeholder", "e.g. Apple")
        label = high_level_props.get("label", "Choose a fruit")
        empty_message = high_level_props.get("empty_message", "No fruits found.")
        input_id = high_level_props.get("input_id", "combobox-input")

        # Build the item renderer function
        def render_item(item):
            return ComboboxItem.create(
                ComboboxItemIndicator.create(
                    class_name="col-start-1",
                ),
                box(
                    item,
                    class_name="col-start-2",
                ),
                value=item,
                key=item,
                class_name="grid cursor-default grid-cols-[0.75rem_1fr] items-center gap-2 py-2 pr-8 pl-4 text-base leading-4 outline-none select-none data-[highlighted]:relative data-[highlighted]:z-0 data-[highlighted]:text-gray-50 data-[highlighted]:before:absolute data-[highlighted]:before:inset-x-2 data-[highlighted]:before:inset-y-0 data-[highlighted]:before:z-[-1] data-[highlighted]:before:rounded-sm data-[highlighted]:before:bg-gray-900",
            )

        # Create items list and combobox list
        # Use function_child to create a function that Base UI calls for each filtered item
        list_content = function_child(render_item)
        combobox_list = ComboboxList.create(list_content)

        return ComboboxRoot.create(
            box(
                box(
                    label,
                    html_for=input_id,
                    element="label",
                ),
                ComboboxInput.create(
                    placeholder=placeholder,
                    id=input_id,
                    class_name="h-10 w-64 rounded-md font-normal border border-gray-200 pl-3.5 text-base text-gray-900 bg-[canvas] focus:outline-2 focus:-outline-offset-1 focus:outline-blue-800",
                ),
                box(
                    ComboboxClear.create(
                        hi("Cancel01Icon", class_name="size-4"),
                        class_name="flex h-10 w-6 items-center justify-center rounded bg-transparent p-0",
                        aria_label="Clear selection",
                    ),
                    ComboboxTrigger.create(
                        hi("ArrowDown01Icon", class_name="size-4"),
                        class_name="flex h-10 w-6 items-center justify-center rounded bg-transparent p-0",
                        aria_label="Open popup",
                    ),
                    class_name="absolute right-2 bottom-0 flex h-10 items-center justify-center text-gray-600",
                ),
                class_name="relative flex flex-col gap-1 text-sm leading-5 font-medium text-gray-900",
            ),
            ComboboxPortal.create(
                ComboboxPositioner.create(
                    ComboboxPopup.create(
                        ComboboxEmpty.create(
                            empty_message,
                            class_name="px-4 py-2 text-[0.925rem] leading-4 text-gray-600 empty:m-0 empty:p-0",
                        ),
                        combobox_list,
                        class_name="w-[var(--anchor-width)] max-h-[min(var(--available-height),23rem)] max-w-[var(--available-width)] origin-[var(--transform-origin)] overflow-y-auto scroll-pt-2 scroll-pb-2 overscroll-contain rounded-md bg-[canvas] py-2 text-gray-900 shadow-lg shadow-gray-200 outline-1 outline-gray-200 transition-[transform,scale,opacity] data-[ending-style]:scale-95 data-[ending-style]:opacity-0 data-[starting-style]:scale-95 data-[starting-style]:opacity-0 dark:shadow-none dark:-outline-offset-1 dark:outline-gray-300",
                    ),
                    side_offset=4,
                    class_name="outline-none",
                ),
                **portal_props,
            ),
            items=items,
            **props,
        )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "placeholder",
            "label",
            "empty_message",
            "input_id",
        ]


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
