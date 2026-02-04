"""Plain chat integration for customer support.

This module provides integration with Plain.com chat widget for live customer support.
See: https://plain.support.site/article/chat-customization
"""

from typing import Any

import reflex as rx
from reflex.components.tags.tag import Tag

PLAIN_APP_ID = "liveChatApp_01KGG4JD5JHG8JY8X5CCN7811V"


class PlainChat(rx.Component):
    """Plain chat widget component.

    See: https://plain.support.site/article/live-chat-authentication

    Note: If you provide email, you MUST also provide email_hash.
    The hash must be generated server-side using HMAC-SHA256 with your Plain secret.
    """

    tag = "PlainChat"

    # Customer details (all optional)
    full_name: rx.Var[str] = rx.Var.create("")
    short_name: rx.Var[str] = rx.Var.create("")
    chat_avatar_url: rx.Var[str] = rx.Var.create("")
    email: rx.Var[str] = rx.Var.create("")
    email_hash: rx.Var[str] = rx.Var.create("")

    # Thread details (optional)
    external_id: rx.Var[str] = rx.Var.create("")

    # Options
    hide_launcher: rx.Var[bool] = rx.Var.create(True)
    require_authentication: rx.Var[bool] = rx.Var.create(False)

    def add_hooks(self) -> list[str | rx.Var]:
        """Add hooks to initialize Plain chat widget."""
        return [
            rx.Var(
                f"""const PlainChatComponent = (() => {{
  // Load Plain chat script
  const script = document.createElement('script');
  script.async = false;
  script.src = 'https://chat.cdn-plain.com/index.js';
  script.onload = function() {{
    // Build customer details, only including non-empty values
    const customerDetails = {{}};
    if ({self.full_name!s}) customerDetails.fullName = {self.full_name!s};
    if ({self.short_name!s}) customerDetails.shortName = {self.short_name!s};
    if ({self.chat_avatar_url!s}) customerDetails.chatAvatarUrl = {self.chat_avatar_url!s};
    if ({self.email!s}) customerDetails.email = {self.email!s};
    if ({self.email_hash!s}) customerDetails.emailHash = {self.email_hash!s};

    // Build thread details, only including non-empty values
    const threadDetails = {{}};
    if ({self.external_id!s}) threadDetails.externalId = {self.external_id!s};

    // Build init options
    const initOptions = {{
      appId: '{PLAIN_APP_ID}',
      hideLauncher: {self.hide_launcher!s},
      hideBranding: true,
      theme: 'auto',
    }};

    if ({self.require_authentication!s}) initOptions.requireAuthentication = true;
    if (Object.keys(customerDetails).length > 0) initOptions.customerDetails = customerDetails;
    if (Object.keys(threadDetails).length > 0) initOptions.threadDetails = threadDetails;

    Plain.init(initOptions);
  }};
  document.head.appendChild(script);
  return null;
}})()"""
            )
        ]

    def _render(self, props: dict[str, Any] | None = None) -> Tag:
        return Tag("")


plain_chat = PlainChat.create


def open_plain_chat() -> rx.event.EventSpec:
    """Open the Plain chat widget.

    Returns:
        An event spec that opens the Plain chat interface when triggered.
    """
    return rx.call_script(
        "try { Plain.open(); } catch (e) { console.error('Plain chat not available:', e); }"
    )
