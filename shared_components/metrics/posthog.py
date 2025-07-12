from typing import Any
import httpx
from pydantic import BaseModel
from shared_components import constants

class DemoEvent(BaseModel):
    distinct_id: str
    thread_id: str
    tier_type: str
    first_name: str
    last_name: str
    email: str
    company_email: str
    linkedin_url: str
    job_title: str
    company_name: str
    num_employees: str
    internal_tools: str
    referral_source: str

async def send_data_to_posthog(event_instance: DemoEvent):
    event_data = {
        "api_key": constants.POSTHOG_API_KEY,
        "event": event_instance.__class__.__name__,
        "properties": event_instance.dict(),
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://app.posthog.com/capture/", json=event_data
            )
            response.raise_for_status()
    except Exception as e:
        # In a real scenario, you might want to log this error more robustly
        print(f"Error sending data to PostHog: {e}")