# ///////////////////////////////////////////////////////////////
# TEST_AUTO_COMPLETE_INPUT - AutoCompleteInput Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for AutoCompleteInput widget.

Tests for the autocomplete input widget with suggestion support.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter

# Local imports
from ezqt_widgets.widgets.input.auto_complete_input import AutoCompleteInput

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestAutoCompleteInput:
    """Tests for AutoCompleteInput class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        input_widget = AutoCompleteInput()

        assert input_widget is not None
        assert isinstance(input_widget, AutoCompleteInput)
        assert input_widget.suggestions == []
        assert input_widget.case_sensitive is False
        assert input_widget.filter_mode == Qt.MatchFlag.MatchContains
        assert input_widget.completion_mode == QCompleter.CompletionMode.PopupCompletion

    def test_should_use_custom_suggestions_and_modes_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom parameters."""
        suggestions = ["test1", "test2", "test3"]
        input_widget = AutoCompleteInput(
            suggestions=suggestions,
            case_sensitive=True,
            filter_mode=Qt.MatchFlag.MatchStartsWith,
            completion_mode=QCompleter.CompletionMode.InlineCompletion,
        )

        assert input_widget.suggestions == suggestions
        assert input_widget.case_sensitive is True
        assert input_widget.filter_mode == Qt.MatchFlag.MatchStartsWith
        assert (
            input_widget.completion_mode == QCompleter.CompletionMode.InlineCompletion
        )

    def test_should_update_properties_when_setters_are_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget properties."""
        input_widget = AutoCompleteInput()

        # Test suggestions property
        suggestions = ["item1", "item2", "item3"]
        input_widget.suggestions = suggestions
        assert input_widget.suggestions == suggestions

        # Test case_sensitive property
        input_widget.case_sensitive = True
        assert input_widget.case_sensitive is True

        # Test filter_mode property
        input_widget.filter_mode = Qt.MatchFlag.MatchStartsWith
        assert input_widget.filter_mode == Qt.MatchFlag.MatchStartsWith

        # Test completion_mode property
        input_widget.completion_mode = QCompleter.CompletionMode.InlineCompletion
        assert (
            input_widget.completion_mode == QCompleter.CompletionMode.InlineCompletion
        )

    def test_should_add_to_suggestions_list_when_add_suggestion_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test add_suggestion method."""
        input_widget = AutoCompleteInput()

        # Initial state
        assert input_widget.suggestions == []

        # Add a suggestion
        input_widget.add_suggestion("new_item")
        assert "new_item" in input_widget.suggestions

        # Add another suggestion
        input_widget.add_suggestion("another_item")
        assert "new_item" in input_widget.suggestions
        assert "another_item" in input_widget.suggestions
        assert len(input_widget.suggestions) == 2

    def test_should_remove_from_suggestions_list_when_remove_suggestion_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test remove_suggestion method."""
        input_widget = AutoCompleteInput(suggestions=["item1", "item2", "item3"])

        # Initial state
        assert len(input_widget.suggestions) == 3

        # Remove a suggestion
        input_widget.remove_suggestion("item2")
        assert "item1" in input_widget.suggestions
        assert "item2" not in input_widget.suggestions
        assert "item3" in input_widget.suggestions
        assert len(input_widget.suggestions) == 2

    def test_should_empty_suggestions_list_when_clear_suggestions_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test clear_suggestions method."""
        input_widget = AutoCompleteInput(suggestions=["item1", "item2", "item3"])

        # Initial state
        assert len(input_widget.suggestions) == 3

        # Clear all suggestions
        input_widget.clear_suggestions()
        assert input_widget.suggestions == []

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refresh_style method."""
        input_widget = AutoCompleteInput()

        # Method should not raise an exception
        try:
            input_widget.refresh_style()
        except Exception as e:
            pytest.fail(f"refresh_style() raised an exception: {e}")

    def test_should_configure_completer_with_model_when_suggestions_are_given(
        self, qt_widget_cleanup
    ) -> None:
        """Test QCompleter integration."""
        input_widget = AutoCompleteInput(suggestions=["test1", "test2"])

        # Verify that the completer is configured
        assert input_widget.completer() is not None
        assert isinstance(input_widget.completer(), QCompleter)

        # Verify that the model contains the suggestions
        model = input_widget.completer().model()
        assert model is not None
        assert model.rowCount() == 2

    def test_should_update_case_sensitivity_flag_when_case_sensitive_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test case sensitivity."""
        input_widget = AutoCompleteInput(suggestions=["Test", "test", "TEST"])

        # Test case insensitive (default)
        input_widget.case_sensitive = False
        assert input_widget.case_sensitive is False

        # Test case sensitive
        input_widget.case_sensitive = True
        assert input_widget.case_sensitive is True

    def test_should_support_all_filter_modes_when_filter_mode_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test different filter modes."""
        input_widget = AutoCompleteInput()

        # Test MatchContains (default)
        input_widget.filter_mode = Qt.MatchFlag.MatchContains
        assert input_widget.filter_mode == Qt.MatchFlag.MatchContains

        # Test MatchStartsWith
        input_widget.filter_mode = Qt.MatchFlag.MatchStartsWith
        assert input_widget.filter_mode == Qt.MatchFlag.MatchStartsWith

        # Test MatchEndsWith
        input_widget.filter_mode = Qt.MatchFlag.MatchEndsWith
        assert input_widget.filter_mode == Qt.MatchFlag.MatchEndsWith

    def test_should_support_all_completion_modes_when_completion_mode_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test different completion modes."""
        input_widget = AutoCompleteInput()

        # Test PopupCompletion (default)
        input_widget.completion_mode = QCompleter.CompletionMode.PopupCompletion
        assert input_widget.completion_mode == QCompleter.CompletionMode.PopupCompletion

        # Test InlineCompletion
        input_widget.completion_mode = QCompleter.CompletionMode.InlineCompletion
        assert (
            input_widget.completion_mode == QCompleter.CompletionMode.InlineCompletion
        )

        # Test UnfilteredPopupCompletion
        input_widget.completion_mode = (
            QCompleter.CompletionMode.UnfilteredPopupCompletion
        )
        assert (
            input_widget.completion_mode
            == QCompleter.CompletionMode.UnfilteredPopupCompletion
        )

    def test_should_handle_text_input_when_user_types(self, qt_widget_cleanup) -> None:
        """Test text handling."""
        input_widget = AutoCompleteInput()

        # Test setText
        input_widget.setText("test text")
        assert input_widget.text() == "test text"

        # Test clear
        input_widget.clear()
        assert input_widget.text() == ""

        # Test placeholder
        input_widget.setPlaceholderText("Enter text...")
        assert input_widget.placeholderText() == "Enter text..."

    def test_should_store_multiple_suggestions_when_multiple_are_added(
        self, qt_widget_cleanup
    ) -> None:
        """Test with many suggestions."""
        suggestions = [f"item_{i}" for i in range(100)]
        input_widget = AutoCompleteInput(suggestions=suggestions)

        # Verify that all suggestions are present
        assert len(input_widget.suggestions) == 100
        assert "item_0" in input_widget.suggestions
        assert "item_99" in input_widget.suggestions

        # Verify that the completer can handle many elements
        assert input_widget.completer().model().rowCount() == 100

    def test_should_handle_empty_suggestions_when_suggestions_list_is_empty(
        self, qt_widget_cleanup
    ) -> None:
        """Test with empty suggestions."""
        input_widget = AutoCompleteInput(suggestions=[])

        # Verify initial state
        assert input_widget.suggestions == []

        # Add suggestions
        input_widget.add_suggestion("new_item")
        assert input_widget.suggestions == ["new_item"]

        # Clear and verify
        input_widget.clear_suggestions()
        assert input_widget.suggestions == []

    def test_should_handle_duplicate_suggestions_when_same_suggestion_is_added(
        self, qt_widget_cleanup
    ) -> None:
        """Test with duplicate suggestions."""
        input_widget = AutoCompleteInput()

        # Add duplicate suggestions
        input_widget.add_suggestion("item")
        input_widget.add_suggestion("item")
        input_widget.add_suggestion("item")

        # Verify that duplicates are ignored (widget behavior)
        assert input_widget.suggestions.count("item") == 1

        # Remove the occurrence
        input_widget.remove_suggestion("item")
        assert input_widget.suggestions.count("item") == 0

    def test_should_handle_special_characters_when_suggestion_has_special_chars(
        self, qt_widget_cleanup
    ) -> None:
        """Test with special characters."""
        special_suggestions = [
            "test@example.com",
            "user-name_123",
            "file/path/to/item",
            "item with spaces",
            "item\nwith\nnewlines",
            "item\twith\ttabs",
        ]

        input_widget = AutoCompleteInput(suggestions=special_suggestions)

        # Verify that all suggestions are preserved
        assert len(input_widget.suggestions) == 6
        for suggestion in special_suggestions:
            assert suggestion in input_widget.suggestions

    def test_should_have_correct_type_property_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test type property for QSS."""
        input_widget = AutoCompleteInput()

        # Verify that the widget works correctly
        # Note: AutoCompleteInput inherits from QLineEdit,
        # so no custom type property
        assert input_widget is not None
        assert isinstance(input_widget, AutoCompleteInput)
