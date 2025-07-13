import os

# URLs
REFLEX_URL = "https://reflex.dev"
DEMO_VIDEO_URL = "https://www.youtube.com/watch?v=s-kr8v7827g"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# PostHog
POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY", "")

# Banned Email DOmains
BANNED_EMAIL_DOMAINS = {
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
