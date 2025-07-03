"""Custom skeleton component."""

from reflex.components.component import Component, memo
from reflex.components.el import Div
from reflex.vars import Var

from reflex_ui.utils.twmerge import cn


class ClassNames:
    """Class names for skeleton component."""

    ROOT = "animate-pulse bg-secondary-6"


@memo
def skeleton_component(
    class_name: str | Var[str] = "",
) -> Component:
    """Skeleton component."""
    return Div.create(class_name=cn(ClassNames.ROOT, class_name))


skeleton = skeleton_component
