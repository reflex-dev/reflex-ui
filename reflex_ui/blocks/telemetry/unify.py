"""Unify analytics tracking integration for Reflex applications."""

import json
import os

import httpx
import reflex as rx

# Unify API configuration
UNIFY_API_KEY = os.getenv("UNIFY_API_KEY", "")
UNIFY_API_BASE_URL = "https://api.unifygtm.com/data/v1"

PIXEL_SCRIPT_UNIFY: str = """
!function(){var e=["identify","page","startAutoPage","stopAutoPage","startAutoIdentify","stopAutoIdentify"];function t(o){return Object.assign([],e.reduce(function(r,n){return r[n]=function(){return o.push([n,[].slice.call(arguments)]),o},r},{}))}window.unify||(window.unify=t(window.unify)),window.unifyBrowser||(window.unifyBrowser=t(window.unifyBrowser));var n=document.createElement("script");n.async=!0,n.setAttribute("src","https://tag.unifyintent.com/v1/XAyM6RZXJzKpWH6mKPaB5S/script.js"),n.setAttribute("data-api-key","wk_DAwnkdfG_625skePqM8NZjq7jFvo6SnWFUPH2aRth"),n.setAttribute("id","unifytag"),(document.body||document.head).appendChild(n)}();"""


def get_unify_trackers() -> rx.Component:
    """Generate specific hardcoded Unify tracking components.

    Returns:
        rx.Component: The PIXEL_SCRIPT_UNIFY script component
    """
    return rx.script(PIXEL_SCRIPT_UNIFY)


async def upsert_unify_person(
    email: str,
    first_name: str | None = None,
    last_name: str | None = None,
    company_name: str | None = None,
    job_title: str | None = None,
    lead_source: str | None = None,
    num_employees: str | None = None,
    additional_attributes: dict[str, str | int | bool] | None = None,
) -> dict | None:
    """Create or update a person record in Unify via the Data API.

    Args:
        email: The user's email address (required, used as unique identifier)
        first_name: The user's first name
        last_name: The user's last name
        company_name: The user's company name
        job_title: The user's job title
        lead_source: How the user found us (e.g., "Demo Form")
        num_employees: Number of employees at the company
        additional_attributes: Any additional attributes to store

    Returns:
        dict: The API response data, or None if the request failed
    """
    if not UNIFY_API_KEY:
        print("Warning: UNIFY_API_KEY not set, skipping Unify API call")
        return None

    # Build the record data
    record_data: dict[str, str | int | bool] = {
        "email": email,
        "demo_request": True,
    }

    if first_name:
        record_data["first_name"] = first_name
    if last_name:
        record_data["last_name"] = last_name
    if lead_source:
        record_data["lead_source"] = lead_source
    if additional_attributes:
        record_data.update(additional_attributes)

    # Add company info to notes or a custom field if available
    notes_parts = []
    if company_name:
        notes_parts.append(f"Company: {company_name}")
    if job_title:
        notes_parts.append(f"Job Title: {job_title}")
    if num_employees:
        notes_parts.append(f"Employees: {num_employees}")

    headers = {
        "x-api-key": UNIFY_API_KEY,
        "Content-Type": "application/json",
    }

    try:
        async with httpx.AsyncClient() as client:
            # Use upsert endpoint to create or update based on email
            response = await client.post(
                f"{UNIFY_API_BASE_URL}/objects/person/records",
                json=record_data,
                headers=headers,
                timeout=10.0,
            )

            if response.status_code in (200, 201):
                return response.json()
            else:
                print(f"Unify API error: {response.status_code} - {response.text}")
                return None

    except Exception as e:
        print(f"Unify API request failed: {e}")
        return None


def unify_identify_js(
    email: str, person_attributes: dict[str, str | int | bool] | None = None
) -> str:
    """Generate JavaScript to identify a user in Unify (client-side fallback).

    Args:
        email: The user's email address (required)
        person_attributes: Optional dictionary of person attributes (status, etc.)

    Returns:
        str: JavaScript code to identify the user in Unify
    """
    # Escape the email to prevent XSS
    escaped_email = email.replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')

    # Build the person object - email is always required
    person_obj = {"email": email}
    if person_attributes:
        person_obj.update(person_attributes)

    # Convert to JSON string
    person_json = json.dumps({"person": person_obj})

    return f"""
    if (window.unify && window.unify.identify) {{
        window.unify.identify('{escaped_email}', {person_json});
    }}
    """
