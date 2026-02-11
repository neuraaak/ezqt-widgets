# ///////////////////////////////////////////////////////////////
# TYPES EXAMPLE - Type Aliases Usage Example
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Example demonstrating the usage of type aliases from ezqt_widgets.types.

This example shows how to use the centralized type aliases to improve
code readability and type safety when working with ezqt_widgets.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

# Local imports
from ezqt_widgets import IconButton, ToggleSwitch
from ezqt_widgets.types import (
    AnimationDuration,
    ColorType,
    IconSource,
    SizeType,
    WidgetParent,
)

# ///////////////////////////////////////////////////////////////
# EXAMPLE FUNCTIONS
# ///////////////////////////////////////////////////////////////


def create_icon_button(
    parent: WidgetParent,
    icon: IconSource,
    text: str,
    size: SizeType = (24, 24),
) -> IconButton:
    """Create an icon button with type-safe parameters.

    Args:
        parent: Parent widget or None.
        icon: Icon source (QIcon, path, URL, or None).
        text: Button text.
        size: Icon size as QSize or (width, height) tuple.

    Returns:
        The created icon button.
    """
    button = IconButton(parent=parent, icon=icon, text=text)
    button.icon_size = size
    return button


def create_toggle_switch(
    parent: WidgetParent,
    checked: bool = False,
    animation_duration: AnimationDuration = 200,
) -> ToggleSwitch:
    """Create a toggle switch with type-safe parameters.

    Args:
        parent: Parent widget or None.
        checked: Initial checked state.
        animation_duration: Animation duration in milliseconds.

    Returns:
        The created toggle switch.
    """
    toggle = ToggleSwitch(parent=parent, checked=checked)
    toggle._animation_duration = animation_duration
    return toggle


def apply_color_to_widget(widget: QWidget, color: ColorType) -> None:
    """Apply a color to a widget with type-safe parameter.

    Args:
        widget: The widget to style.
        color: Color as QColor or string (hex, named color, etc.).
    """
    if isinstance(color, str):
        color = QColor(color)
    widget.setStyleSheet(f"background-color: {color.name()};")


# ///////////////////////////////////////////////////////////////
# MAIN EXAMPLE
# ///////////////////////////////////////////////////////////////


def main() -> None:
    """Run the type aliases usage example."""
    app = QApplication([])

    # Create main window
    window = QWidget()
    window.setWindowTitle("Type Aliases Example - ezqt_widgets")
    window.setMinimumSize(400, 300)

    layout = QVBoxLayout(window)

    # Example 1: Create button with different icon source types
    print("Creating buttons with different icon sources...")

    # Using None as icon source
    button1 = create_icon_button(
        parent=window,
        icon=None,
        text="No Icon Button",
    )
    layout.addWidget(button1)

    # Using string path as icon source
    button2 = create_icon_button(
        parent=window,
        icon="path/to/icon.png",  # Would work with a real path
        text="Path Icon Button",
    )
    layout.addWidget(button2)

    # Using QIcon as icon source
    button3 = create_icon_button(
        parent=window,
        icon=QIcon(),
        text="QIcon Button",
    )
    layout.addWidget(button3)

    # Example 2: Create toggle with custom animation duration
    print("Creating toggle switches...")

    toggle1 = create_toggle_switch(
        parent=window,
        checked=False,
        animation_duration=100,  # Fast animation
    )
    layout.addWidget(toggle1)

    toggle2 = create_toggle_switch(
        parent=window,
        checked=True,
        animation_duration=500,  # Slow animation
    )
    layout.addWidget(toggle2)

    # Example 3: Apply colors using different formats
    print("Applying colors...")

    # Using hex color string
    apply_color_to_widget(button1, "#FF5733")

    # Using named color string
    apply_color_to_widget(button2, "lightblue")

    # Using QColor object
    apply_color_to_widget(button3, QColor(100, 200, 100))

    # Example 4: Using SizeType with different formats
    print("Setting sizes...")

    # Using tuple
    button1.icon_size = (32, 32)

    # Using QSize
    button2.icon_size = QSize(24, 24)

    window.show()

    print("\nType aliases example running!")
    print("Benefits of using type aliases:")
    print("  - Better code readability")
    print("  - Centralized type definitions")
    print("  - Easier refactoring")
    print("  - Consistent typing across the library")
    print("\nClose the window to exit.")

    app.exec()


# ///////////////////////////////////////////////////////////////
# ENTRY POINT
# ///////////////////////////////////////////////////////////////

if __name__ == "__main__":
    main()
