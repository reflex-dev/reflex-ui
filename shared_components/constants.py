import os

# URLs
REFLEX_URL = "https://reflex.dev"
DEMO_VIDEO_URL = "https://www.youtube.com/watch?v=s-kr8v7827g"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# PostHog
POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY", "")
