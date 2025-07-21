"""Custom link component."""

from typing import Literal

from reflex.components.react_router.dom import ReactRouterLink, To
from reflex.vars.base import Var

from reflex_ui.components.component import CoreComponent
from reflex_ui.components.icons.hugeicon import hi

LiteralLinkVariant = Literal["primary", "secondary"]
LiteralLinkSize = Literal["xs", "sm", "md", "lg", "xl"]


class ClassNames:
    """Class names for the link component."""

    ROOT = "font-medium underline-offset-2 hover:underline w-fit group/link relative"


LINK_VARIANTS: dict[str, dict[str, str]] = {
    "size": {
        "xs": "text-xs",
        "sm": "text-sm",
        "md": "text-md",
        "lg": "text-lg",
        "xl": "text-xl",
    },
    "variant": {
        "primary": "text-primary-11",
        "secondary": "text-secondary-11",
    },
}


class Link(ReactRouterLink, CoreComponent):
    """Link component."""

    # The size of the link. Defaults to "sm".
    size: Var[LiteralLinkSize]

    # The variant of the link. Defaults to "secondary".
    variant: Var[LiteralLinkVariant]

    # Whether to show the icon. Defaults to False.
    show_icon: Var[bool]

    # The page to link to.
    to: Var[str | To]

    @classmethod
    def create(cls, *children, **props) -> ReactRouterLink:
        """Create the link component."""
        size = props.pop("size", "sm")
        cls.validate_size(size)
        variant = props.pop("variant", "secondary")
        cls.validate_variant(variant)
        show_icon = props.pop("show_icon", False)

        # Apply default styling
        cls.set_class_name(
            f"{ClassNames.ROOT} {LINK_VARIANTS['size'][size]} {LINK_VARIANTS['variant'][variant]}",
            props,
        )

        children = list(children)
        if show_icon:
            children.append(
                hi(
                    "LinkSquare02Icon",
                    class_name="absolute top-1/2 -translate-y-1/2 right-[-1.25rem] group-hover/link:opacity-100 text-secondary-9 opacity-0",
                ),
            )

        return super().create(*children, **props)

    @staticmethod
    def validate_variant(variant: LiteralLinkVariant):
        """Validate the link variant."""
        if variant not in LINK_VARIANTS["variant"]:
            available_variants = ", ".join(LINK_VARIANTS["variant"].keys())
            message = (
                f"Invalid variant: {variant}. Available variants: {available_variants}"
            )
            raise ValueError(message)

    @staticmethod
    def validate_size(size: LiteralLinkSize):
        """Validate the link size."""
        if size not in LINK_VARIANTS["size"]:
            available_sizes = ", ".join(LINK_VARIANTS["size"].keys())
            message = f"Invalid size: {size}. Available sizes: {available_sizes}"
            raise ValueError(message)

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "size",
            "variant",
            "show_icon",
        ]


link = Link.create
