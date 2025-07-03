"""Base UI component."""

# Based on https://base-ui.com/

from reflex_ui.components.component import CoreComponent

PACKAGE_NAME = "@base-ui-components/react"
PACKAGE_VERSION = "^1.0.0-beta.1"


class BaseUIComponent(CoreComponent):
    """Base UI component."""

    lib_dependencies: list[str] = [f"{PACKAGE_NAME}@{PACKAGE_VERSION}"]
