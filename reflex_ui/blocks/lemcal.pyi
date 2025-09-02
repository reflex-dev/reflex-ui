"""Lemcal booking integration for Reflex applications."""

from typing import Any

import reflex as rx

def get_lemcal_script() -> rx.Component: ...
def lemcal_button(
    child: rx.Component | None = ...,
    label: str = ...,
    class_name: str = ...,
    user_id: str = ...,
    meeting_type: str = ...,
    **props: Any,
) -> rx.Component: ...
def lemcal_calendar(
    user_id: str = ...,
    meeting_type: str = ...,
    class_name: str = ...,
    refresh_on_mount: bool = ...,
    **props: Any,
) -> rx.Component: ...
