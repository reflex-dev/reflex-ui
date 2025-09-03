import reflex as rx


def lemcal_calendar(**props) -> rx.Component:
    return rx.el.div(
        class_name="lemcal-embed-booking-calendar",
        data_user="usr_8tiwtJ8nEJaFj2qH9",
        data_meeting_type="met_EHtPvmZoKE4SFk4kZ",
        **props,
    )


def lemcal_script(**props) -> rx.Component:
    return rx.script(
        src="https://cdn.lemcal.com/lemcal-integrations.min.js",
        defer=True,
        **props,
    )
