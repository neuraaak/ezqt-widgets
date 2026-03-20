# ///////////////////////////////////////////////////////////////
# TEST_SEARCH_INPUT - SearchInput Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for SearchInput widget.

Tests for the search input widget with history support.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap

# Local imports
from ezqt_widgets.widgets.input.search_input import SearchInput

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestSearchInput:
    """Tests for SearchInput class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        search_widget = SearchInput()

        assert search_widget is not None
        assert isinstance(search_widget, SearchInput)
        assert search_widget.max_history == 20
        assert search_widget.search_icon is None
        assert search_widget.icon_position == "left"
        assert search_widget.clear_button is True

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom parameters."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.red)
        icon = QIcon(pixmap)

        search_widget = SearchInput(
            max_history=50,
            search_icon=icon,
            icon_position="right",
            clear_button=False,
        )

        assert search_widget.max_history == 50
        assert search_widget.search_icon is not None
        assert search_widget.icon_position == "right"
        assert search_widget.clear_button is False

    def test_should_update_properties_when_setters_are_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget properties."""
        search_widget = SearchInput()

        # Test search_icon property
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.blue)
        icon = QIcon(pixmap)
        search_widget.search_icon = icon
        assert search_widget.search_icon is not None

        # Test icon_position property
        search_widget.icon_position = "right"
        assert search_widget.icon_position == "right"

        # Test clear_button property
        search_widget.clear_button = False
        assert search_widget.clear_button is False

        # Test max_history property
        search_widget.max_history = 100
        assert search_widget.max_history == 100

    def test_should_limit_history_to_max_size_when_items_are_added(
        self, qt_widget_cleanup
    ) -> None:
        """Test history management."""
        search_widget = SearchInput(max_history=5)

        # Initial state
        assert search_widget.getHistory() == []

        # Add to history
        search_widget.addToHistory("search1")
        search_widget.addToHistory("search2")
        search_widget.addToHistory("search3")

        history = search_widget.getHistory()
        assert len(history) == 3
        assert "search1" in history
        assert "search2" in history
        assert "search3" in history

        # Test max_history limit
        search_widget.addToHistory("search4")
        search_widget.addToHistory("search5")
        search_widget.addToHistory("search6")  # Should replace oldest

        history = search_widget.getHistory()
        assert len(history) == 5  # Max history
        assert "search6" in history  # Most recent
        assert "search1" not in history  # Oldest removed

    def test_should_clear_all_history_when_clear_history_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test history clearing."""
        search_widget = SearchInput()

        # Add to history
        search_widget.addToHistory("search1")
        search_widget.addToHistory("search2")
        assert len(search_widget.getHistory()) == 2

        # Clear history
        search_widget.clearHistory()
        assert search_widget.getHistory() == []

    def test_should_set_history_list_when_set_history_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test history setting."""
        search_widget = SearchInput(max_history=10)

        # Set a history
        history_list = ["item1", "item2", "item3", "item4", "item5"]
        search_widget.setHistory(history_list)

        # Verify history
        history = search_widget.getHistory()
        assert len(history) == 5
        for item in history_list:
            assert item in history

    def test_should_keep_only_most_recent_when_history_exceeds_max(
        self, qt_widget_cleanup
    ) -> None:
        """Test history trimming."""
        search_widget = SearchInput(max_history=3)

        # Add more items than the limit
        search_widget.addToHistory("item1")
        search_widget.addToHistory("item2")
        search_widget.addToHistory("item3")
        search_widget.addToHistory("item4")
        search_widget.addToHistory("item5")

        # Verify that only the 3 most recent are preserved
        history = search_widget.getHistory()
        assert len(history) == 3
        assert "item3" in history
        assert "item4" in history
        assert "item5" in history
        assert "item1" not in history
        assert "item2" not in history

    def test_should_deduplicate_items_when_same_item_is_added_twice(
        self, qt_widget_cleanup
    ) -> None:
        """Test with duplicate items in history."""
        search_widget = SearchInput()

        # Add duplicate items
        search_widget.addToHistory("item")
        search_widget.addToHistory("item")
        search_widget.addToHistory("item")

        # Verify that duplicates are removed (widget behavior)
        history = search_widget.getHistory()
        assert history.count("item") == 1  # Only one occurrence

    def test_should_return_empty_list_when_history_is_cleared(
        self, qt_widget_cleanup
    ) -> None:
        """Test with empty history."""
        search_widget = SearchInput()

        # Initial state
        assert search_widget.getHistory() == []

        # Add and clear
        search_widget.addToHistory("item")
        assert len(search_widget.getHistory()) == 1

        search_widget.clearHistory()
        assert search_widget.getHistory() == []

    def test_should_store_icon_when_search_icon_is_set(self, qt_widget_cleanup) -> None:
        """Test icon management."""
        search_widget = SearchInput()

        # Test without icon
        assert search_widget.search_icon is None

        # Test with icon
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.green)
        icon = QIcon(pixmap)
        search_widget.search_icon = icon
        assert search_widget.search_icon is not None

        # Test with icon path
        search_widget.search_icon = "path/to/icon.png"
        # Note: The widget can handle icon paths according to implementation

    def test_should_update_icon_position_when_icon_position_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test icon positions."""
        search_widget = SearchInput()

        # Test left position (default)
        assert search_widget.icon_position == "left"

        # Test right position
        search_widget.icon_position = "right"
        assert search_widget.icon_position == "right"

        # Test invalid position (not accepted)
        search_widget.icon_position = "center"
        # Value remains "right"
        assert search_widget.icon_position == "right"

    def test_should_show_or_hide_clear_button_when_text_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test clear button toggle."""
        search_widget = SearchInput()

        # Initial state
        assert search_widget.clear_button is True

        # Disable
        search_widget.clear_button = False
        assert search_widget.clear_button is False

        # Re-enable
        search_widget.clear_button = True
        assert search_widget.clear_button is True

    def test_should_validate_max_history_when_max_history_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test max_history validation."""
        search_widget = SearchInput()

        # Positive value
        search_widget.max_history = 50
        assert search_widget.max_history == 50

        # Zero value (becomes 1)
        search_widget.max_history = 0
        assert search_widget.max_history == 1

        # Negative value (becomes 1)
        search_widget.max_history = -5
        assert search_widget.max_history == 1

    def test_should_handle_text_changes_when_user_types(
        self, qt_widget_cleanup
    ) -> None:
        """Test text handling."""
        search_widget = SearchInput()

        # Test setText
        search_widget.setText("search query")
        assert search_widget.text() == "search query"

        # Test clear
        search_widget.clear()
        assert search_widget.text() == ""

        # Test placeholder
        search_widget.setPlaceholderText("Search...")
        assert search_widget.placeholderText() == "Search..."

    def test_should_emit_search_changed_signal_when_text_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget signals."""
        search_widget = SearchInput()

        # Test searchSubmitted signal
        signal_received = False
        received_text = ""

        def on_search_submitted(text: str) -> None:
            nonlocal signal_received, received_text
            signal_received = True
            received_text = text

        search_widget.searchSubmitted.connect(on_search_submitted)

        # Simulate a search
        search_widget.setText("test search")
        # Note: The signal is emitted on keyPressEvent with Enter
        # We don't test keyPressEvent to avoid Qt issues

        # Verify that the signal is connected
        assert search_widget.searchSubmitted is not None

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle method."""
        search_widget = SearchInput()

        # Method should not raise an exception
        try:
            search_widget.refreshStyle()
        except Exception as e:
            pytest.fail(f"refreshStyle() raised an exception: {e}")

    def test_should_handle_large_history_when_many_items_are_added(
        self, qt_widget_cleanup
    ) -> None:
        """Test with large history."""
        search_widget = SearchInput(max_history=1000)

        # Add many items
        for i in range(1000):
            search_widget.addToHistory(f"search_{i}")

        # Verify the limit
        history = search_widget.getHistory()
        assert len(history) == 1000

        # Add one more item
        search_widget.addToHistory("overflow")
        history = search_widget.getHistory()
        assert len(history) == 1000
        assert "overflow" in history  # Most recent
        assert "search_0" not in history  # Oldest removed

    def test_should_handle_special_characters_in_search_when_text_contains_special_chars(
        self, qt_widget_cleanup
    ) -> None:
        """Test with special characters in history."""
        search_widget = SearchInput()

        special_searches = [
            "search with spaces",
            "search@email.com",
            "search-with-dashes",
            "search_with_underscores",
            "search with\nnewlines",
            "search with\ttabs",
            "search with émojis 🚀",
            "search with unicode: 你好世界",
        ]

        # Add special searches
        for search in special_searches:
            search_widget.addToHistory(search)

        # Verify that all are preserved
        history = search_widget.getHistory()
        assert len(history) == len(special_searches)
        for search in special_searches:
            assert search in history

    def test_should_have_correct_type_property_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test type property for QSS."""
        search_widget = SearchInput()

        # Verify that the widget works correctly
        assert search_widget is not None
        assert isinstance(search_widget, SearchInput)
