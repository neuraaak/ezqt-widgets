# ///////////////////////////////////////////////////////////////
# TEST_DATE_BUTTON - DateButton Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for DateButton widget.

Tests for the date selection button widget with integrated calendar dialog.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from unittest.mock import MagicMock, patch

# Third-party imports
import pytest
from PySide6.QtCore import QDate, QPoint, QSize, Qt
from PySide6.QtGui import QIcon, QMouseEvent
from PySide6.QtWidgets import QDialog

# Local imports
from ezqt_widgets.widgets.button.date_button import (
    DateButton,
    DatePickerDialog,
)

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_should_format_date_string_when_date_is_valid(
        self, qt_widget_cleanup
    ) -> None:
        """Test format_date with a valid date."""
        date = QDate(2024, 1, 15)
        result = DateButton._format_date(date, "dd/MM/yyyy")
        assert result == "15/01/2024"

    def test_should_return_empty_string_when_date_is_invalid(
        self, qt_widget_cleanup
    ) -> None:
        """Test format_date with an invalid date."""
        date = QDate()
        result = DateButton._format_date(date, "dd/MM/yyyy")
        assert result == ""

    def test_should_use_custom_format_when_format_is_given(
        self, qt_widget_cleanup
    ) -> None:
        """Test format_date with a custom format."""
        date = QDate(2024, 1, 15)
        result = DateButton._format_date(date, "yyyy-MM-dd")
        assert result == "2024-01-15"

    def test_should_return_date_object_when_date_string_is_valid(
        self, qt_widget_cleanup
    ) -> None:
        """Test parse_date with a valid string."""
        result = DateButton._parse_date("15/01/2024", "dd/MM/yyyy")
        assert result.isValid()
        assert result.year() == 2024
        assert result.month() == 1
        assert result.day() == 15

    def test_should_return_none_when_date_string_is_invalid(
        self, qt_widget_cleanup
    ) -> None:
        """Test parse_date with an invalid string."""
        result = DateButton._parse_date("invalid", "dd/MM/yyyy")
        assert not result.isValid()

    def test_should_return_icon_when_get_calendar_icon_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test get_calendar_icon."""
        icon = DateButton._get_calendar_icon()
        assert icon is not None
        assert isinstance(icon, QIcon)
        assert not icon.isNull()


class TestDatePickerDialog:
    """Tests for DatePickerDialog class."""

    def test_should_create_dialog_when_instantiated(self, qt_widget_cleanup) -> None:
        """Test dialog creation."""
        dialog = DatePickerDialog()
        assert dialog is not None
        assert isinstance(dialog, DatePickerDialog)

    def test_should_initialize_with_date_when_date_is_given(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with a date."""
        date = QDate(2024, 1, 15)
        dialog = DatePickerDialog(current_date=date)
        assert dialog.selectedDate() == date

    def test_should_return_selected_date_when_date_is_picked(
        self, qt_widget_cleanup
    ) -> None:
        """Test selected_date property."""
        dialog = DatePickerDialog()
        assert dialog.selectedDate() is None


class TestDateButton:
    """Tests for DateButton class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        button = DateButton()

        assert button is not None
        assert isinstance(button, DateButton)
        assert button.date_format == "dd/MM/yyyy"
        assert button.placeholder == "Select a date"
        assert button.show_calendar_icon is True
        assert button.icon_size == QSize(16, 16)

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom parameters."""
        date = QDate(2024, 1, 15)
        button = DateButton(
            date=date,
            date_format="yyyy-MM-dd",
            placeholder="Choose date",
            show_calendar_icon=False,
            icon_size=QSize(24, 24),
        )

        assert button.date == date
        assert button.date_format == "yyyy-MM-dd"
        assert button.placeholder == "Choose date"
        assert button.show_calendar_icon is False
        assert button.icon_size == QSize(24, 24)

    def test_should_parse_string_date_when_date_string_is_given(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with a string date."""
        button = DateButton(date="15/01/2024")

        assert button.date.isValid()
        assert button.date.year() == 2024
        assert button.date.month() == 1
        assert button.date.day() == 15

    def test_should_update_properties_when_setters_are_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test button properties."""
        button = DateButton()

        # Test date property
        date = QDate(2024, 1, 15)
        button.date = date
        assert button.date == date

        # Test date_string property
        button.date_string = "20/02/2024"
        assert button.date.year() == 2024
        assert button.date.month() == 2
        assert button.date.day() == 20

        # Test date_format property
        button.date_format = "yyyy-MM-dd"
        assert button.date_format == "yyyy-MM-dd"

        # Test placeholder property
        button.placeholder = "New placeholder"
        assert button.placeholder == "New placeholder"

        # Test show_calendar_icon property
        button.show_calendar_icon = False
        assert button.show_calendar_icon is False

        # Test icon_size property
        button.icon_size = QSize(32, 32)
        assert button.icon_size == QSize(32, 32)

    def test_should_emit_date_changed_signal_when_date_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test button signals."""
        button = DateButton()

        # Test dateChanged signal
        date = QDate(2024, 1, 15)

        signal_received = False

        def on_date_changed(new_date: QDate) -> None:
            nonlocal signal_received
            signal_received = True
            assert new_date == date

        button.dateChanged.connect(on_date_changed)
        button.date = date

        # Verify that the signal was emitted
        assert signal_received

    def test_should_not_raise_when_methods_are_called(self, qt_widget_cleanup) -> None:
        """Test button methods."""
        button = DateButton()

        # Test clearDate
        button.date = QDate(2024, 1, 15)
        button.clearDate()
        assert not button.date.isValid()

        # Test setToday
        button.setToday()
        assert button.date.isValid()
        assert button.date == QDate.currentDate()

    @patch("ezqt_widgets.widgets.button.date_button.DatePickerDialog")
    def test_should_open_calendar_dialog_when_open_calendar_is_called(
        self, mock_dialog_class, qt_widget_cleanup
    ) -> None:
        """Test open_calendar method."""
        button = DateButton()

        # Mock the dialog
        mock_dialog = MagicMock()
        mock_dialog.selectedDate.return_value = QDate(2024, 1, 15)
        mock_dialog_class.return_value = mock_dialog

        # Test calendar opening
        button.openCalendar()

        # Verify that the dialog was created and executed
        mock_dialog_class.assert_called_once()
        mock_dialog.exec.assert_called_once()

    def test_should_return_valid_size_hints_when_queried(
        self, qt_widget_cleanup
    ) -> None:
        """Test size hint methods."""
        button = DateButton(text="Test Button")

        # Test sizeHint
        size_hint = button.sizeHint()
        assert size_hint is not None
        assert isinstance(size_hint, QSize)
        assert size_hint.width() > 0
        assert size_hint.height() > 0

        # Test minimumSizeHint
        min_size_hint = button.minimumSizeHint()
        assert min_size_hint is not None
        assert isinstance(min_size_hint, QSize)
        assert min_size_hint.width() > 0
        assert min_size_hint.height() > 0

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle method."""
        button = DateButton()

        # Method should not raise an exception
        try:
            button.refreshStyle()
        except Exception as e:
            pytest.fail(f"refreshStyle() raised an exception: {e}")

    def test_should_have_minimum_dimensions_when_instantiated(
        self, qt_widget_cleanup
    ) -> None:
        """Test minimum dimensions."""
        button = DateButton(min_width=150, min_height=50)

        assert button.min_width == 150
        assert button.min_height == 50

        # Modify dimensions
        button.min_width = 200
        button.min_height = 75

        assert button.min_width == 200
        assert button.min_height == 75

        # Test with None
        button.min_width = None
        button.min_height = None

        assert button.min_width is None
        assert button.min_height is None

    @patch("ezqt_widgets.widgets.button.date_button.DatePickerDialog")
    def test_should_open_calendar_when_mouse_is_pressed(
        self, mock_dialog_class, qt_widget_cleanup
    ) -> None:
        """Test mousePressEvent."""
        button = DateButton()

        # Mock the dialog to avoid blocking
        mock_dialog = MagicMock()
        mock_dialog.selectedDate.return_value = QDate(2024, 1, 15)
        mock_dialog.exec.return_value = QDialog.DialogCode.Accepted
        mock_dialog_class.return_value = mock_dialog

        # Create a real Qt mouse event
        event = QMouseEvent(
            QMouseEvent.Type.MouseButtonPress,
            QPoint(10, 10),
            QPoint(10, 10),
            Qt.MouseButton.LeftButton,
            Qt.MouseButton.LeftButton,
            Qt.KeyboardModifier.NoModifier,
        )

        # Test that the event does not raise an exception
        try:
            button.mousePressEvent(event)
        except Exception as e:
            pytest.fail(f"mousePressEvent() raised an exception: {e}")

        # Verify that the dialog was created and executed
        mock_dialog_class.assert_called_once()
        mock_dialog.exec.assert_called_once()

    def test_should_display_formatted_date_when_date_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test display with a date."""
        date = QDate(2024, 1, 15)
        button = DateButton(date=date)

        # Verify that the date is displayed
        assert button.date_string == "15/01/2024"

    def test_should_display_placeholder_when_no_date_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test display without a date."""
        button = DateButton()

        # Verify that the widget displays a date
        # Note: DateButton initializes with current date by default
        assert button.date_string != ""
        assert button.date.isValid()

        # Clear the date
        button.clearDate()

        # Verify that the date is cleared
        # Note: clearDate() sets an invalid QDate, so date_string returns ""
        assert button.date_string == ""
        assert not button.date.isValid()

        # Verify that the label displays the placeholder
        # The internal label should display the placeholder
        assert button.date_label.text() == button.placeholder

    def test_should_display_custom_format_when_format_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test with a custom format."""
        date = QDate(2024, 1, 15)
        button = DateButton(date=date, date_format="yyyy-MM-dd")

        # Verify that the format is applied
        assert button.date_string == "2024-01-15"

    # ------------------------------------------------
    # New feature tests — min/max date constraints
    # ------------------------------------------------

    def test_should_store_minimum_date_when_provided(self, qt_widget_cleanup) -> None:
        """Test that minimum_date is stored on construction."""
        min_d = QDate(2024, 1, 1)
        button = DateButton(minimum_date=min_d)

        assert button.minimum_date == min_d

    def test_should_store_maximum_date_when_provided(self, qt_widget_cleanup) -> None:
        """Test that maximum_date is stored on construction."""
        max_d = QDate(2024, 12, 31)
        button = DateButton(maximum_date=max_d)

        assert button.maximum_date == max_d

    def test_should_reject_date_below_minimum_when_minimum_date_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test that dates before minimum_date are silently rejected."""
        min_d = QDate(2024, 6, 1)
        button = DateButton(minimum_date=min_d)

        # Force a known valid date first
        button.date = QDate(2024, 6, 15)
        stored = button.date

        # Attempt to set a date below the minimum
        button.date = QDate(2024, 1, 1)
        assert button.date == stored  # unchanged

    def test_should_reject_date_above_maximum_when_maximum_date_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test that dates after maximum_date are silently rejected."""
        max_d = QDate(2024, 6, 30)
        button = DateButton(maximum_date=max_d)

        button.date = QDate(2024, 6, 15)
        stored = button.date

        # Attempt to set a date above the maximum
        button.date = QDate(2024, 12, 31)
        assert button.date == stored  # unchanged

    def test_should_accept_date_within_range_when_constraints_are_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test that a date within [min, max] is accepted."""
        min_d = QDate(2024, 1, 1)
        max_d = QDate(2024, 12, 31)
        button = DateButton(minimum_date=min_d, maximum_date=max_d)

        target = QDate(2024, 6, 15)
        button.date = target
        assert button.date == target

    def test_should_update_minimum_date_property_when_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test minimum_date property setter."""
        button = DateButton()

        new_min = QDate(2025, 1, 1)
        button.minimum_date = new_min
        assert button.minimum_date == new_min

        button.minimum_date = None
        assert button.minimum_date is None

    def test_should_update_maximum_date_property_when_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test maximum_date property setter."""
        button = DateButton()

        new_max = QDate(2025, 12, 31)
        button.maximum_date = new_max
        assert button.maximum_date == new_max

        button.maximum_date = None
        assert button.maximum_date is None

    def test_should_not_call_super_when_left_button_pressed(
        self, qt_widget_cleanup
    ) -> None:
        """Test that left-button press absorbs the event (no QToolButton clicked)."""
        button = DateButton()

        clicked_count = 0

        def on_clicked() -> None:
            nonlocal clicked_count
            clicked_count += 1

        button.clicked.connect(on_clicked)

        event = QMouseEvent(
            QMouseEvent.Type.MouseButtonPress,
            QPoint(10, 10),
            QPoint(10, 10),
            Qt.MouseButton.LeftButton,
            Qt.MouseButton.LeftButton,
            Qt.KeyboardModifier.NoModifier,
        )

        # Patch openCalendar so the dialog does not block
        with patch.object(button, "openCalendar"):
            button.mousePressEvent(event)

        # clicked must NOT have been emitted by QToolButton
        assert clicked_count == 0

    @patch("ezqt_widgets.widgets.button.date_button.DatePickerDialog")
    def test_should_pass_min_max_to_dialog_when_constraints_set(
        self, mock_dialog_class, qt_widget_cleanup
    ) -> None:
        """Test that min/max dates are forwarded to DatePickerDialog."""
        min_d = QDate(2024, 1, 1)
        max_d = QDate(2024, 12, 31)
        button = DateButton(minimum_date=min_d, maximum_date=max_d)

        mock_dialog = MagicMock()
        mock_dialog.exec.return_value = QDialog.DialogCode.Rejected
        mock_dialog_class.return_value = mock_dialog

        button.openCalendar()

        # Verify the dialog was instantiated with the constraints
        _, kwargs = mock_dialog_class.call_args
        assert kwargs.get("min_date") == min_d
        assert kwargs.get("max_date") == max_d
