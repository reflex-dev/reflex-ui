"""Set of custom icons."""

from reflex.components.component import Component, memo
from reflex.components.el import svg
from reflex.vars.base import Var

from reflex_ui.utils.twmerge import cn


@memo
def spinner_component(
    class_name: str | Var[str] = "",
) -> Component:
    """Create a spinner SVG icon.

    Args:
        class_name: The class name of the spinner.

    Returns:
        The spinner SVG icon.

    """
    return svg(
        svg.path(
            opacity="0.2",
            d="M14.66 8a6.666 6.666 0 1 1-13.333 0 6.666 6.666 0 0 1 13.333 0Z",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        svg.path(
            d="M13.413 11.877A6.666 6.666 0 1 1 10.26 1.728",
            stroke="currentColor",
            stroke_width="1.5",
        ),
        xmlns="http://www.w3.org/2000/svg",
        custom_attrs={"viewBox": "0 0 16 16"},
        class_name=cn("animate-spin size-4 fill-none", class_name),
    )


spinner = spinner_component


def select_arrow_icon(
    class_name: str | Var[str] = "",
) -> Component:
    """A select arrow SVG icon."""
    return svg(
        svg.path(
            d="M4.99902 10.0003L7.99967 13.0003L10.999 10.0003M4.99902 6.00033L7.99967 3.00033L10.999 6.00033",
            stroke="currentColor",
            stroke_width="1.5",
            stroke_linecap="round",
            stroke_linejoin="round",
        ),
        xmlns="http://www.w3.org/2000/svg",
        custom_attrs={"viewBox": "0 0 16 16"},
        class_name=cn("size-4 fill-none", class_name),
    )


select_arrow = select_arrow_icon
