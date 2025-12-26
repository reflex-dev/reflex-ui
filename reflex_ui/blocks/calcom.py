"""Cal.com integration components for Reflex UI."""

import os

import reflex as rx

DEFAULT_CAL_NAMESPACE = os.getenv("DEFAULT_CAL_NAMESPACE", "reflex-intro-call")

DEFAULT_CAL_LINK = os.getenv("DEFAULT_CAL_LINK", "team/reflex/reflex-intro-call")


def get_cal_attrs(
    cal_namespace: str = DEFAULT_CAL_NAMESPACE,
    cal_link: str = DEFAULT_CAL_LINK,
    config: str | rx.Var[str] | None = '{"theme": "dark", "layout": "month_view"}',
    **kwargs,
):
    """Get Cal.com attributes for embedding.

    Args:
        cal_namespace: The Cal.com namespace
        cal_link: The Cal.com form link
        config: Cal.com configuration dict including theme, layout, name, email, etc.
        **kwargs: Additional attributes to include

    Returns:
        Dictionary of Cal.com attributes
    """
    attrs = {
        "data-cal-link": cal_link,
        "data-cal-namespace": cal_namespace,
        "data-cal-config": config,
    }
    attrs.update(kwargs)
    return attrs


class CalcomPopupEmbed(rx.Fragment):
    """Cal.com popup embed component using React hooks."""

    def add_imports(self) -> rx.ImportDict:
        """Add required imports for Cal.com embed.

        Returns:
            Dictionary of imports needed for the component
        """
        return {
            "react": rx.ImportVar("useEffect"),
            "@calcom/embed-react@1.5.3": rx.ImportVar("getCalApi"),
        }

    def add_hooks(self) -> list[str | rx.Var[object]]:
        """Add React hooks for Cal.com API initialization.

        Returns:
            List of hook code strings to initialize Cal.com
        """
        return [
            """
useEffect(() => {
  (async function () {
    const cal = await getCalApi({ namespace: "reflex-intro-call" });
    cal("ui", {
      hideEventTypeDetails: false,
      layout: "month_view",
      styles: {
        branding: { brandColor: "#6F56CF" },
      },
    });
  })();
}, []);
""",
        ]


calcom_popup_embed = CalcomPopupEmbed.create


class CalEmbed(rx.Component):
    """Cal.com embed component using the Cal React component."""

    library = "@calcom/embed-react@1.5.3"
    tag = "Cal"
    is_default = True

    cal_link: rx.Var[str]

    namespace: rx.Var[str]

    config: rx.Var[dict]

    @classmethod
    def create(
        cls,
        cal_link: str = DEFAULT_CAL_LINK,
        cal_namespace: str = DEFAULT_CAL_NAMESPACE,
        config: rx.Var[dict] | dict | None = None,
        **props,
    ):
        """Create a Cal.com embed component.

        Args:
            cal_link: The Cal.com link (e.g., "team/reflex/reflex-intro-call")
            cal_namespace: The namespace for the Cal.com embed
            config: Configuration object for Cal.com including prefill data.
                   According to https://cal.com/help/embedding/prefill-booking-form-embed
                   you can prefill: name, email, notes, and location.
                   Example: {"layout": "month_view", "name": "John Doe", "email": "[email protected]", "notes": "Company details..."}
            **props: Additional props to pass to the component
        """
        return super().create(
            cal_link=cal_link,
            namespace=cal_namespace,
            config=config,
            **props,
        )


cal_embed = CalEmbed.create
