import reflex as rx
from reflex.components.el.elements.forms import HTMLInputTypeAttribute
from reflex.vars.base import get_unique_variable_name

from shared_components.booking_form.ui.components.icons import get_icon
from shared_components.booking_form.utils.twmerge import cn


def user_input(
    placeholder: str = "",
    name: str = "",
    input_id: str = "",
    input_cn: str = "",
    type_: HTMLInputTypeAttribute = "text",
    class_name: str = "",
    **props,
) -> rx.Component:
    """Create a basic input component.

    Args:
        placeholder: Placeholder text for the input.
        name: Name of the input.
        input_id: ID of the input.
        input_cn: Additional Tailwind CSS class for input.
        type_: Type of the input.
        class_name: Additional CSS classes to apply to the input component.
        **props: Additional props to pass to the input element.

    Returns:
        rx.Component: A basic input component.

    """
    if not input_id:
        input_id = get_unique_variable_name()

    return rx.box(
        rx.el.input(
            placeholder=placeholder,
            name=name,
            id=input_id,
            class_name=cn(
                "box-border flex flex-row flex-1 gap-2 border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--color-violet-6)] px-6 pr-8 border rounded-[0.625rem] h-[2.25rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 peer pl-2.5 disabled:cursor-not-allowed disabled:border disabled:border-slate-5 disabled:!bg-slate-3 disabled:text-slate-8 disabled:placeholder:text-slate-8",
                input_cn,
            ),
            type=type_,
            custom_attrs={
                "autoComplete": "off",
                "autoCorrect": "off",
                "data-vaul-no-drag": "",
            },
            **props,
        ),
        rx.el.button(
            get_icon("cancel-circle"),
            class_name="right-0 z-10 absolute inset-y-0 flex items-center opacity-100 peer-placeholder-shown:opacity-0 pr-2.5 text-slate-9 hover:text-slate-12 transition-bg peer-placeholder-shown:pointer-events-none peer-disabled:pointer-events-none peer-disabled:hidden",
            content_editable=False,
            on_click=rx.set_value(input_id, ""),
            on_mouse_down=rx.prevent_default,
            type="button",
            tab_index=-1,
        ),
        class_name=cn("relative flex", class_name),
    )
