"""Tailwind CSS class merging utility."""

from collections.abc import Sequence

from reflex import ImportVar
from reflex.vars import FunctionVar, Var
from reflex.vars.base import VarData

CLASS_NAME = Var[str] | str
CN_ARG = CLASS_NAME | Var[list[str]] | Sequence[CLASS_NAME]


def cn(class_1: CN_ARG, class_2: CN_ARG = "") -> Var:
    """Merge Tailwind CSS classes.

    Args:
        class_1: The first class or list of classes to merge.
        class_2: The second class or list of classes to merge (optional).

    Returns:
        Var: A Var with merged classes

    Examples:
        >>> cn("bg-red-500", rx.cond(State.is_active, "bg-blue-500", "bg-red-500"))
        >>> cn("bg-red-500", "text-white bg-blue-500")
        >>> cn("base-class")

    """
    return (
        Var(
            "cn",
            _var_data=VarData(imports={"clsx-for-tailwind": ImportVar(tag="cn")}),
        )
        .to(FunctionVar)
        .call(class_1, class_2)
        .to(str)
    )
