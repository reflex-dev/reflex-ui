from typing import Literal

import reflex as rx

from shared_components.booking_form.utils.twmerge import cn

DropdownVariant = Literal["selectable", "actions"]
DEFAULT_CLASS_NAME = "flex p-1 rounded-xl items-center justify-start flex-col shadow-large bg-slate-1 border border-slate-5"

VARIANT_STYLES: dict[DropdownVariant, str] = {
    "selectable": "w-[10.5rem]",
    "actions": "w-[9rem]",
}


def dropdown(
    components: list[rx.Component],
    variant: DropdownVariant = "actions",
    class_name: str = "",
) -> rx.Component:
    """A dropdown component.

    Args:
        components (List[rx.Component]): List of components to be displayed in the dropdown.
        variant (DropdownVariant, optional): The visual style of the dropdown. Defaults to "actions".
        class_name (str, optional): Additional CSS classes to apply to the dropdown. Defaults to "".
        size (DropdownSize, optional): The size of the dropdown. Defaults to "sm".

    Returns:
        rx.Component: A customizable dropdown component containing the provided components.

    """
    classes = cn(DEFAULT_CLASS_NAME + " " + VARIANT_STYLES[variant], class_name)

    return rx.box(*components, class_name=classes)
