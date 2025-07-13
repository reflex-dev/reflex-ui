import reflex as rx

from shared_components.booking_form.ui.components.button import button
from shared_components.booking_form.ui.components.dropdown import dropdown
from shared_components.booking_form.ui.components.select import select, select_item
from shared_components.booking_form.ui.components.user_input import user_input
from shared_components.booking_form.states.booking_state import BookingFormState, show_thank_you_dialog

def thank_you_modal() -> rx.Component:
    """Thank you modal for small companies."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.box(
                rx.box(
                    rx.text(
                        "Thank You for Your Interest!",
                        class_name="text-2xl font-semibold text-slate-12 font-sans",
                    ),
                    rx.dialog.close(
                        button(
                            rx.icon("x", class_name="!text-slate-9"),
                            variant="transparent",
                            size="icon-sm",
                            type="button",
                            class_name="focus:outline-none",
                            on_click=show_thank_you_dialog.set_value(False),
                        ),
                    ),
                    class_name="flex flex-row items-center gap-2 justify-between w-full",
                ),
                rx.text(
                    "We've received your submission and our team will get back to you soon. We appreciate your interest in Reflex!",
                    class_name="text-slate-9 font-medium text-sm",
                ),
                class_name="flex flex-col w-full gap-y-4",
            ),
            class_name="w-full",
            on_interact_outside=show_thank_you_dialog.set_value(False),
            on_escape_key_down=show_thank_you_dialog.set_value(False),
        ),
        open=show_thank_you_dialog.value,
    )

def form_field(label: str, field_component: rx.Component) -> rx.Component:
    """Reusable form field component with consistent styling."""
    return rx.el.div(
        rx.el.label(
            label,
            class_name="text-slate-12 text-base font-semibold",
        ),
        field_component,
        class_name="flex flex-col gap-2 w-full",
    )

def select_employees() -> rx.Component:
    return select(
        placeholder=BookingFormState.selected_num_employees,
        show_arrow=True,
        content=dropdown(
            components=[
                select_item(
                    content=(
                        rx.box(
                            rx.text(option),
                            class_name="flex flex-row items-center gap-2.5 w-full text-start",
                        ),
                        [
                            BookingFormState.set_selected_num_employees(option),
                        ],
                    ),
                    is_selected=option == BookingFormState.selected_num_employees,
                    size="xs",
                    variant="selectable",
                )
                for option in ["1", "2-5", "6-10", "11-50", "51-100", "101-500", "500+"]
            ],
            variant="selectable",
            class_name="w-full min-w-[11rem] overflow-hidden",
        ),
        size="xs",
        variant="outline",
        align="start",
        class_name="!outline-none justify-between flex-1 !px-2.5 !rounded-[0.625rem] !h-[2.25rem] [&>div]:h-[2.25rem] [&>div]:flex [&>div]:items-center [&>div]:justify-center",
    )

def select_referral_source() -> rx.Component:
    return select(
        placeholder=BookingFormState.selected_referral_source,
        show_arrow=True,
        content=dropdown(
            components=[
                select_item(
                    content=(
                        rx.box(
                            rx.text(option),
                            class_name="flex flex-row items-center gap-2.5 w-full text-start",
                        ),
                        [
                            BookingFormState.set_selected_referral_source(option),
                        ],
                    ),
                    is_selected=option
                    == BookingFormState.selected_referral_source,
                    size="xs",
                    variant="selectable",
                )
                for option in [
                    "Google Search",
                    "Social Media",
                    "Word of Mouth",
                    "Blog",
                    "Conference",
                    "Other",
                ]
            ],
            variant="selectable",
            class_name="w-full min-w-[11rem] overflow-hidden",
        ),
        size="xs",
        variant="outline",
        align="start",
        class_name="!outline-none justify-between flex-1 !px-2.5 !rounded-[0.625rem] !h-[2.25rem] [&>div]:h-[2.25rem] [&>div]:flex [&>div]:items-center [&>div]:justify-center",
    )

def demo_request_form() -> rx.Component:
    """Reusable form component with all the demo request fields."""
    return rx.el.div(
        # Personal Information
        rx.el.div(
            form_field(
                "First name *",
                user_input(
                    placeholder="John",
                    required=True,
                    type_="text",
                    name="first_name",
                ),
            ),
            form_field(
                "Last name *",
                user_input(
                    placeholder="Smith",
                    required=True,
                    type_="text",
                    name="last_name",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-2 w-full",
        ),
        rx.el.div(
            form_field(
                "Business email *",
                user_input(
                    placeholder="john@reflex.dev",
                    required=True,
                    type_="email",
                    name="company_email",
                ),
            ),
            rx.text(
                rx.cond(
                    BookingFormState.show_email_error,
                    "Use your company email to book a demo.",
                    "",
                ),
                class_name="text-sm text-red-10 font-medium",
            ),
            class_name="flex flex-col gap-2 w-full",
        ),
        rx.el.div(
            form_field(
                "Job title *",
                user_input(
                    placeholder="CTO",
                    required=True,
                    type_="text",
                    name="job_title",
                ),
            ),
            # Company Information
            form_field(
                "Company name *",
                user_input(
                    placeholder="Pynecone, Inc.",
                    required=True,
                    type_="text",
                    name="company_name",
                ),
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-2 w-full",
        ),
        rx.el.div(
            form_field(
                "LinkedIn profile URL",
                user_input(
                    placeholder="https://linkedin.com/in/your-profile",
                    required=True,
                    type_="text",
                    name="linkedin_url",
                ),
            ),
            rx.text(
                rx.cond(
                    BookingFormState.show_linkedin_error,
                    "The LinkedIn provided is not valid.",
                    "",
                ),
                class_name="text-sm text-red-10 font-medium",
            ),
            class_name="flex flex-col gap-2 w-full",
        ),
        form_field(
            "What are you looking to build? *",
            rx.el.textarea(
                placeholder="Please list any apps, requirements, or data sources you plan on using",
                required=True,
                name="internal_tools",
                class_name="box-border border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--color-violet-4)] border rounded-[0.625rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 h-24 px-2.5 py-2 resize-none",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Number of employees *",
                    class_name="text-slate-12 text-base font-semibold",
                ),
                select_employees(),
                class_name="flex flex-col gap-2 w-full",
            ),
            rx.el.div(
                rx.el.label(
                    "How did you hear about us? *",
                    class_name="text-slate-12 text-base font-semibold",
                ),
                select_referral_source(),
                class_name="flex flex-col gap-2 w-full",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-2 w-full",
        ),
        class_name="flex flex-col gap-4",
    )

def booking_form() -> rx.Component:
    """Returns the booking form & thank-you"""
    return rx.fragment(
        rx.box(
            rx.el.form(
                demo_request_form(),
                button(
                    "Submit",
                    class_name="w-full mt-6",
                    size="lg",
                    type_="submit",
                ),
                on_submit=BookingFormState.submit,
                class_name="flex flex-col gap-4 h-full",
            ),
            class_name="relative bg-slate-1 p-6 sm:p-8 rounded-2xl border-2 border-violet-9 dark:border-violet-6 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0",
        ),
        thank_you_modal(),
    )
