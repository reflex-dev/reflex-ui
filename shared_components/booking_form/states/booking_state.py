import reflex as rx
import re
import urllib.parse
from typing import Any

from reflex.experimental import ClientStateVar

from shared_components.booking_form import constants
from shared_components.booking_form.logger import ReflexLogger, reflex_log_level_converter
from shared_components.booking_form.metrics.posthog import DemoEvent, send_data_to_posthog


show_thank_you_dialog = ClientStateVar.create(
    var_name="show_thank_you_dialog", default=False
)

benefits = [
    "Increased message limit",
    "Unlimited private projects",
    "Priority support",
    "Custom domains",
    "Pro Hosting features",
]

logger = ReflexLogger(__name__, reflex_log_level_converter(constants.LOG_LEVEL))


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
    personal_domains = constants.BANNED_EMAIL_DOMAINS

    return domain not in personal_domains and ".edu" not in domain


def is_valid_linkedin_url(linkedin_url: str) -> bool:
    """Check if LinkedIn URL matches correct pattern."""
    linkedin_pattern = r"^https?://(www\.)?linkedin\.com/(in|company)/.+$"
    return bool(re.match(linkedin_pattern, linkedin_url))


def is_small_company(num_employees: str) -> bool:
    """Check if company has 10 or fewer employees."""
    return num_employees in ["1", "2-5", "6-10"]


class BookingFormState(rx.State):
    show_email_error: bool = False
    show_linkedin_error: bool = False
    selected_referral_source: str = "Google Search"
    selected_num_employees: str = "500+"
    posthog_api_key: str = ""
    cal_com_url: str = ""

    @rx.event
    def set_selected_num_employees(self, value: str):
        """Set the selected number of employees."""
        self.selected_num_employees = value

    @rx.event
    def set_selected_referral_source(self, value: str):
        """Set the selected referral source."""
        self.selected_referral_source = value

    @rx.event
    def set_show_email_error(self, value: bool):
        """Set the visibility of the email error message."""
        self.show_email_error = value

    @rx.event
    def submit(self, form_data: dict[str, Any]):
        if not check_if_company_email(form_data.get("company_email", "")):
            self.show_email_error = True
            yield rx.set_focus("company_email")
            return

        if not is_valid_linkedin_url(form_data.get("linkedin_url", "")):
            self.show_linkedin_error = True
            return

        notes_content = f"""
Name: {form_data.get("first_name", "")} {form_data.get("last_name", "")}
Business Email: {form_data.get("company_email", "")}
LinkedIn URL: {form_data.get("linkedin_url", "")}
Job Title: {form_data.get("job_title", "")}
Company Name: {form_data.get("company_name", "")}
Number of Employees: {self.selected_num_employees}
Internal Tools to Build: {form_data.get("internal_tools", "")}
How they heard about Reflex: {self.selected_referral_source}"""

        yield BookingFormState.send_demo_event(form_data)

        if is_small_company(self.selected_num_employees):
            yield show_thank_you_dialog.push(True)
            return

        params = {
            "email": form_data.get("company_email", ""),
            "name": f"{form_data.get('first_name', '')} {form_data.get('last_name', '')}",
            "notes": notes_content,
        }

        query_string = urllib.parse.urlencode(params)
        cal_url = f"{self.cal_com_url}?{query_string}"

        return rx.redirect(cal_url)

    @rx.event(background=True)
    async def send_demo_event(self, form_data: dict[str, Any]):
        if self.posthog_api_key:
            first_name = form_data.get("first_name", "")
            last_name = form_data.get("last_name", "")
            await send_data_to_posthog(
                DemoEvent(
                    distinct_id=f"{first_name} {last_name}",
                    thread_id="demo_thread_id",
                    tier_type="demo_tier_type",
                    first_name=first_name,
                    last_name=last_name,
                    email=form_data.get("company_email", ""),
                    company_email=form_data.get("company_email", ""),
                    linkedin_url=form_data.get("linkedin_url", ""),
                    job_title=form_data.get("job_title", ""),
                    company_name=form_data.get("company_name", ""),
                    num_employees=self.selected_num_employees,
                    internal_tools=form_data.get("internal_tools", ""),
                    referral_source=self.selected_referral_source,
                )
            )
