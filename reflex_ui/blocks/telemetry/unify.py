"""Unify analytics tracking integration for Reflex applications."""

import json

import reflex as rx

PIXEL_SCRIPT_UNIFY: str = """
!function(){var e=["identify","page","startAutoPage","stopAutoPage","startAutoIdentify","stopAutoIdentify"];function t(o){return Object.assign([],e.reduce(function(r,n){return r[n]=function(){return o.push([n,[].slice.call(arguments)]),o},r},{}))}window.unify||(window.unify=t(window.unify)),window.unifyBrowser||(window.unifyBrowser=t(window.unifyBrowser));var n=document.createElement("script");n.async=!0,n.setAttribute("src","https://tag.unifyintent.com/v1/XAyM6RZXJzKpWH6mKPaB5S/script.js"),n.setAttribute("data-api-key","wk_DAwnkdfG_625skePqM8NZjq7jFvo6SnWFUPH2aRth"),n.setAttribute("id","unifytag"),(document.body||document.head).appendChild(n)}();"""


def get_unify_trackers() -> rx.Component:
    """Generate specific hardcoded Unify tracking components.

    Returns:
        rx.Component: The PIXEL_SCRIPT_UNIFY script component
    """
    return rx.script(PIXEL_SCRIPT_UNIFY)


def unify_identify_js(
    email: str, person_attributes: dict[str, str | int | bool] | None = None
) -> str:
    """Generate JavaScript to identify a user in Unify.

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
