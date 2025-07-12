from typing import Literal

import reflex as rx
from reflex.event import EventType

from shared_components.ui.components.icons import get_icon, hi, spinner

SelectVariant = Literal["primary", "secondary", "outline", "transparent"]
SelectSize = Literal["xs", "sm", "md", "lg"]
SelectItemVariant = Literal["selectable", "actions"]

DEFAULT_CLASS_NAME = "inline-flex transition-bg shrink-0 items-center w-auto cursor-pointer disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 outline-none focus:outline-none"

VARIANT_STYLES: dict[SelectVariant, str] = {
    "primary": "text-slate-9 font-medium border border-slate-5 bg-slate-1 hover:bg-slate-3 radix-state-open:bg-slate-3",
    "secondary": "text-slate-11 font-medium bg-slate-4 hover:bg-slate-6 radix-state-open:bg-slate-6",
    "transparent": "bg-transparent text-slate-9 font-medium hover:bg-slate-3 radix-state-open:bg-slate-3",
    "outline": "text-slate-9 font-medium border border-slate-5 hover:bg-slate-3 radix-state-open:bg-slate-3 bg-slate-1",
}

SIZE_STYLES: dict[SelectSize, str] = {
    "xs": "text-sm px-1.5 h-7 rounded-md gap-1.5",
    "sm": "text-sm px-2 h-8 rounded-lg gap-2",
    "md": "text-sm px-2.5 min-h-9 max-h-9 rounded-[10px] gap-2.5",
    "lg": "text-sm px-3 h-10 rounded-xl gap-3",
}


def select_item(
    content: tuple[str | rx.Component, EventType[()]],
    is_selected: bool | rx.Var[bool] = False,
    size: SelectSize = "sm",
    variant: SelectItemVariant = "actions",
    loading: bool = False,
    **props,
) -> rx.Component:
    """A select item component.

    Args:
        content: A tuple containing the item text and its on_click event handler(s).
        is_selected: Whether the item is currently selected. Defaults to False.
        size: The size of the select item. Defaults to "sm".
        variant : The variant of the select item. Defaults to "actions".
        gradient_class_name (str): The gradient class name to apply to the select item. Defaults to "".
        icon: An optional icon to display in the select item. Defaults to None.
        tier: The tier of the select item. Defaults to "".
        loading: Whether the select item is in a loading state. Defaults to False.
        **props: Additional properties to pass to the underlying button component.

    Returns:
        rx.Component: A styled select item component.

    """
    text, on_click_event = content
    base_classes = [
        "inline-flex transition-bg shrink-0 items-center w-full cursor-pointer disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:!text-slate-8 outline-none focus:outline-none",
        "bg-transparent text-slate-9 font-medium hover:bg-slate-3 font-sans",
        SIZE_STYLES[size],
    ]

    common_props = {
        "class_name": " ".join(filter(None, base_classes)),
        "type": "button",
        "on_click": on_click_event,
        **props,
    }

    text_component = rx.box(
        text,
        class_name="truncate" + rx.cond(is_selected, " !text-slate-12", "").to(str),
    )

    tick_icon = rx.cond(
        loading,
        rx.box(
            spinner(
                class_name="!text-slate-9 [&>svg]:animate-spin size-4",
            ),
            display=rx.cond(is_selected, "flex", "none"),
        ),
        hi(
            tag="tick-02",
            class_name="!text-slate-12 shrink-0",
            display=rx.cond(is_selected, "flex", "none"),
        ),
    )

    # Selectable variant
    if variant == "selectable":
        return rx.popover.close(
            rx.el.button(
                text_component,
                rx.box(class_name="flex-1"),
                tick_icon,
                **common_props,
            ),
            class_name="w-full outline-none focus:outline-none",
        )

    # Actions variant
    if variant == "actions":
        return rx.el.button(text_component, **common_props)

    msg = f"Invalid variant '{variant}'."
    raise ValueError(msg)


def select(
    content: rx.Component,
    variant: SelectVariant = "primary",
    size: SelectSize = "sm",
    placeholder: str | rx.Var | rx.Component = "Select an option",
    align: Literal["start", "center", "end"] = "start",
    class_name: str = "",
    icon: rx.Component | None = None,
    show_arrow: bool = True,
    unstyled: bool = False,
    tier: str = "",
    disabled: bool | rx.Var[bool] = False,
    **props,
) -> rx.Component:
    """A dropdown select component.

    Args:
        content: The content to display in the select dropdown.
        items: List of components to be displayed as options in the select dropdown.
        variant: The visual style of the select. Defaults to "primary".
        size: The size of the select component. Defaults to "md".
        placeholder: Text to display when no option is selected. Defaults to "Select an option".
        align: The alignment of the dropdown content. Defaults to "start".
        class_name: Additional CSS classes to apply to the select. Defaults to "".
        selected_condition: Condition to determine if an item is selected. Defaults to False.
        icon: An optional icon to display in the select trigger. Defaults to None.
        show_arrow: Whether to show the arrow icon. Defaults to True.
        unstyled: Whether to remove the default styles. Defaults to False.
        tier: The tier of the select. Defaults to "".
        disabled: Whether the select is disabled. Defaults to False.
        **props: Additional properties to pass to the underlying Popover component.

    Returns:
        rx.Component: A customizable select component with a dropdown list of options.

    """
    classes = (
        [
            DEFAULT_CLASS_NAME,
            VARIANT_STYLES[variant],
            SIZE_STYLES[size],
            class_name,
        ]
        if not unstyled
        else [class_name]
    )

    return rx.popover.root(
        rx.popover.trigger(
            rx.el.button(
                icon if icon else rx.fragment(),
                (
                    rx.cond(
                        placeholder,
                        rx.box(placeholder),
                    )
                    if not isinstance(placeholder, rx.Component)
                    else placeholder
                ),
                (
                    (
                        get_icon(icon="select-arrows", class_name="text-slate-9")
                        if show_arrow
                        else rx.fragment()
                    ),
                ),
                class_name=" ".join(filter(None, classes)),
                disabled=disabled,
                type="button",
            ),
        ),
        rx.popover.content(
            content,
            side="bottom",
            align=align,
            side_offset=4,
            align_offset=-4 if align in ["start", "end"] else 0,
            avoid_collisions=True,
            class_name="items-center bg-transparent !shadow-none !p-0 border-none w-auto overflow-visible font-sans pointer-events-auto",
        ),
        **props,
    )