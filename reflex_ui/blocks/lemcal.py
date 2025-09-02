"""Lemcal booking integration for Reflex applications."""

from typing import Any

import reflex as rx

LEMCAL_SCRIPT_URL = "https://cdn.lemcal.com/lemcal-integrations.min.js"


def get_lemcal_script() -> rx.Component:
    """Generate Lemcal script component for a Reflex application.

    Returns:
        rx.Component: Script component needed for Lemcal integration
    """
    return rx.el.script(
        src=LEMCAL_SCRIPT_URL,
        defer=True,
    )


def lemcal_button(
    child: rx.Component | None = None,
    label: str = "Book a Demo",
    class_name: str = "",
    user_id: str = "usr_8tiwtJ8nEJaFj2qH9",
    meeting_type: str = "met_ToQQ9dLZDYrEBv5qz",
    **props: Any,
) -> rx.Component:
    """Reusable Lemcal embed button wrapper.

    Wraps provided child (or a default button) in a div with the Lemcal
    integration class and data attributes so that the external script can
    attach the booking behavior.

    Args:
        child: Custom component to wrap (defaults to a button with label)
        label: Default button text if no child provided
        class_name: Additional CSS classes to apply
        user_id: Lemcal user ID for booking integration
        meeting_type: Lemcal meeting type ID for booking integration
        **props: Additional props to pass to the wrapper div

    Returns:
        rx.Component: Lemcal button wrapper component
    """
    content = child if child is not None else rx.el.button(label)
    return rx.el.div(
        content,
        class_name=("lemcal-embed-button " + class_name).strip(),
        custom_attrs={
            "data-user": user_id,
            "data-meeting-type": meeting_type,
        },
        **props,
    )


def lemcal_calendar(
    user_id: str = "usr_8tiwtJ8nEJaFj2qH9",
    meeting_type: str = "met_ToQQ9dLZDYrEBv5qz",
    class_name: str = "",
    refresh_on_mount: bool = True,
    **props: Any,
) -> rx.Component:
    """Lemcal booking calendar embed component.

    Creates a div with the Lemcal calendar integration class and data attributes.
    Optionally refreshes the Lemcal integration when the component mounts.

    Args:
        user_id: Lemcal user ID for booking integration
        meeting_type: Lemcal meeting type ID for booking integration
        class_name: Additional CSS classes to apply
        refresh_on_mount: Whether to call window.lemcal.refresh() on mount
        **props: Additional props to pass to the wrapper div

    Returns:
        rx.Component: Lemcal calendar embed component
    """
    calendar_props = {
        "class_name": ("lemcal-embed-booking-calendar " + class_name).strip(),
        "custom_attrs": {
            "data-user": user_id,
            "data-meeting-type": meeting_type,
        },
        **props,
    }

    if refresh_on_mount:
        calendar_props["on_mount"] = rx.call_function("window.lemcal.refresh")

    return rx.el.div(**calendar_props)
