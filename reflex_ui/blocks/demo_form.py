"""Demo form component for collecting user information and scheduling enterprise calls.

This module provides a comprehensive demo form that validates company emails,
sends data to PostHog and Slack, and redirects users to appropriate Cal.com links
based on company size.
"""

from typing import Any

import reflex as rx
from reflex.experimental.client_state import ClientStateVar

import reflex_ui as ui

demo_form_error_message = ClientStateVar.create("demo_form_error_message", "")
demo_form_open_cs = ClientStateVar.create("demo_form_open", False)


def check_if_company_email(email: str) -> bool:
    """Check if an email address is from a company domain (not a personal email provider).

    Args:
        email: The email address to check

    Returns:
        True if it's likely a company email, False if it's from a personal provider
    """
    if not email or "@" not in email:
        return False

    domain = email.split("@")[-1].lower()

    # List of common personal email providers
    personal_domains = {
        "gmail.com",
        "outlook.com",
        "hotmail.com",
        "yahoo.com",
        "icloud.com",
        "aol.com",
        "protonmail.com",
        "proton.me",
        "mail.com",
        "yandex.com",
        "zoho.com",
        "live.com",
        "msn.com",
        "me.com",
        "mac.com",
        "googlemail.com",
        "yahoo.co.uk",
        "yahoo.ca",
        "yahoo.co.in",
        "outlook.co.uk",
        "hotmail.co.uk",
    }

    return domain not in personal_domains and ".edu" not in domain


def check_if_default_value_is_selected(value: str) -> bool:
    """Check if the default value is selected."""
    return value.strip() != "Select"


class DemoFormStateUI(rx.State):
    """State for handling demo form submissions and validation."""

    @rx.event
    def on_submit(self, form_data: dict[str, Any]):
        """Handle form submission with validation logic.

        Validates company email and required fields. If successful, clears errors.
        The actual submission is handled by the external script.

        Args:
            form_data: Form data dictionary containing user inputs
        """
        if not check_if_company_email(form_data.get("email", "")):
            return [
                rx.set_focus("email"),
                rx.toast.error(
                    "Please enter a valid company email - gmails, aol, me, etc are not allowed",
                    position="top-center",
                ),
                demo_form_error_message.push(
                    "Please enter a valid company email - gmails, aol, me, etc are not allowed"
                ),
            ]
        
        # Check if the has selected a number of employees
        if not check_if_default_value_is_selected(
            form_data.get("number_of_employees", "")
        ):
            return [
                rx.toast.error(
                    "Please select a number of employees",
                    position="top-center",
                ),
                demo_form_error_message.push("Please select a number of employees"),
            ]
            
        # Check if the has entered a referral source
        if not check_if_default_value_is_selected(
            form_data.get("how_did_you_hear_about_us", "")
        ):
            return [
                rx.toast.error(
                    "Please select how did you hear about us",
                    position="top-center",
                ),
                demo_form_error_message.push(
                    "Please select how did you hear about us"
                ),
            ]
            
        # Check if the has entered a technical level
        if not check_if_default_value_is_selected(form_data.get("technical_level", "")):
            return [
                rx.set_focus("technical_level"),
                rx.toast.error(
                    "Please select a technical level",
                    position="top-center",
                ),
                demo_form_error_message.push("Please select a technical level"),
            ]

        return None


def input_field(
    label: str,
    placeholder: str,
    name: str,
    type: str = "text",
    required: bool = False,
) -> rx.Component:
    """Create a labeled input field component.

    Args:
        label: The label text to display above the input
        placeholder: Placeholder text for the input
        name: The name attribute for the input field
        type: The input type (text, email, tel, etc.)
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled input field
    """
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-sm font-medium text-secondary-12",
        ),
        ui.input(
            placeholder=placeholder,
            name=name,
            type=type,
            required=required,
            max_length=255,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5",
    )


def text_area_field(
    label: str, placeholder: str, name: str, required: bool = False
) -> rx.Component:
    """Create a labeled textarea field component.

    Args:
        label: The label text to display above the textarea
        placeholder: Placeholder text for the textarea
        name: The name attribute for the textarea field
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled textarea field
    """
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-secondary-12"),
        ui.textarea(
            placeholder=placeholder,
            name=name,
            required=required,
            class_name="w-full min-h-14",
            max_length=800,
        ),
        class_name="flex flex-col gap-1.5",
    )


def select_field(
    label: str,
    name: str,
    items: list[str],
    required: bool = False,
) -> rx.Component:
    """Create a labeled select field component.

    Args:
        label: The label text to display above the select
        name: The name attribute for the select field
        items: List of options to display in the select
        required: Whether the field is required

    Returns:
        A Reflex component containing the labeled select field
    """
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-xs lg:text-sm font-medium text-secondary-12 truncate min-w-0",
        ),
        ui.select(
            default_value="Select",
            name=name,
            items=items,
            required=required,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5 min-w-0",
    )


def demo_form(**props) -> rx.Component:
    """Create and return the demo form component.

    Builds a complete form with all required fields, validation,
    and styling. The form includes personal info, company details,
    and preferences.

    Args:
        **props: Additional properties to pass to the form component

    Returns:
        A Reflex form component with all demo form fields
    """
    form = rx.el.form(
        rx.el.div(
            input_field("First name", "John", "first_name", "text", True),
            input_field("Last name", "Smith", "last_name", "text", True),
            class_name="grid grid-cols-2 gap-4",
        ),
        input_field("Business Email", "john@company.com", "email", "email", True),
        rx.el.div(
            input_field("Job title", "CTO", "job_title", "text", True),
            input_field("Company name", "Pynecone, Inc.", "company_name", "text", True),
            class_name="grid grid-cols-2 gap-4",
        ),
        text_area_field(
            "What are you looking to build? *",
            "Please list any apps, requirements, or data sources you plan on using",
            "internal_tools",
            True,
        ),
        rx.el.div(
            select_field(
                "Number of employees?",
                "number_of_employees",
                ["1", "2-5", "6-10", "11-50", "51-100", "101-500", "500+"],
            ),
            select_field(
                "How did you hear about us?",
                "how_did_you_hear_about_us",
                [
                    "Google Search",
                    "Social Media",
                    "Word of Mouth",
                    "Blog",
                    "Conference",
                    "Other",
                ],
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
        ),
        select_field(
            "How technical are you?",
            "technical_level",
            ["Non-technical", "Neutral", "Technical"],
            True,
        ),
        rx.cond(
            demo_form_error_message.value,
            rx.el.span(
                demo_form_error_message.value,
                class_name="text-destructive-10 text-sm font-medium px-2 py-1 rounded-md bg-destructive-3 border border-destructive-4",
            ),
        ),
        ui.button(
            "Submit",
            type="submit",
            class_name="w-full",
        ),
        on_submit=DemoFormStateUI.on_submit,
        class_name=ui.cn(
            "@container flex flex-col lg:gap-6 gap-2 p-6",
            props.pop("class_name", ""),
        ),
        data_default_form_id="965991",
        **props,
    )
    return rx.fragment(
        form,
    )


def demo_form_dialog(trigger: rx.Component | None, **props) -> rx.Component:
    """Return a demo form dialog container element.

    Args:
        trigger: The component that triggers the dialog
        **props: Additional properties to pass to the dialog root

    Returns:
        A Reflex dialog component containing the demo form
    """
    class_name = ui.cn("w-auto", props.pop("class_name", ""))
    return ui.dialog.root(
        ui.dialog.trigger(render_=trigger),
        ui.dialog.portal(
            ui.dialog.backdrop(),
            ui.dialog.popup(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Book a Demo",
                            class_name="text-xl font-bold text-secondary-12",
                        ),
                        ui.dialog.close(
                            render_=ui.button(
                                ui.hi("Cancel01Icon"),
                                variant="ghost",
                                size="icon-sm",
                                class_name="text-secondary-11",
                            ),
                        ),
                        class_name="flex flex-row justify-between items-center gap-1 px-6 pt-4 -mb-4",
                    ),
                    demo_form(class_name="w-full max-w-md"),
                    class_name="relative isolate overflow-hidden -m-px w-full max-w-md",
                ),
                class_name="h-fit mt-1 overflow-hidden w-full max-w-md",
            ),
        ),
        open=demo_form_open_cs.value,
        on_open_change=demo_form_open_cs.set_value,
        class_name=class_name,
        **props,
    )
