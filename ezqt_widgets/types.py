# ///////////////////////////////////////////////////////////////
# TYPES - Type Aliases Module
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Type aliases module for ezqt_widgets.

This module centralizes common type aliases used throughout the library
to improve code readability, maintainability, and type safety.

Example:
    >>> from ezqt_widgets.types import IconSource, SizeType
    >>> from PySide6.QtGui import QIcon
    >>>
    >>> def create_icon(source: IconSource) -> QIcon:
    ...     # Use the type alias
    ...     pass
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from collections.abc import Callable
from typing import Any, TypeAlias

# Third-party imports
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QIcon, QPixmap
from PySide6.QtWidgets import QWidget

# ///////////////////////////////////////////////////////////////
# TYPE ALIASES
# ///////////////////////////////////////////////////////////////

# ------------------------------------------------
# Icon Types
# ------------------------------------------------

IconSource: TypeAlias = QIcon | str | None
"""Type alias for icon sources.

Accepts:
    - QIcon: A Qt icon object
    - str: Path to an icon file (local path, resource path, or URL)
    - None: No icon

Used by: IconButton, DateButton, LoaderButton, etc.
"""

IconSourceExtended: TypeAlias = QIcon | QPixmap | str | None
"""Type alias for extended icon sources (includes QPixmap).

Accepts:
    - QIcon: A Qt icon object
    - QPixmap: A Qt pixmap object
    - str: Path to an icon file (local path, resource path, or URL)
    - None: No icon

Used by: ToggleIcon, HoverLabel, and other widgets that support QPixmap.
"""

# ------------------------------------------------
# Size Types
# ------------------------------------------------

SizeType: TypeAlias = QSize | tuple[int, int]
"""Type alias for size specifications.

Accepts:
    - QSize: A Qt size object
    - tuple[int, int]: (width, height) tuple

Used by: IconButton, widget sizing, etc.
"""

# ------------------------------------------------
# Color Types
# ------------------------------------------------

ColorType: TypeAlias = QColor | str
"""Type alias for color specifications.

Accepts:
    - QColor: A Qt color object
    - str: Color string (hex "#RRGGBB", named color "red", etc.)

Used by: Widgets with custom painting (ToggleSwitch, CircularTimer, etc.)
"""

# ------------------------------------------------
# Widget Types
# ------------------------------------------------

WidgetParent: TypeAlias = QWidget | None
"""Type alias for widget parent parameter.

Accepts:
    - QWidget: A parent widget
    - None: No parent (top-level widget)

Used by: All widget constructors.
"""

# ------------------------------------------------
# Animation Types
# ------------------------------------------------

AnimationDuration: TypeAlias = int
"""Type alias for animation duration in milliseconds.

Used by: Widgets with animations (ToggleSwitch, LoaderButton, etc.)
"""

# ------------------------------------------------
# Callback Types
# ------------------------------------------------

EventCallback: TypeAlias = Callable[[], None]
"""Type alias for event callbacks without parameters.

Used by: Click handlers, event callbacks, etc.
"""

ValueCallback: TypeAlias = Callable[[Any], None]
"""Type alias for value change callbacks.

Used by: Signal handlers, value change callbacks, etc.
"""

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Icon types
    "IconSource",
    "IconSourceExtended",
    # Size types
    "SizeType",
    # Color types
    "ColorType",
    # Widget types
    "WidgetParent",
    # Animation types
    "AnimationDuration",
    # Callback types
    "EventCallback",
    "ValueCallback",
]
