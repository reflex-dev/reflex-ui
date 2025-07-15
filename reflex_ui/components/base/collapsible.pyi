"""Type stubs for collapsible component."""

from typing import Any, Literal

from reflex.components.component import Component, ComponentNamespace
from reflex.event import EventType
from reflex.vars.base import Var

from reflex_ui.components.base_ui import BaseUIComponent

class ClassNames:
    ROOT: str
    TRIGGER: str
    PANEL: str

class CollapsibleBaseComponent(BaseUIComponent):
    library: str
    @property
    def import_var(self): ...

class CollapsibleRoot(CollapsibleBaseComponent):
    tag: str
    default_open: Var[bool]
    open: Var[bool]
    on_open_change: EventType[bool]
    disabled: Var[bool]
    @classmethod
    def create(
        cls,
        *children,
        default_open: bool | Var[bool] | None = None,
        open: bool | Var[bool] | None = None,
        on_open_change: EventType[bool] | None = None,
        disabled: bool | Var[bool] | None = None,
        **props,
    ) -> CollapsibleRoot: ...

class CollapsibleTrigger(CollapsibleBaseComponent):
    tag: str
    native_button: Var[bool]
    render_: Var[Component]
    @classmethod
    def create(
        cls,
        *children,
        native_button: bool | Var[bool] | None = None,
        render_: Component | Var[Component] | None = None,
        **props,
    ) -> CollapsibleTrigger: ...

class CollapsiblePanel(CollapsibleBaseComponent):
    tag: str
    hidden_until_found: Var[bool]
    class_name: Var[str]
    keep_mounted: Var[bool]
    render_: Var[Component]
    @classmethod
    def create(
        cls,
        *children,
        hidden_until_found: bool | Var[bool] | None = None,
        class_name: str | Var[str] | None = None,
        keep_mounted: bool | Var[bool] | None = None,
        render_: Component | Var[Component] | None = None,
        **props,
    ) -> CollapsiblePanel: ...

class HighLevelCollapsible(CollapsibleRoot):
    trigger: Var[Component | None]
    content: Var[str | Component | None]
    @classmethod
    def create(
        cls,
        *children,
        trigger: Component | Var[Component] | None = None,
        content: str | Component | Var[str | Component] | None = None,
        default_open: bool | Var[bool] | None = None,
        open: bool | Var[bool] | None = None,
        on_open_change: EventType[bool] | None = None,
        disabled: bool | Var[bool] | None = None,
        **props,
    ) -> HighLevelCollapsible: ...

class Collapsible(ComponentNamespace):
    root: staticmethod
    trigger: staticmethod
    panel: staticmethod
    __call__: staticmethod

collapsible: Collapsible
