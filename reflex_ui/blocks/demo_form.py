"""Multi-step demo form component for collecting user information and scheduling calls.

This module provides a multi-step demo form that:
- Step 1: Collects name and email (validates company vs personal email)
- Step 2: Collects number of employees (routes small companies to Unify)
- Step 3: Collects company details and schedules demo
"""

import os
import urllib.parse
from typing import Any

import httpx
import reflex as rx
from reflex.utils.console import log

import reflex_ui as ui
from reflex_ui.blocks.telemetry.unify import unify_identify_js

# Environment variables for Cal.com URLs
CAL_REQUEST_DEMO_URL = os.getenv(
    "CAL_REQUEST_DEMO_URL", "https://cal.com/team/reflex/reflex-intro-call"
)

# Slack webhook URL for notifications (set via environment variable)
SLACK_DEMO_WEBHOOK_URL = os.getenv("SLACK_DEMO_WEBHOOK_URL", "")

# Threshold for small company (≤15 employees goes to Unify)
SMALL_COMPANY_THRESHOLD = 15


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


def get_employee_count(num_employees: str) -> int:
    """Convert employee count string to a numeric value for comparison.

        Args:
        num_employees: String like "1-5", "6-15", "16-50", etc.

    Returns:
        The upper bound of the range as an integer
    """
    employee_map = {
        "1-5": 5,
        "6-15": 15,
        "16-50": 50,
        "51-200": 200,
        "201-500": 500,
        "500+": 1000,
    }
    return employee_map.get(num_employees, 0)


class DemoFormState(rx.State):
    """State for the multi-step demo form."""

    # Current step (1, 2, or 3)
    current_step: int = 1

    # Form data stored across steps
    first_name: str = ""
    last_name: str = ""
    email: str = ""
    num_employees: str = ""
    company_name: str = ""
    job_title: str = ""
    looking_to_build: str = ""

    # Loading state
    is_loading: bool = False

    # Error message
    error_message: str = ""

    # Sent to Unify flag (shows thank you screen)
    sent_to_unify: bool = False

    # Show calendar flag (shows embedded Cal.com calendar)
    show_calendar: bool = False

    # Cal.com prefill data (stored as JSON string for use in script)
    cal_prefill_json: str = "{}"
    cal_prefill_query: str = ""

    @rx.var
    def progress_percentage(self) -> int:
        """Calculate progress percentage based on current step."""
        return int((self.current_step / 3) * 100)

    @rx.var
    def step_title(self) -> str:
        """Get the title for the current step."""
        titles = {
            1: "Let's get started",
            2: "Company size",
            3: "Tell us more",
        }
        return titles.get(self.current_step, "")

    @rx.var
    def step_subtitle(self) -> str:
        """Get the subtitle for the current step."""
        subtitles = {
            1: "Enter your details to book a demo",
            2: "How many people work at your company?",
            3: "Help us prepare for your demo",
        }
        return subtitles.get(self.current_step, "")

    @rx.event
    def reset_form(self):
        """Reset the form to initial state."""
        self.current_step = 1
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.num_employees = ""
        self.company_name = ""
        self.job_title = ""
        self.looking_to_build = ""
        self.error_message = ""
        self.is_loading = False
        self.sent_to_unify = False
        self.show_calendar = False
        self.cal_prefill_json = "{}"
        self.cal_prefill_query = ""

    @rx.event
    def submit_step_1(self, form_data: dict[str, Any]):
        """Handle step 1 submission - validate email and proceed or send to Unify."""
        self.error_message = ""
        self.first_name = form_data.get("first_name", "").strip()
        self.last_name = form_data.get("last_name", "").strip()
        self.email = form_data.get("email", "").strip()

        # Validate required fields
        if not self.first_name:
            self.error_message = "Please enter your first name"
            return rx.toast.error("Please enter your first name", position="top-center")

        if not self.last_name:
            self.error_message = "Please enter your last name"
            return rx.toast.error("Please enter your last name", position="top-center")

        if not self.email:
            self.error_message = "Please enter your email"
            return rx.toast.error("Please enter your email", position="top-center")

        # Check if personal email -> send to Unify (show thank you screen)
        if not check_if_company_email(self.email):
            self.sent_to_unify = True
            # Call Unify identify on frontend and send Slack notification
            return [
                rx.call_script(
                    unify_identify_js(
                        email=self.email,
                        person_attributes={"status": "Personal email"},
                    )
                ),
                DemoFormState.send_unify_notification("Personal email detected"),
            ]

        # Company email -> proceed to step 2
        self.current_step = 2

    @rx.event
    def submit_step_2(self, form_data: dict[str, Any]):
        """Handle step 2 submission - check company size and proceed or send to Unify."""
        self.error_message = ""
        self.num_employees = form_data.get("num_employees", "")

        # Validate selection
        if not self.num_employees or self.num_employees == "Select":
            self.error_message = "Please select the number of employees"
            return rx.toast.error(
                "Please select the number of employees", position="top-center"
            )

        # Check if small company (≤15) -> send to Unify (show thank you screen)
        employee_count = get_employee_count(self.num_employees)
        if employee_count <= SMALL_COMPANY_THRESHOLD:
            self.sent_to_unify = True
            # Call Unify identify on frontend and send Slack notification
            return [
                rx.call_script(
                    unify_identify_js(
                        email=self.email,
                        person_attributes={"status": f"Small company ({self.num_employees} employees)"},
                    )
                ),
                DemoFormState.send_unify_notification(f"Small company ({self.num_employees} employees)"),
            ]

        # Larger company -> proceed to step 3
        self.current_step = 3

    @rx.event
    def submit_step_3(self, form_data: dict[str, Any]):
        """Handle step 3 submission - collect final details and show calendar."""
        import json

        self.error_message = ""
        self.is_loading = True

        self.company_name = form_data.get("company_name", "").strip()
        self.job_title = form_data.get("job_title", "").strip()
        self.looking_to_build = form_data.get("looking_to_build", "").strip()

        # Validate required fields
        if not self.company_name:
            self.is_loading = False
            self.error_message = "Please enter your company name"
            return rx.toast.error(
                "Please enter your company name", position="top-center"
            )

        if not self.job_title:
            self.is_loading = False
            self.error_message = "Please enter your job title"
            return rx.toast.error("Please enter your job title", position="top-center")

        # Build prefill data for Cal.com and store in state
        name = f"{self.first_name} {self.last_name}"
        notes = f"Company: {self.company_name}\nJob Title: {self.job_title}\nEmployees: {self.num_employees}\nLooking to build: {self.looking_to_build or 'Not specified'}"
        
        # Build URL query string for Cal.com prefill
        prefill_params = urllib.parse.urlencode({
            "name": name,
            "email": self.email,
            "notes": notes,
        })
        self.cal_prefill_query = prefill_params
        self.cal_prefill_json = json.dumps({
            "name": name,
            "email": self.email,
            "notes": notes,
        })

        self.is_loading = False
        self.show_calendar = True

        # Send Slack notification
        return DemoFormState.send_enterprise_notification()

    @rx.event
    def go_back(self):
        """Go back to the previous step."""
        if self.current_step > 1:
            self.current_step -= 1
            self.error_message = ""

    @rx.event
    def go_back_from_calendar(self):
        """Go back from calendar to step 3."""
        self.show_calendar = False

    @rx.event
    def init_cal_embed(self):
        """Initialize Cal.com embed after component mounts."""
        import time
        unique_ns = f"reflex-demo-{int(time.time() * 1000)}"
        
        init_script = f"""
        (function initCal() {{
            var ns = "{unique_ns}";
            var el = document.querySelector('.cal-embed-container');
            
            if (!el || el.dataset.calInit === 'true') return;
            el.dataset.calInit = 'true';
            el.innerHTML = '';
            
            // Load Cal.com script if needed
            if (!window.Cal) {{
                var p=function(a,ar){{a.q.push(ar)}},d=document;
                window.Cal=window.Cal||function(){{
                    var cal=window.Cal,ar=arguments;
                    if(!cal.loaded){{cal.ns={{}};cal.q=[];d.head.appendChild(d.createElement("script")).src="https://app.cal.com/embed/embed.js";cal.loaded=true}}
                    if(ar[0]==="init"){{var api=function(){{p(api,arguments)}},ns=ar[1];api.q=[];if(typeof ns==="string"){{cal.ns[ns]=cal.ns[ns]||api;p(cal.ns[ns],ar);p(cal,["initNamespace",ns])}}else p(cal,ar);return}}
                    p(cal,ar);
                }};
            }}
            
            Cal("init", ns, {{origin: "https://app.cal.com"}});
            
            // Wait for Cal to be ready
            if (!window.Cal.ns || !window.Cal.ns[ns]) {{
                el.dataset.calInit = 'false';
                setTimeout(initCal, 100);
                return;
            }}
            
            Cal.ns[ns]("inline", {{
                elementOrSelector: el,
                config: {{"layout": "month_view"}},
                calLink: "team/reflex/reflex-intro-call?{self.cal_prefill_query}"
            }});
            
            // Close overlay on booking success
            Cal.ns[ns]("on", {{
                action: "bookingSuccessful",
                callback: function() {{
                    setTimeout(function() {{
                        var btn = document.querySelector('.cal-embed-container').closest('[class*="fixed"]').querySelector('button[aria-label="Close"]');
                        if (btn) btn.click();
                    }}, 1500);
                }}
            }});
        }})();
        """
        return rx.call_script(init_script)

    @rx.event(background=True)
    async def send_unify_notification(self, reason: str):
        """Send Slack notification when user is sent to Unify.

        Args:
            reason: The reason for sending to Unify (e.g., "Personal email", "Small company")
        """
        if not SLACK_DEMO_WEBHOOK_URL:
            return

        async with self:
            slack_payload = {
                "text": "🔄 User was sent to Unify for a sequence",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "🔄 User Sent to Unify",
                        },
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": f"*Name:*\n{self.first_name} {self.last_name}"},
                            {"type": "mrkdwn", "text": f"*Email:*\n{self.email}"},
                            {"type": "mrkdwn", "text": f"*Reason:*\n{reason}"},
                            {"type": "mrkdwn", "text": f"*Employees:*\n{self.num_employees or 'Not provided'}"},
                        ],
                    },
                ],
            }

        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    SLACK_DEMO_WEBHOOK_URL,
                    json=slack_payload,
                    headers={"Content-Type": "application/json"},
                )
        except Exception as e:
            log(f"Error sending Unify notification to Slack: {e}")

    @rx.event(background=True)
    async def send_enterprise_notification(self):
        """Send Slack notification when enterprise user submits demo form."""
        if not SLACK_DEMO_WEBHOOK_URL:
            return

        async with self:
            slack_payload = {
                "text": "🚀 Enterprise Submitted demo form",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "🚀 Enterprise Submitted Demo Form",
                        },
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": f"*Name:*\n{self.first_name} {self.last_name}"},
                            {"type": "mrkdwn", "text": f"*Email:*\n{self.email}"},
                            {"type": "mrkdwn", "text": f"*Company:*\n{self.company_name}"},
                            {"type": "mrkdwn", "text": f"*Job Title:*\n{self.job_title}"},
                            {"type": "mrkdwn", "text": f"*Employees:*\n{self.num_employees}"},
                            {"type": "mrkdwn", "text": f"*Looking to build:*\n{self.looking_to_build or 'Not specified'}"},
                        ],
                    },
                ],
            }

        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    SLACK_DEMO_WEBHOOK_URL,
                    json=slack_payload,
                    headers={"Content-Type": "application/json"},
                )
        except Exception as e:
            log(f"Error sending Enterprise notification to Slack: {e}")


def input_field(
    label: str,
    placeholder: str,
    name: str,
    type: str = "text",
    required: bool = False,
    default_value: str = "",
) -> rx.Component:
    """Create a labeled input field component."""
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
            default_value=default_value,
            max_length=255,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5",
    )


def text_area_field(
    label: str,
    placeholder: str,
    name: str,
    required: bool = False,
    default_value: str = "",
) -> rx.Component:
    """Create a labeled textarea field component."""
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-sm font-medium text-secondary-12",
        ),
        ui.textarea(
            placeholder=placeholder,
            name=name,
            required=required,
            default_value=default_value,
            class_name="w-full min-h-24",
            max_length=800,
        ),
        class_name="flex flex-col gap-1.5",
    )


def select_field(
    label: str,
    name: str,
    items: list[str],
    required: bool = False,
    default_value: str | rx.Var[str] = "Select",
) -> rx.Component:
    """Create a labeled select field component."""
    return rx.el.div(
        rx.el.label(
            label + (" *" if required else ""),
            class_name="block text-sm font-medium text-secondary-12",
        ),
        ui.select(
            default_value=default_value,
            name=name,
            items=items,
            required=required,
            class_name="w-full",
        ),
        class_name="flex flex-col gap-1.5",
    )


def step_indicator() -> rx.Component:
    """Create a progress bar showing progress through the form."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                class_name="h-full bg-primary-9 rounded-full transition-all duration-300 ease-out",
                style={"width": f"{DemoFormState.progress_percentage}%"},
            ),
            class_name="h-1.5 bg-secondary-4 rounded-full overflow-hidden",
        ),
        class_name="mb-6",
    )


def step_header() -> rx.Component:
    """Create the header for each step showing title and subtitle."""
    return rx.el.div(
        rx.el.h2(
            DemoFormState.step_title,
            class_name="text-xl font-semibold text-secondary-12",
        ),
        rx.el.p(
            DemoFormState.step_subtitle,
            class_name="text-sm text-secondary-11",
        ),
        class_name="flex flex-col gap-1 mb-4",
    )


def error_display() -> rx.Component:
    """Display error message if present."""
    return rx.cond(
        DemoFormState.error_message,
        rx.el.div(
            rx.el.span(
                DemoFormState.error_message,
                class_name="text-sm font-medium",
            ),
            class_name="text-destructive-11 bg-destructive-3 border border-destructive-6 rounded-lg px-3 py-2",
        ),
    )


def step_1_form() -> rx.Component:
    """Step 1: Collect first name, last name, and company email."""
    return rx.el.form(
        rx.el.div(
            input_field(
                "First name",
                "John",
                "first_name",
                "text",
                True,
                DemoFormState.first_name,
            ),
            input_field(
                "Last name",
                "Smith",
                "last_name",
                "text",
                True,
                DemoFormState.last_name,
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4",
        ),
        input_field(
            "Company Email (Gmail, etc not allowed)",
            "john@company.com",
            "email",
            "email",
            True,
            DemoFormState.email,
        ),
        error_display(),
        ui.button(
            "Continue",
            type="submit",
            class_name="w-full mt-2",
        ),
        on_submit=DemoFormState.submit_step_1,
        class_name="flex flex-col gap-4",
    )


def step_2_form() -> rx.Component:
    """Step 2: Collect number of employees."""
    return rx.el.form(
        select_field(
            "Number of employees",
            "num_employees",
            ["1-5", "6-15", "16-50", "51-200", "201-500", "500+"],
            True,
            rx.cond(
                DemoFormState.num_employees != "",
                DemoFormState.num_employees,
                "Select",
            ),
        ),
        error_display(),
        rx.el.div(
            ui.button(
                "Back",
                type="button",
                variant="outline",
                on_click=DemoFormState.go_back,
                class_name="flex-1",
            ),
            ui.button(
                "Continue",
                type="submit",
                class_name="flex-1",
            ),
            class_name="flex gap-3 mt-2",
        ),
        on_submit=DemoFormState.submit_step_2,
        class_name="flex flex-col gap-4",
    )


def step_3_form() -> rx.Component:
    """Step 3: Collect company name, job title, and what they want to build."""
    return rx.el.form(
        input_field(
            "Company name",
            "Acme Inc.",
            "company_name",
            "text",
            True,
            DemoFormState.company_name,
        ),
        input_field(
            "Job title",
            "CTO",
            "job_title",
            "text",
            True,
            DemoFormState.job_title,
        ),
        text_area_field(
            "What are you looking to build?",
            "Tell us about your project (optional)",
            "looking_to_build",
            False,
            DemoFormState.looking_to_build,
        ),
        error_display(),
        rx.el.div(
            ui.button(
                "Back",
                type="button",
                variant="outline",
                on_click=DemoFormState.go_back,
                class_name="flex-1",
            ),
            ui.button(
                "Book Demo",
                type="submit",
                loading=DemoFormState.is_loading,
                class_name="flex-1",
            ),
            class_name="flex gap-3 mt-2",
        ),
        on_submit=DemoFormState.submit_step_3,
        class_name="flex flex-col gap-4",
    )


def thank_you_screen() -> rx.Component:
    """Thank you screen shown when user is sent to Unify."""
    return rx.el.div(
        # Success icon
        rx.el.div(
            rx.el.div(
                ui.hi("CheckmarkCircle02Icon", class_name="size-8 text-white"),
                class_name="size-16 rounded-full bg-success-9 flex items-center justify-center",
            ),
            class_name="flex justify-center mb-6",
        ),
        # Thank you message
        rx.el.div(
            rx.el.h2(
                "Thanks for your response!",
                class_name="text-xl font-semibold text-secondary-12 text-center",
            ),
            rx.el.p(
                "We'll get back to you soon.",
                class_name="text-sm text-secondary-11 text-center mt-1",
            ),
            class_name="flex flex-col gap-1",
        ),
        # Additional info
        rx.el.p(
            "One of our team members will reach out to discuss how we can help.",
            class_name="text-sm text-secondary-10 text-center mt-4",
        ),
        # Start over button
        ui.button(
            "Start Over",
            variant="outline",
            on_click=DemoFormState.reset_form,
            class_name="w-full mt-6",
        ),
        class_name="flex flex-col py-8",
    )


def calendar_overlay() -> rx.Component:
    """Full-screen calendar overlay that replaces the dialog."""
    return rx.cond(
        DemoFormState.show_calendar,
        rx.el.div(
            # Backdrop
            rx.el.div(
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm",
                on_click=DemoFormState.go_back_from_calendar,
            ),
            # Calendar container
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Book a Demo",
                        class_name="text-xl font-bold text-secondary-12",
                    ),
                    rx.el.p(
                        "Select a time that works for you.",
                        class_name="text-sm text-secondary-11",
                    ),
                    ui.button(
                        ui.hi("Cancel01Icon"),
                        variant="ghost",
                        size="icon-sm",
                        on_click=DemoFormState.go_back_from_calendar,
                        class_name="text-secondary-11 absolute top-4 right-4",
                        aria_label="Close",
                    ),
                    class_name="flex flex-col gap-0.5 px-6 pt-4 pb-2 relative",
                ),
                rx.el.div(
                    class_name="w-full min-h-[600px] overflow-auto cal-embed-container px-4 pb-4",
                ),
                class_name="relative bg-secondary-1 rounded-xl shadow-2xl w-full max-w-4xl max-h-[90vh] overflow-auto",
                on_mount=DemoFormState.init_cal_embed,
            ),
            class_name="fixed inset-0 z-[100000] flex items-center justify-center p-4",
        ),
        rx.fragment(),
    )


def demo_form(**props) -> rx.Component:
    """Create and return the multi-step demo form component.

    Args:
        **props: Additional properties to pass to the form container

    Returns:
        A Reflex component with the multi-step demo form
    """
    # Remove class_name from props to avoid conflict with conditional class_name
    props.pop("class_name", None)
    
    return rx.el.div(
        rx.cond(
            DemoFormState.sent_to_unify,
            # Show thank you screen when sent to Unify
            thank_you_screen(),
            # Show regular multi-step form
            rx.fragment(
                step_indicator(),
                step_header(),
                rx.cond(
                    DemoFormState.current_step == 1,
                    step_1_form(),
                    rx.cond(
                        DemoFormState.current_step == 2,
                        step_2_form(),
                        step_3_form(),
                    ),
                ),
            ),
        ),
        class_name="flex flex-col p-4 sm:p-6",
        **props,
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

    # Create a client state for the dialog open state
    from reflex.experimental.client_state import ClientStateVar

    demo_form_open_cs = ClientStateVar.create("demo_form_dialog_open", False)

    return rx.fragment(
        ui.dialog.root(
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
                            rx.el.p(
                                "Hop on a call with the Reflex team.",
                                class_name="text-sm text-secondary-11",
                            ),
                            ui.dialog.close(
                                render_=ui.button(
                                    ui.hi("Cancel01Icon"),
                                    variant="ghost",
                                    size="icon-sm",
                                    on_click=DemoFormState.reset_form,
                                    class_name="text-secondary-11 absolute top-4 right-4",
                                    aria_label="Close",
                                ),
                            ),
                            class_name="flex flex-col gap-0.5 px-6 pt-4 pb-2 relative",
                        ),
                        demo_form(class_name="w-full"),
                        class_name="relative isolate overflow-hidden -m-px w-full max-w-md",
                    ),
                    class_name="h-fit mt-1 overflow-hidden w-full max-w-md",
                ),
            ),
            open=rx.cond(
                DemoFormState.show_calendar,
                False,
                demo_form_open_cs.value,
            ),
            on_open_change=demo_form_open_cs.set_value,
            class_name=class_name,
            **props,
        ),
        # Calendar overlay (shows when form is complete)
        calendar_overlay(),
    )
