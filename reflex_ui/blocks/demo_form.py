"""Demo form component for collecting user information and scheduling enterprise calls.

This module provides a comprehensive demo form that validates company emails,
sends data to PostHog and Slack, and redirects users to appropriate Cal.com links
based on company size.
"""

import os
import urllib.parse
from dataclasses import asdict, dataclass
from typing import Any

import httpx
import reflex as rx
from reflex.utils.console import log

import reflex_ui as ui

CAL_REQUEST_DEMO_URL = os.getenv(
    "CAL_REQUEST_DEMO_URL", "https://cal.com/team/reflex/reflex-intro"
)
CAL_ENTERPRISE_FOLLOW_UP_URL = os.getenv(
    "CAL_ENTERPRISE_FOLLOW_UP_URL",
    "https://cal.com/team/reflex/reflex-intro",
)
SLACK_DEMO_WEBHOOK_URL = os.getenv("SLACK_DEMO_WEBHOOK_URL", "")
POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY", "")


@dataclass(kw_only=True)
class PosthogEvent:
    """Base event structure."""

    distinct_id: str

    def to_dict(self) -> dict[str, Any]:
        """Convert the event instance to a dictionary representation.

        Returns:
            A dictionary containing all the event data.
        """
        return asdict(self)


@dataclass
class DemoEvent(PosthogEvent):
    """Event for demo booking."""

    first_name: str
    last_name: str
    company_email: str
    linkedin_url: str
    job_title: str
    company_name: str
    num_employees: str
    internal_tools: str
    referral_source: str
    phone_number: str = ""


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
            class_name="w-full",
        ),
        class_name="flex flex-col gap-2",
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
            placeholder=placeholder, name=name, required=required, class_name="w-full"
        ),
        class_name="flex flex-col gap-2",
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
        rx.el.label(label, class_name="block text-sm font-medium text-secondary-12"),
        ui.select(
            default_value="Select",
            name=name,
            items=items,
            required=required,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-2",
    )


def is_small_company(num_employees: str) -> bool:
    """Check if company has 10 or fewer employees."""
    return num_employees in ["1", "2-5", "6-10"]


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


def check_if_number_of_employees_is_valid(number_of_employees: str) -> bool:
    """Check if the number of employees is valid."""
    return number_of_employees.strip() != "Select"


def check_if_referral_source_is_valid(referral_source: str) -> bool:
    """Check if the referral source is valid."""
    return referral_source.strip() != "Select"


class DemoForm(rx.ComponentState):
    """Component state for handling demo form submissions and integrations."""

    @rx.event(background=True)
    async def on_submit(self, form_data: dict[str, Any]):
        """Handle form submission with validation and routing logic.

        Validates company email, sends data to PostHog and Slack,
        then redirects to appropriate Cal.com link based on company size.

        Args:
            form_data: Form data dictionary containing user inputs
        """
        if not check_if_company_email(form_data.get("email", "")):
            yield rx.set_focus("email")
            yield rx.toast.error(
                "Please enter a valid company email",
                position="top-center",
            )
            return
        # Check if the has selected a number of employees
        if not check_if_number_of_employees_is_valid(
            form_data.get("number_of_employees", "")
        ):
            yield rx.toast.error(
                "Please select a number of employees",
                position="top-center",
            )
            return

        # Check if the has entered a referral source
        if not check_if_referral_source_is_valid(
            form_data.get("how_did_you_hear_about_us", "")
        ):
            yield rx.toast.error(
                "Please select how did you hear about us",
                position="top-center",
            )
            return
        # Send to PostHog and Slack for all submissions
        await self.send_demo_event(form_data)

        yield rx.call_script(
            f"try {{ ko.identify('{form_data.get('email', '')}'); }} catch(e) {{ console.warn('Koala identify failed:', e); }}"
        )
        if is_small_company(form_data.get("number_of_employees", "")):
            yield rx.toast.success(
                "Thanks for your interest in Reflex! We'll be in touch soon.",
                position="top-center",
            )
            yield rx.redirect(CAL_REQUEST_DEMO_URL)
            return
        notes_content = f"""
Name: {form_data.get("first_name", "")} {form_data.get("last_name", "")}
Business Email: {form_data.get("email", "")}
LinkedIn URL: {form_data.get("linkedin_profile_url", "")}
Job Title: {form_data.get("job_title", "")}
Company Name: {form_data.get("company_name", "")}
Number of Employees: {form_data.get("number_of_employees", "")}
Internal Tools to Build: {form_data.get("internal_tools", "")}
How they heard about Reflex: {form_data.get("how_did_you_hear_about_us", "")}"""

        params = {
            "email": form_data.get("email", ""),
            "name": f"{form_data.get('first_name', '')} {form_data.get('last_name', '')}",
            "notes": notes_content,
        }

        query_string = urllib.parse.urlencode(params)
        cal_url_with_params = f"{CAL_ENTERPRISE_FOLLOW_UP_URL}?{query_string}"

        yield rx.redirect(cal_url_with_params)

    async def send_demo_event(self, form_data: dict[str, Any]):
        """Create and send demo event to PostHog and Slack.

        Converts form data into a DemoEvent and sends to both analytics
        platforms. Logs errors but doesn't raise exceptions.

        Args:
            form_data: Form data dictionary containing user inputs
        """
        first_name = form_data.get("first_name", "")
        last_name = form_data.get("last_name", "")
        demo_event = DemoEvent(
            distinct_id=f"{first_name} {last_name}",
            first_name=first_name,
            last_name=last_name,
            company_email=form_data.get("email", ""),
            linkedin_url=form_data.get("linkedin_profile_url", ""),
            job_title=form_data.get("job_title", ""),
            company_name=form_data.get("company_name", ""),
            num_employees=form_data.get("number_of_employees", ""),
            internal_tools=form_data.get("internal_tools", ""),
            referral_source=form_data.get("how_did_you_hear_about_us", ""),
            phone_number=form_data.get("phone_number", ""),
        )

        # Send to PostHog
        await self.send_data_to_posthog(demo_event)

        try:
            await self.send_data_to_slack(demo_event)
        except Exception as e:
            log(f"Failed to send to Slack: {e}")

    async def send_data_to_posthog(self, event_instance: PosthogEvent):
        """Send data to PostHog using class introspection.

        Args:
            event_instance: An instance of a PosthogEvent subclass.

        Raises:
            httpx.HTTPError: When there is an error sending data to PostHog.
        """
        event_data = {
            "api_key": POSTHOG_API_KEY,
            "event": event_instance.__class__.__name__,
            "properties": event_instance.to_dict(),
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://app.posthog.com/capture/", json=event_data
                )
                response.raise_for_status()
        except Exception:
            log("Error sending data to PostHog")

    async def send_data_to_slack(self, event_instance: DemoEvent):
        """Send demo form data to Slack webhook.

        Args:
            event_instance: An instance of DemoEvent with form data.
        """
        slack_payload = {
            "lookingToBuild": event_instance.internal_tools,
            "businessEmail": event_instance.company_email,
            "howDidYouHear": event_instance.referral_source,
            "linkedinUrl": event_instance.linkedin_url,
            "jobTitle": event_instance.job_title,
            "numEmployees": event_instance.num_employees,
            "companyName": event_instance.company_name,
            "firstName": event_instance.first_name,
            "lastName": event_instance.last_name,
            "phoneNumber": event_instance.phone_number,
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    SLACK_DEMO_WEBHOOK_URL,
                    json=slack_payload,
                    headers={"Content-Type": "application/json"},
                )
                response.raise_for_status()
        except Exception as e:
            log(f"Error sending data to Slack webhook: {e}")

    @classmethod
    def get_component(cls, **props):
        """Create and return the demo form component.

        Builds a complete form with all required fields, validation,
        and styling. The form includes personal info, company details,
        and preferences.

        Args:
            **props: Additional properties to pass to the form component

        Returns:
            A Reflex form component with all demo form fields
        """
        return rx.el.form(
            rx.el.div(
                input_field("First name", "John", "first_name", "text", True),
                input_field("Last name", "Smith", "last_name", "text", True),
                class_name="grid grid-cols-2 gap-4",
            ),
            input_field("Email", "john@example.com", "email", "email", True),
            rx.el.div(
                input_field("Job title", "CTO", "job_title", "text", True),
                input_field(
                    "Company name", "Pynecone, Inc.", "company_name", "text", True
                ),
                class_name="grid grid-cols-2 gap-4",
            ),
            input_field(
                "Linkedin Profile URL",
                "https://linkedin.com/in/your-profile",
                "linkedin_profile_url",
                "text",
                False,
            ),
            input_field(
                "Phone number",
                "+1 (555) 123-4567",
                "phone_number",
                "tel",
                False,
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
                class_name="grid grid-cols-2 gap-4",
            ),
            ui.button("Submit", type="submit", class_name="w-full"),
            on_submit=cls.on_submit,
            class_name=ui.cn(
                "flex flex-col gap-6 p-6",
                props.pop("class_name", ""),
            ),
            **props,
        )


demo_form = DemoForm.create
