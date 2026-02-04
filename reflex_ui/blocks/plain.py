"""Plain chat integration for customer support.

This module provides integration with Plain.com chat widget for live customer support.
See: https://plain.support.site/article/chat-customization
"""

import os
from typing import Any

import reflex as rx
from reflex.components.tags.tag import Tag

PLAIN_APP_ID = os.getenv("PLAIN_APP_ID", "liveChatApp_01KGG4JD5JHG8JY8X5CCN7811V")


class PlainChat(rx.Component):
    """Plain chat widget component."""

    tag = "PlainChat"

    full_name: rx.Var[str]
    short_name: rx.Var[str]
    chat_avatar_url: rx.Var[str]
    external_id: rx.Var[str]
    hide_launcher: rx.Var[bool] = rx.Var.create(True)

    # Optional email authentication
    email: rx.Var[str] = rx.Var.create("")
    email_hash: rx.Var[str] = rx.Var.create("")

    # Optional built-in email verification
    require_authentication: rx.Var[bool] = rx.Var.create(False)

    def add_imports(self) -> dict:
        """Add React imports."""
        return {"react": ["useEffect"]}

    def add_hooks(self) -> list[str | rx.Var]:
        """Add hooks to initialize Plain chat widget."""
        return [
            rx.Var(
                f"""useEffect(() => {{
  const script = document.createElement('script');
  script.async = false;
  script.src = 'https://chat.cdn-plain.com/index.js';
  script.onload = () => {{
    Plain.init({{
      appId: '{PLAIN_APP_ID}',
      hideLauncher: {self.hide_launcher!s},
      hideBranding: true,
      theme: 'auto',
      customerDetails: {{
        fullName: {self.full_name!s},
        shortName: {self.short_name!s},
        chatAvatarUrl: {self.chat_avatar_url!s},
        email: {self.email!s},
        emailHash: {self.email_hash!s},
      }},
      threadDetails: {{
        externalId: {self.external_id!s},
      }},
      requireAuthentication: {self.require_authentication!s},
    }});
  }};
  document.head.appendChild(script);
}}, [])"""
            )
        ]

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        """Render empty tag."""
        return Tag("")


plain_chat = PlainChat.create


def open_plain_chat() -> rx.event.EventSpec:
    """Open the Plain chat widget."""
    return rx.call_script(
        "try { Plain.open(); } catch (e) { console.error('Plain chat not available:', e); }"
    )
