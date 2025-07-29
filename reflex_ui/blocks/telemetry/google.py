"""Google Analytics tracking integration for Reflex applications."""

import reflex as rx

# Google Tag Manager script template
GTAG_SCRIPT_TEMPLATE: str = """
window.dataLayer = window.dataLayer || [];
function gtag() {{
    window.dataLayer.push(arguments);
}}
gtag('js', new Date());
gtag('config', '{tracking_id}');
"""

# Google Tag Manager script URL template
GTAG_SCRIPT_URL_TEMPLATE: str = (
    "https://www.googletagmanager.com/gtag/js?id={tracking_id}"
)


def get_google_analytics_trackers(
    tracking_id: str,
) -> list[rx.Component]:
    """Generate Google Analytics tracking components for a Reflex application.

    Args:
        tracking_id: Google Analytics tracking ID (defaults to app's tracking ID)

    Returns:
        list[rx.Component]: Script components needed for Google Analytics tracking
    """
    # Load Google Tag Manager script
    return [
        rx.script(src=GTAG_SCRIPT_URL_TEMPLATE.format(tracking_id=tracking_id)),
        rx.script(GTAG_SCRIPT_TEMPLATE.format(tracking_id=tracking_id)),
    ]
