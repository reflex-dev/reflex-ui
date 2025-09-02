"""Lemcal booking integration for Reflex applications."""

import reflex as rx
from typing import Any

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
