"""Utilities for rendering iterables."""

import inspect
from collections.abc import Callable, Iterable
from typing import Any

from reflex.vars.base import LiteralVar, Var
from reflex.vars.sequence import ArrayVar


class IterableListVarError(TypeError):
    """Raised when the iterable type is invalid."""


class IterableListRenderError(TypeError):
    """Raised when there is an error with the render function."""


def iterable_list(
    iterable: Var[Iterable] | Iterable,
    render_fn: Callable,
) -> Var:
    """Create a .map() expression that renders a list of components.

    Generates: items.map((item) => <Component />)

    Use this for standard list rendering where all items are rendered immediately.
    For React render props (function children), use function_child() instead.

    Args:
        iterable: The iterable to create components from.
        render_fn: A function that takes (item) or (item, index) and returns a component.

    Returns:
        A Var containing the .map() expression.

    Raises:
        IterableListVarError: If the iterable type is invalid.
        IterableListRenderError: If the render function signature is invalid.

    """
    from reflex.vars import ObjectVar, StringVar

    # Convert to Var if needed
    iterable_var = (
        LiteralVar.create(iterable).guess_type()
        if not isinstance(iterable, Var)
        else iterable.guess_type()
    )

    # Convert special types to arrays
    if isinstance(iterable_var, ObjectVar):
        iterable_var = iterable_var.entries()  # Convert object to [key, value] pairs
    elif isinstance(iterable_var, StringVar):
        iterable_var = iterable_var.split()  # Convert string to array of characters

    # Validate we have an array
    if not isinstance(iterable_var, ArrayVar):
        msg = f"Could not iterate over var `{iterable_var!s}` of type {iterable_var._var_type}."
        raise IterableListVarError(msg)

    # Inspect render function signature
    render_sig = inspect.signature(render_fn)
    params = list(render_sig.parameters.values())

    # Must accept 1 param (item) or 2 params (item, index)
    if len(params) == 0 or len(params) > 2:
        msg = (
            f"Expected 1 or 2 parameters in render function, got "
            f"{[p.name for p in params]}."
        )
        raise IterableListRenderError(msg)

    # Extract parameter names from function signature
    arg_name = params[0].name if len(params) >= 1 else "item"
    index_name = params[1].name if len(params) == 2 else None

    # Create Var objects representing the loop variables
    arg_var = Var(_js_expr=arg_name, _var_type=Any)

    # Call render function to build the component template
    if len(params) == 1:
        component = render_fn(arg_var)
    else:
        index_var = Var(_js_expr=index_name or "index", _var_type=int)
        component = render_fn(arg_var, index_var)

    # Convert component to JSX string
    from reflex.compiler.compiler import _into_component_once

    component = _into_component_once(component)

    if component is None:
        msg = "The render function must return a component."
        raise IterableListRenderError(msg)

    # Build the .map() expression
    if index_name:
        map_expr = f"{iterable_var}.map(({arg_name}, {index_name}) => {component})"
    else:
        map_expr = f"{iterable_var}.map(({arg_name}) => {component})"

    return Var(_js_expr=map_expr, _var_type=list)


def function_child(
    render_fn: Callable,
) -> Var:
    """Create a function child for React render prop patterns.

    Generates: (item) => <Component />

    This is specifically for components that expect a function child (render prop),
    such as Base UI's Combobox.List, which filters items dynamically by calling
    this function only for matching items.

    The difference from iterable_list():
    - function_child(): Returns a function that the component calls
    - iterable_list(): Returns an array by immediately calling .map()

    Args:
        render_fn: A function that takes (item) or (item, index) and returns a component.

    Returns:
        A Var containing the function expression (not a .map() call).

    Raises:
        IterableListRenderError: If the render function signature is invalid.
    """
    # Inspect render function signature
    render_sig = inspect.signature(render_fn)
    params = list(render_sig.parameters.values())

    # Must accept 1 param (item) or 2 params (item, index)
    if len(params) == 0 or len(params) > 2:
        msg = (
            f"Expected 1 or 2 parameters in render function, got "
            f"{[p.name for p in params]}."
        )
        raise IterableListRenderError(msg)

    # Extract parameter names from function signature
    arg_name = params[0].name if len(params) >= 1 else "item"
    index_name = params[1].name if len(params) == 2 else None

    # Create Var objects representing the function parameters
    arg_var = Var(_js_expr=arg_name, _var_type=Any)

    # Call render function to build the component template
    if len(params) == 1:
        component = render_fn(arg_var)
    else:
        index_var = Var(_js_expr=index_name or "index", _var_type=int)
        component = render_fn(arg_var, index_var)

    # Convert component to JSX string
    from reflex.compiler.compiler import _into_component_once

    component = _into_component_once(component)

    if component is None:
        msg = "The render function must return a component."
        raise IterableListRenderError(msg)

    # Build just the function expression (no .map() call)
    # This lets the parent component control when/how to call it
    if index_name:
        func_expr = f"({arg_name}, {index_name}) => {component}"
    else:
        func_expr = f"({arg_name}) => {component}"

    return Var(_js_expr=func_expr, _var_type=Any)
