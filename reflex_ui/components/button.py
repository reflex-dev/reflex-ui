"""Custom button component."""

from typing import Literal

from reflex.components.component import Component
from reflex.components.core.cond import cond
from reflex.components.el import Button as BaseButton
from reflex.vars import Var

from .base.core_component import CoreComponent
from .icons.icon import spinner

LiteralButtonVariant = Literal[
    "primary", "destructive", "outline", "secondary", "ghost", "link", "dark"
]
LiteralButtonSize = Literal["xs", "sm", "md", "lg", "icon"]

DEFAULT_CLASS_NAME = "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-colors disabled:cursor-not-allowed disabled:border disabled:border-secondary-4/80 disabled:bg-secondary-3 disabled:text-secondary-8 shrink-0 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 text-medium cursor-pointer box-border"

BUTTON_VARIANTS = {
    "variant": {
        "primary": "bg-primary-9 text-white hover:bg-primary-10",
        "destructive": "bg-destructive-9 hover:bg-destructive-10 text-white",
        "outline": "border border-secondary-5/80 hover:bg-border-secondary-6/80 bg-secondary-1 hover:bg-secondary-3 text-secondary-12",
        "secondary": "bg-secondary-4 text-secondary-12 hover:bg-secondary-5",
        "ghost": "hover:bg-secondary-3 text-secondary-12",
        "link": "text-secondary-12 underline-offset-4 hover:underline",
        "dark": "bg-secondary-12 text-secondary-1 hover:bg-secondary-12/80",
    },
    "size": {
        "xs": "px-1.5 h-7 rounded-sm gap-1.5",
        "sm": "px-2 h-8 rounded-lg gap-2",
        "md": "px-2.5 h-9 rounded-lg gap-2",
        "lg": "px-3 h-10 rounded-xl gap-2.5",
        "xl": "px-3.5 h-12 rounded-2xl gap-3",
        "icon-xs": "size-7 rounded-md",
        "icon-sm": "size-8 rounded-md",
        "icon-md": "size-9 rounded-lg",
        "icon-lg": "size-10 rounded-xl",
        "icon-xl": "size-12 rounded-2xl",
    },
}


class Button(BaseButton, CoreComponent):
    """A custom button component."""

    # Button variant
    variant: Var[LiteralButtonVariant] = "primary"

    # Button size
    size: Var[LiteralButtonSize] = "md"

    # The loading state of the button
    loading: Var[bool] = False

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Create the button component."""
        variant = props.pop("variant", "primary")
        cls.validate_variant(variant)

        size = props.pop("size", "md")
        cls.validate_size(size)

        loading = props.pop("loading", False)
        disabled = props.pop("disabled", False)

        button_classes = f"{DEFAULT_CLASS_NAME} {BUTTON_VARIANTS['variant'][variant]} {BUTTON_VARIANTS['size'][size]}"

        cls.set_class_name(button_classes, props)

        children_list = list(children)

        if isinstance(loading, Var):
            props["disabled"] = cond(loading, True, disabled)
            children_list.insert(0, cond(loading, spinner()))
        else:
            props["disabled"] = True if loading else disabled
            children_list.insert(0, spinner()) if loading else None

        return super().create(*children_list, **props)

    @staticmethod
    def validate_variant(variant: LiteralButtonVariant):
        if variant not in BUTTON_VARIANTS["variant"]:
            raise ValueError(
                f"Invalid variant: {variant}. Available variants: {', '.join(BUTTON_VARIANTS['variant'].keys())}"
            )

    @staticmethod
    def validate_size(size: LiteralButtonSize):
        if size not in BUTTON_VARIANTS["size"]:
            raise ValueError(
                f"Invalid size: {size}. Available sizes: {', '.join(BUTTON_VARIANTS['size'].keys())}"
            )

    def _exclude_props(self) -> list[str]:
        return [
            *super()._exclude_props(),
            "size",
            "variant",
            "loading",
        ]


button = Button.create
