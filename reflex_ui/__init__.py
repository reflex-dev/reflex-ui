"""Reflex UI package."""

from reflex.utils import lazy_loader

_REFLEX_UI_MAPPING = {
    "components.base.avatar": ["avatar"],
    "components.base.badge": ["badge"],
    "components.base.button": ["button"],
    "components.base.checkbox": ["checkbox"],
    "components.base.scroll_area": ["scroll_area"],
    "components.base.select": ["select"],
    "components.base.skeleton": ["skeleton"],
    "components.base.slider": ["slider"],
    "components.base.switch": ["switch"],
    "components.base.theme_switcher": ["theme_switcher"],
    "components.base.tooltip": ["tooltip"],
}

_SUBMODULES = {"components", "utils"}
_SUBMOD_ATTRS = {
    **_REFLEX_UI_MAPPING,
    "components": ["base"],
    "components.icons.hugeicon": ["hi", "icon"],
    "components.icons.others": ["spinner"],
    "utils.twmerge": ["cn"],
}

getattr, __dir__, __all__ = lazy_loader.attach(
    __name__,
    submodules=_SUBMODULES,
    submod_attrs=_SUBMOD_ATTRS,
)


def __getattr__(name: str):
    return getattr(name)
