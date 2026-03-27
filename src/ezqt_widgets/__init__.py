# ///////////////////////////////////////////////////////////////
# EZQT_WIDGETS - Main Module
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
ezqt_widgets - Custom Qt widgets collection for PySide6.

ezqt_widgets is a collection of custom and reusable Qt widgets for PySide6.
It provides advanced, reusable, and styled graphical components to facilitate
the development of modern and ergonomic interfaces.

**Main Features:**
    - Enhanced button widgets (date picker, icon buttons, loading buttons)
    - Advanced input widgets (auto-complete, search, tab replacement)
    - Enhanced label widgets (clickable tags, framed labels, hover labels, indicators)
    - Utility widgets (circular timers, draggable lists, option selectors, toggles)
    - Modern and ergonomic UI components
    - Fully typed API with type hints
    - PySide6 compatible

**Quick Start:**
    >>> from ezqt_widgets import DateButton, IconButton, AutoCompleteInput
    >>> from PySide6.QtWidgets import QApplication
    >>>
    >>> app = QApplication([])
    >>>
    >>> # Create a date button
    >>> date_btn = DateButton()
    >>> date_btn.show()
    >>>
    >>> # Create an icon button
    >>> icon_btn = IconButton(icon="path/to/icon.png", text="Click me")
    >>> icon_btn.show()
    >>>
    >>> # Create an auto-complete input
    >>> input_widget = AutoCompleteInput(completions=["option1", "option2"])
    >>> input_widget.show()
    >>>
    >>> app.exec()
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import sys

# Local imports
from .types import (
    AnimationDuration,
    ColorType,
    EventCallback,
    IconSource,
    IconSourceExtended,
    SizeType,
    ValueCallback,
    WidgetParent,
)
from .version import __version__
from .widgets.button import (
    DateButton,
    DatePickerDialog,
    IconButton,
    LoaderButton,
)
from .widgets.input import (
    AutoCompleteInput,
    FilePickerInput,
    PasswordInput,
    SearchInput,
    SpinBoxInput,
    TabReplaceTextEdit,
)
from .widgets.label import (
    ClickableTagLabel,
    FramedLabel,
    HoverLabel,
    IndicatorLabel,
)
from .widgets.misc import (
    CircularTimer,
    CollapsibleSection,
    DraggableItem,
    DraggableList,
    NotificationBanner,
    NotificationLevel,
    OptionSelector,
    ThemeIcon,
    ToggleIcon,
    ToggleSwitch,
)

# ///////////////////////////////////////////////////////////////
# META INFORMATIONS
# ///////////////////////////////////////////////////////////////

__author__ = "Neuraaak"
__maintainer__ = "Neuraaak"
__description__ = (
    "A collection of custom and reusable Qt widgets for PySide6. "
    "Provides advanced, reusable, and styled graphical components "
    "to facilitate the development of modern and ergonomic interfaces."
)
__python_requires__ = ">=3.11"
__license__ = "MIT"
__keywords__ = [
    "qt",
    "pyside6",
    "widgets",
    "gui",
    "interface",
    "components",
    "ui",
    "desktop",
]
__url__ = "https://github.com/neuraaak/ezqt-widgets"
__repository__ = "https://github.com/neuraaak/ezqt-widgets"

# ///////////////////////////////////////////////////////////////
# PYTHON VERSION CHECK
# ///////////////////////////////////////////////////////////////

if sys.version_info < (3, 11):  # noqa: UP036
    raise RuntimeError(
        f"ezqt_widgets {__version__} requires Python 3.11 or higher. "
        f"Current version: {sys.version}"
    )

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Widgets
    "AutoCompleteInput",
    "CircularTimer",
    "ClickableTagLabel",
    "CollapsibleSection",
    "DateButton",
    "DatePickerDialog",
    "DraggableItem",
    "DraggableList",
    "FilePickerInput",
    "FramedLabel",
    "HoverLabel",
    "IconButton",
    "IndicatorLabel",
    "LoaderButton",
    "NotificationBanner",
    "NotificationLevel",
    "OptionSelector",
    "PasswordInput",
    "SearchInput",
    "SpinBoxInput",
    "TabReplaceTextEdit",
    "ThemeIcon",
    "ToggleIcon",
    "ToggleSwitch",
    # Type aliases
    "AnimationDuration",
    "ColorType",
    "EventCallback",
    "IconSource",
    "IconSourceExtended",
    "SizeType",
    "ValueCallback",
    "WidgetParent",
    # Metadata
    "__author__",
    "__description__",
    "__keywords__",
    "__license__",
    "__maintainer__",
    "__python_requires__",
    "__repository__",
    "__url__",
    "__version__",
]
