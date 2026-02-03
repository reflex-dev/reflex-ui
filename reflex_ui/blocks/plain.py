"""Plain chat integration for customer support.

This module provides integration with Plain.com chat widget for live customer support.
"""

import reflex as rx

PLAIN_INIT_SCRIPT = """
(function(d, script) {{
  script = d.createElement('script');
  script.async = false;
  script.onload = function(){{
    Plain.init({{
      appId: 'liveChatApp_01KGG4JD5JHG8JY8X5CCN7811V',
      hideLauncher: {hide_launcher},
      hideBranding: true,
      theme: 'auto',
    }});
  }};
  script.src = 'https://chat.cdn-plain.com/index.js';
  d.getElementsByTagName('head')[0].appendChild(script);
}}(document));
"""


def open_plain_chat() -> rx.event.EventSpec:
    """Open the Plain chat widget.

    Returns:
        An event spec that opens the Plain chat interface when triggered.
    """
    return rx.call_script(
        "try { Plain.open(); } catch (e) { console.error('Plain chat not available:', e); }"
    )


def get_plain_script(hide_launcher: bool = True) -> rx.Component:
    """Get the Plain chat initialization script component.

    Args:
        hide_launcher: Whether to hide the default Plain chat launcher button. Defaults to True.

    Returns:
        A Reflex script component that initializes the Plain chat widget.
    """
    return rx.script(PLAIN_INIT_SCRIPT.format(hide_launcher=str(hide_launcher).lower()))
