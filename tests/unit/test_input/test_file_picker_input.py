# ///////////////////////////////////////////////////////////////
# TEST_FILE_PICKER_INPUT - FilePickerInput Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for FilePickerInput widget.

Tests for the file picker input widget combining a QLineEdit and
a folder icon button.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import tempfile

# Third-party imports
import pytest
from PySide6.QtWidgets import QLineEdit, QToolButton

# Local imports
from ezqt_widgets.widgets.input.file_picker_input import FilePickerInput

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestFilePickerInput:
    """Tests for FilePickerInput class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        widget = FilePickerInput()

        assert widget is not None
        assert isinstance(widget, FilePickerInput)
        assert widget.path == ""
        assert widget.mode == "file"
        assert widget.placeholder_text == "Select a file..."
        assert widget.filter == ""
        assert widget.dialog_title == ""

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom keyword arguments."""
        widget = FilePickerInput(
            placeholder="Choose a CSV...",
            mode="directory",
            filter="CSV (*.csv)",
            dialog_title="Pick folder",
        )

        assert widget.placeholder_text == "Choose a CSV..."
        assert widget.mode == "directory"
        assert widget.filter == "CSV (*.csv)"
        assert widget.dialog_title == "Pick folder"

    def test_should_have_line_edit_and_button_children(self, qt_widget_cleanup) -> None:
        """Test that child widgets are correctly instantiated."""
        widget = FilePickerInput()

        line_edits = widget.findChildren(QLineEdit)
        buttons = widget.findChildren(QToolButton)

        assert len(line_edits) >= 1
        assert len(buttons) >= 1

    def test_should_update_path_property_when_set(self, qt_widget_cleanup) -> None:
        """Test path property setter and getter."""
        widget = FilePickerInput()

        widget.path = "/home/user/file.txt"
        assert widget.path == "/home/user/file.txt"

        widget.path = ""
        assert widget.path == ""

    def test_should_clear_path_when_clear_is_called(self, qt_widget_cleanup) -> None:
        """Test clear() method resets path to empty string."""
        widget = FilePickerInput()
        widget.path = "/some/path/file.csv"
        assert widget.path == "/some/path/file.csv"

        widget.clear()
        assert widget.path == ""

    def test_should_update_mode_when_mode_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test mode property setter."""
        widget = FilePickerInput()

        widget.mode = "directory"
        assert widget.mode == "directory"

        widget.mode = "file"
        assert widget.mode == "file"

    def test_should_ignore_invalid_mode_when_set(self, qt_widget_cleanup) -> None:
        """Test that an invalid mode value is silently ignored."""
        widget = FilePickerInput(mode="file")

        widget.mode = "invalid"  # type: ignore[assignment]
        assert widget.mode == "file"  # Unchanged

    def test_should_update_placeholder_when_placeholder_text_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test placeholder_text property setter."""
        widget = FilePickerInput()

        widget.placeholder_text = "Select a folder..."
        assert widget.placeholder_text == "Select a folder..."

    def test_should_update_filter_when_filter_is_set(self, qt_widget_cleanup) -> None:
        """Test filter property setter."""
        widget = FilePickerInput()

        widget.filter = "Images (*.png *.jpg)"
        assert widget.filter == "Images (*.png *.jpg)"

    def test_should_update_dialog_title_when_dialog_title_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test dialog_title property setter."""
        widget = FilePickerInput()

        widget.dialog_title = "Open project file"
        assert widget.dialog_title == "Open project file"

    def test_should_emit_path_changed_signal_when_path_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test pathChanged signal emission on path assignment."""
        widget = FilePickerInput()

        received: list[str] = []
        widget.pathChanged.connect(received.append)

        tmp_path = tempfile.gettempdir() + "/test.txt"
        widget.path = tmp_path
        assert len(received) >= 1
        assert received[-1] == tmp_path

    def test_should_emit_path_changed_signal_on_clear(self, qt_widget_cleanup) -> None:
        """Test pathChanged signal emission when clear() is called."""
        widget = FilePickerInput()
        widget.path = tempfile.gettempdir() + "/file.py"

        received: list[str] = []
        widget.pathChanged.connect(received.append)

        widget.clear()
        assert len(received) >= 1
        assert received[-1] == ""

    def test_should_not_raise_when_set_theme_is_called(self, qt_widget_cleanup) -> None:
        """Test setTheme() does not raise for dark and light themes."""
        widget = FilePickerInput()

        try:
            widget.setTheme("dark")
            widget.setTheme("light")
        except Exception as exc:
            pytest.fail(f"setTheme() raised an exception: {exc}")

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle() does not raise."""
        widget = FilePickerInput()

        try:
            widget.refreshStyle()
        except Exception as exc:
            pytest.fail(f"refreshStyle() raised an exception: {exc}")

    def test_should_handle_unicode_path_when_path_contains_unicode(
        self, qt_widget_cleanup
    ) -> None:
        """Test path property with unicode characters."""
        widget = FilePickerInput()

        unicode_path = "/home/utilisateur/fichier_テスト.txt"
        widget.path = unicode_path
        assert widget.path == unicode_path

    def test_should_have_file_selected_signal_defined(self, qt_widget_cleanup) -> None:
        """Test that fileSelected signal exists and is connectable."""
        widget = FilePickerInput()

        received: list[str] = []
        widget.fileSelected.connect(received.append)

        # Signal is connected — verify no exception during connection
        assert widget.fileSelected is not None
