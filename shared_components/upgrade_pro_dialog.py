import re
import urllib.parse
from typing import Any

import reflex as rx
from reflex.experimental import ClientStateVar

from shared_components import constants
from shared_components.logger import ReflexLogger, reflex_log_level_converter
from shared_components.metrics.posthog import DemoEvent, send_data_to_posthog
from shared_components.ui.components import button
from shared_components.ui.components.dropdown import dropdown
from shared_components.ui.components.icons import hi
from shared_components.ui.components.select import select, select_item
from shared_components.ui.components.user_input import user_input

show_thank_you_dialog = ClientStateVar.create(
    var_name="show_thank_you_dialog", default=False
)

show_upgrade_pro_dialog = ClientStateVar.create(
    var_name="show_upgrade_pro_dialog", default=False
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


def is_valid_linkedin_url(linkedin_url: str) -> bool:
    """Check if LinkedIn URL matches correct pattern."""
    linkedin_pattern = r"^https?://(www\.)?linkedin\.com/(in|company)/.+$"
    return bool(re.match(linkedin_pattern, linkedin_url))


def is_small_company(num_employees: str) -> bool:
    """Check if company has 10 or fewer employees."""
    return num_employees in ["1", "2-5", "6-10"]


class UpgradeProDialogState(rx.State):
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

        yield UpgradeProDialogState.send_demo_event(form_data)

        if is_small_company(self.selected_num_employees):
            yield show_upgrade_pro_dialog.push(False)
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


def logo(path: str, width: str = "4.75rem") -> rx.Component:
    return rx.fragment(
        rx.color_mode_cond(
            rx.image(
                src=f"{constants.REFLEX_URL}/landing/companies/light/{path}.svg",
                alt=f"{path} logo",
                loading="lazy",
                width=width,
                class_name="shrink-0 grayscale-[1] h-auto",
            ),
            rx.image(
                src=f"{constants.REFLEX_URL}/landing/companies/dark/{path}.svg",
                alt=f"{path} logo",
                loading="lazy",
                width=width,
                class_name="shrink-0 grayscale-[1] h-auto",
            ),
        ),
    )


def companies_section() -> rx.Component:
    return rx.el.section(
        rx.text(
            "Trusted by",
            class_name="text-slate-12 text-xl font-semibold",
        ),
        rx.box(
            logo("fastly"),
            logo("autodesk", "8rem"),
            logo("dell"),
            logo("sellerx", "6rem"),
            class_name="flex flex-row flex-wrap justify-start items-center gap-x-8 gap-y-3 h-auto",
        ),
        class_name="flex flex-col justify-center gap-4 w-full h-auto mt-1.5",
    )


def select_employees() -> rx.Component:
    return select(
        placeholder=UpgradeProDialogState.selected_num_employees,
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
                            UpgradeProDialogState.set_selected_num_employees(option),
                        ],
                    ),
                    is_selected=option == UpgradeProDialogState.selected_num_employees,
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
        placeholder=UpgradeProDialogState.selected_referral_source,
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
                            UpgradeProDialogState.set_selected_referral_source(option),
                        ],
                    ),
                    is_selected=option
                    == UpgradeProDialogState.selected_referral_source,
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
                    UpgradeProDialogState.show_email_error,
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
                    UpgradeProDialogState.show_linkedin_error,
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
                class_name="box-border border-slate-5 bg-slate-1 focus:shadow-[0px_0px_0px_2px_var(--c-violet-4)] border rounded-[0.625rem] font-medium text-slate-12 text-sm placeholder:text-slate-9 outline-none focus:outline-none caret-slate-12 h-24 px-2.5 py-2 resize-none",
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


def benefit(text: str) -> rx.Component:
    return rx.el.li(
        hi(
            "checkmark-circle-02",
            class_name="!text-violet-9",
        ),
        rx.text(
            text,
            class_name="text-sm font-medium text-slate-12",
        ),
        class_name="items-center flex gap-2",
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                hi(icon, class_name="text-slate-12 size-5"),
                rx.text(title, class_name="text-slate-12 text-base font-semibold"),
                class_name="flex flex-row gap-2 items-center",
            ),
            rx.text(
                description, class_name="text-slate-9 font-medium text-sm text-start"
            ),
            class_name="flex flex-col gap-1.5 w-full py-2",
        ),
        class_name="border-slate-3",
    )


def quote_card() -> rx.Component:
    return rx.box(
        rx.text(
            "“Reflex has been a game changer for our team”",
            class_name="text-slate-11 text-lg font-medium",
        ),
        rx.image(
            src=rx.color_mode_cond(
                light="/light/dell.svg",
                dark="/dark/dell.svg",
            ),
            class_name="h-5",
        ),
        class_name="flex flex-col gap-2 justify-start items-start mb-4",
    )


def sales_dialog_content() -> rx.Component:
    return rx.box(
        rx.image(
            src=rx.color_mode_cond(
                light="/light/radial_circle.svg",
                dark="/dark/radial_circle.svg",
            ),
            alt="Radial circle",
            class_name="top-0 right-0 absolute pointer-events-none z-[-1]",
        ),
        rx.box(
            rx.el.h2(
                "Get a demo of Reflex Build",
                class_name="text-slate-12 text-2xl lg:text-3xl font-semibold",
            ),
            rx.box(
                feature_card(
                    "customer-support",
                    "Custom Setup",
                    "Get a personalized walkthrough of how Reflex Build can work for your specific needs.",
                ),
                feature_card(
                    "ai-browser",
                    "Try It First",
                    "Test out Reflex Build with your team before making any commitments.",
                ),
                class_name="flex flex-col",
            ),
            rx.box(
                rx.image(
                    "/reflex_logo.svg",
                    class_name="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 z-[-1]",
                ),
                rx.video(
                    url=constants.DEMO_VIDEO_URL,
                    class_name="size-full rounded-2xl overflow-hidden z-[1] border border-slate-4/20 shadow-[0px_0px_0px_2px_var(--c-violet-6)]",
                ),
                class_name="relative isolate aspect-video",
            ),
            companies_section(),
            class_name="flex flex-col gap-4 p-4 max-lg:hidden",
        ),
    )


def upgrade_pro_dialog_content() -> rx.Component:
    return sales_dialog_content()


def companies() -> rx.Component:
    return rx.el.section(
        rx.box(
            logo("amazon"),
            logo("nasa"),
            logo("dell"),
            logo("ibm"),
            logo("accenture"),
            logo("rappi"),
            logo("nike"),
            class_name="flex flex-row flex-wrap justify-center md:justify-start items-center gap-8 h-auto",
        ),
        class_name="flex flex-col justify-center gap-4 w-full h-auto",
    )


def custom_quote_form() -> rx.Component:
    """Custom quote form component with clean, maintainable structure."""
    return rx.box(
        rx.box(
            # Left column - Content
            rx.box(
                upgrade_pro_dialog_content(),
                class_name="mb-8 lg:mb-0 text-center sm:text-left",
            ),
            # Right column - Form
            rx.box(
                rx.el.form(
                    demo_request_form(),
                    button(
                        "Submit",
                        class_name="w-full mt-6",
                        size="lg",
                        type_="submit",
                    ),
                    on_submit=UpgradeProDialogState.submit,
                    class_name="flex flex-col gap-4 h-full",
                ),
                class_name="relative bg-slate-1 p-6 sm:p-8 rounded-2xl border-2 border-violet-9 dark:border-violet-6 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 max-w-7xl mx-auto items-start",
        ),
        class_name="py-8 sm:py-12 px-4 sm:px-8",
    )


def upgrade_pro_dialog() -> rx.Component:
    return rx.fragment(
        rx.dialog.root(
            rx.dialog.trigger(rx.fragment()),
            rx.dialog.content(
                custom_quote_form(),
                class_name="w-full max-w-[75rem] overflow-hidden relative !shadow-large !rounded-xl !bg-slate-1 !p-2 md:!p-6 !font-sans",
                on_interact_outside=show_upgrade_pro_dialog.set_value(False),
                on_escape_key_down=show_upgrade_pro_dialog.set_value(False),
            ),
            open=show_upgrade_pro_dialog.value,
            on_open_change=UpgradeProDialogState.set_show_email_error(False),
        ),
        thank_you_modal(),
    )
