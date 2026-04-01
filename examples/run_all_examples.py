#!/usr/bin/env python3
# ///////////////////////////////////////////////////////////////
# RUN ALL EXAMPLES - EzQt Widgets
# Main launcher for all widget examples
# ///////////////////////////////////////////////////////////////

"""
Main script to run all EzQt Widgets examples.

This script provides a graphical interface to launch and explore
any example widget available in the examples folder.

Features:
    - Navigation between different widget categories
    - Modern tabbed interface
    - Help and About dialogs
    - Error handling for missing widgets

Example:
    Run this script to open the examples launcher::

        $ python run_all_examples.py
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import os
import sys
from importlib import import_module

# Third-party imports
from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent, QFont
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from utils.theme import apply_theme

# ///////////////////////////////////////////////////////////////
# PATH SETUP
# ///////////////////////////////////////////////////////////////

# Add current folder to path for relative imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# ///////////////////////////////////////////////////////////////
# EXAMPLES LAUNCHER
# ///////////////////////////////////////////////////////////////


class EzQtExamplesLauncher(QMainWindow):
    """
    Main launcher for all EzQt Widgets examples.

    This class provides a modern tabbed interface to navigate
    between different widget category examples.

    Attributes:
        nav_buttons: Dictionary of navigation buttons.
        example_widgets: Dictionary of example widget instances.
        stacked_widget: Stacked widget containing all examples.
    """

    def __init__(self) -> None:
        """Initialize the EzQtExamplesLauncher."""
        super().__init__()
        self.setWindowTitle("EzQt Widgets - Examples Launcher")
        self.setMinimumSize(1200, 800)
        self.nav_buttons: dict[str, QPushButton] = {}
        self.example_widgets: dict[str, QWidget] = {}
        self._setup_ui()
        self._setup_theme()

    # -----------------------------------------------------------
    # UI Setup
    # -----------------------------------------------------------

    def _setup_ui(self) -> None:
        """Configure the user interface."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Header with title and navigation
        self._setup_header(main_layout)

        # Content area with stacked widget
        self._setup_content_area(main_layout)

        # Footer with information
        self._setup_footer(main_layout)

    def _setup_header(self, main_layout: QVBoxLayout) -> None:
        """
        Configure the header with navigation.

        Args:
            main_layout: Parent layout to add the header to.
        """
        # Header container
        header_frame = QFrame()
        header_frame.setObjectName("header")
        header_frame.setFixedHeight(120)
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(20, 15, 20, 15)

        # Main title
        title = QLabel("EzQt Widgets - Complete Demonstration")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("main-title")
        header_layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("Select a category to explore the widgets")
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setObjectName("subtitle")
        header_layout.addWidget(subtitle)

        # Navigation bar
        nav_frame = QFrame()
        nav_frame.setObjectName("nav-bar")
        nav_layout = QHBoxLayout(nav_frame)
        nav_layout.setSpacing(10)
        nav_layout.setContentsMargins(0, 10, 0, 0)

        # Navigation items
        nav_items = [
            ("buttons", "Buttons", "🎯"),
            ("inputs", "Inputs", "⌨️"),
            ("labels", "Labels", "🏷️"),
            ("misc", "Misc", "🔧"),
        ]

        # Create example widgets first to know which are available
        self._load_example_widgets()

        # Create navigation buttons only for available widgets
        for key, text, icon in nav_items:
            if key in self.example_widgets and self.example_widgets[key] is not None:
                btn = QPushButton(f"{icon} {text}")
                btn.setObjectName("nav-button")
                btn.setCheckable(True)
                btn.clicked.connect(lambda _checked, k=key: self._switch_to_example(k))
                nav_layout.addWidget(btn)
                self.nav_buttons[key] = btn

        # Set first available button as active
        if self.nav_buttons:
            first_key = list(self.nav_buttons.keys())[0]
            self.nav_buttons[first_key].setChecked(True)

        header_layout.addWidget(nav_frame)
        main_layout.addWidget(header_frame)

    def _load_example_widgets(self) -> None:
        """Load all example widgets with error handling."""
        widget_modules = [
            ("buttons", "_button", "ButtonExampleWidget"),
            ("inputs", "_input", "InputExampleWidget"),
            ("labels", "_label", "LabelExampleWidget"),
            ("misc", "_misc", "MiscExampleWidget"),
        ]

        for key, module_name, class_name in widget_modules:
            try:
                module = import_module(module_name)
                widget_class = getattr(module, class_name)
                self.example_widgets[key] = widget_class()
            except Exception as e:
                print(f"Error loading {class_name}: {e}")

    def _setup_content_area(self, main_layout: QVBoxLayout) -> None:
        """
        Configure the content area.

        Args:
            main_layout: Parent layout to add the content area to.
        """
        # Container for content
        content_frame = QFrame()
        content_frame.setObjectName("content-area")
        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(20, 20, 20, 20)

        # Stacked widget for examples
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("stacked-content")

        # Add widgets to stacked widget
        for widget in self.example_widgets.values():
            if widget is not None:
                self.stacked_widget.addWidget(widget)

        content_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(content_frame)

    def _setup_footer(self, main_layout: QVBoxLayout) -> None:
        """
        Configure the footer.

        Args:
            main_layout: Parent layout to add the footer to.
        """
        # Footer container
        footer_frame = QFrame()
        footer_frame.setObjectName("footer")
        footer_frame.setFixedHeight(60)
        footer_layout = QHBoxLayout(footer_frame)
        footer_layout.setContentsMargins(20, 10, 20, 10)

        # Version information
        version_info = QLabel("EzQt Widgets v2.3.0 - Custom Qt widgets library")
        version_info.setObjectName("footer-text")
        footer_layout.addWidget(version_info)

        # Action buttons
        action_layout = QHBoxLayout()
        action_layout.setSpacing(10)

        help_btn = QPushButton("Help")
        help_btn.setObjectName("footer-button")
        help_btn.clicked.connect(self._show_help)
        action_layout.addWidget(help_btn)

        about_btn = QPushButton("About")
        about_btn.setObjectName("footer-button")
        about_btn.clicked.connect(self._show_about)
        action_layout.addWidget(about_btn)

        footer_layout.addLayout(action_layout)
        main_layout.addWidget(footer_frame)

    def _setup_theme(self) -> None:
        """Configure the global application theme."""
        apply_theme(self)

    # -----------------------------------------------------------
    # Navigation
    # -----------------------------------------------------------

    def _switch_to_example(self, example_key: str) -> None:
        """
        Switch to the selected example.

        Args:
            example_key: Key of the example to display.
        """
        # Update navigation buttons
        for key, btn in self.nav_buttons.items():
            btn.setChecked(key == example_key)

        # Change displayed widget
        if example_key in self.example_widgets:
            self.stacked_widget.setCurrentWidget(self.example_widgets[example_key])
            print(f"Switched to example: {example_key}")

    # -----------------------------------------------------------
    # Dialog Methods
    # -----------------------------------------------------------

    def _show_help(self) -> None:
        """Display the help dialog."""
        help_text = """
        <h3>User Guide - EzQt Widgets</h3>

        <p><b>Navigation:</b></p>
        <ul>
            <li>Use the navigation buttons at the top to switch examples</li>
            <li>Each example demonstrates a widget category</li>
            <li>Interact with widgets to see their features</li>
        </ul>

        <p><b>Available Categories:</b></p>
        <ul>
            <li><b>Buttons:</b> DateButton, IconButton, LoaderButton</li>
            <li><b>Inputs:</b> TabReplaceTextEdit, AutoCompleteInput, SearchInput</li>
            <li><b>Labels:</b> FramedLabel, IndicatorLabel, HoverLabel, ClickableTagLabel</li>
            <li><b>Misc:</b> OptionSelector, CircularTimer, ToggleIcon, ToggleSwitch, DraggableList</li>
        </ul>

        <p><b>Tests:</b></p>
        <ul>
            <li>Use "Test" buttons to see interactions</li>
            <li>"Reset" buttons restore initial state</li>
        </ul>
        """

        QMessageBox.information(self, "Help - EzQt Widgets", help_text)

    def _show_about(self) -> None:
        """Display the about dialog."""
        about_text = """
        <h3>EzQt Widgets v2.3.0</h3>

        <p>Custom Qt widgets library for PySide6.</p>

        <p><b>Features:</b></p>
        <ul>
            <li>Advanced button widgets</li>
            <li>Specialized input fields</li>
            <li>Interactive labels</li>
            <li>Various utility widgets</li>
        </ul>

        <p><b>Compatibility:</b> PySide6</p>
        <p><b>License:</b> MIT</p>

        <p>Developed to simplify creating modern Qt interfaces.</p>
        """

        QMessageBox.about(self, "About - EzQt Widgets", about_text)

    # -----------------------------------------------------------
    # Events
    # -----------------------------------------------------------

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        Handle application close event.

        Args:
            event: The close event.
        """
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Do you really want to quit the demonstration?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


# ///////////////////////////////////////////////////////////////
# MAIN FUNCTION
# ///////////////////////////////////////////////////////////////


def main() -> None:
    """Main function."""
    app = QApplication(sys.argv)

    # Application configuration
    app.setApplicationName("EzQt Widgets Examples")
    app.setApplicationVersion("2.3.0")
    app.setOrganizationName("EzQt Widgets")

    # Create and display main window
    window = EzQtExamplesLauncher()
    window.show()

    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
