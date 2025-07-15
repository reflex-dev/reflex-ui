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


@memo
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


@memo
def arrow_svg_component(class_name: str | Var[str] = "") -> Component:
    """Create a tooltip arrow SVG icon.

    The arrow SVG icon.
    """
    return svg(
        svg.path(
            d="M9.66437 2.60207L4.80758 6.97318C4.07308 7.63423 3.11989 8 2.13172 8H0V9H20V8H18.5349C17.5468 8 16.5936 7.63423 15.8591 6.97318L11.0023 2.60207C10.622 2.2598 10.0447 2.25979 9.66437 2.60207Z",
            class_name=cn("fill-secondary-12", class_name),
        ),
        svg.path(
            d="M10.3333 3.34539L5.47654 7.71648C4.55842 8.54279 3.36693 9 2.13172 9H0V8H2.13172C3.11989 8 4.07308 7.63423 4.80758 6.97318L9.66437 2.60207C10.0447 2.25979 10.622 2.2598 11.0023 2.60207L15.8591 6.97318C16.5936 7.63423 17.5468 8 18.5349 8H20V9H18.5349C17.2998 9 16.1083 8.54278 15.1901 7.71648L10.3333 3.34539Z",
            class_name="fill-none",
        ),
        width="20",
        height="10",
        xmlns="http://www.w3.org/2000/svg",
        custom_attrs={"viewBox": "0 0 20 10"},
        fill="none",
    )


arrow_svg = arrow_svg_component
