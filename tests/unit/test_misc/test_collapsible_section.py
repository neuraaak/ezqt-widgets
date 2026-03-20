# ///////////////////////////////////////////////////////////////
# TEST_COLLAPSIBLE_SECTION - CollapsibleSection Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for CollapsibleSection widget.

Tests for the accordion-style collapsible section widget.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtWidgets import QApplication, QLabel, QWidget

# Local imports
from ezqt_widgets.widgets.misc.collapsible_section import CollapsibleSection

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestCollapsibleSection:
    """Tests for CollapsibleSection class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        section = CollapsibleSection()

        assert section is not None
        assert isinstance(section, CollapsibleSection)
        assert section.title == ""
        assert section.is_expanded is True

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom keyword arguments."""
        section = CollapsibleSection(title="My Section", expanded=False)

        assert section.title == "My Section"
        assert section.is_expanded is False

    def test_should_update_title_when_title_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test title property setter."""
        section = CollapsibleSection(title="Original")

        section.title = "Updated Title"
        assert section.title == "Updated Title"

    def test_should_expand_when_expand_is_called_on_collapsed_section(
        self, qt_widget_cleanup
    ) -> None:
        """Test expand() transitions from collapsed to expanded."""
        section = CollapsibleSection(expanded=False)

        assert not section.is_expanded
        section.expand()
        assert section.is_expanded

    def test_should_collapse_when_collapse_is_called_on_expanded_section(
        self, qt_widget_cleanup
    ) -> None:
        """Test collapse() transitions from expanded to collapsed."""
        section = CollapsibleSection(expanded=True)

        assert section.is_expanded
        section.collapse()
        assert not section.is_expanded

    def test_should_toggle_state_when_toggle_is_called(self, qt_widget_cleanup) -> None:
        """Test toggle() flips the expanded state."""
        section = CollapsibleSection(expanded=True)

        section.toggle()
        assert not section.is_expanded

        section.toggle()
        assert section.is_expanded

    def test_should_not_change_state_when_expand_is_called_twice(
        self, qt_widget_cleanup
    ) -> None:
        """Test that expand() is idempotent when already expanded."""
        section = CollapsibleSection(expanded=True)

        received: list[bool] = []
        section.expandedChanged.connect(received.append)

        section.expand()  # Already expanded — should not emit
        assert len(received) == 0
        assert section.is_expanded

    def test_should_not_change_state_when_collapse_is_called_twice(
        self, qt_widget_cleanup
    ) -> None:
        """Test that collapse() is idempotent when already collapsed."""
        section = CollapsibleSection(expanded=False)

        received: list[bool] = []
        section.expandedChanged.connect(received.append)

        section.collapse()  # Already collapsed — should not emit
        assert len(received) == 0
        assert not section.is_expanded

    def test_should_emit_expanded_changed_when_state_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test expandedChanged signal emission on state changes."""
        section = CollapsibleSection(expanded=True)

        received: list[bool] = []
        section.expandedChanged.connect(received.append)

        section.collapse()
        assert len(received) == 1
        assert received[0] is False

        section.expand()
        assert len(received) == 2
        assert received[1] is True

    def test_should_set_content_widget_when_set_content_widget_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test setContentWidget() accepts any QWidget."""
        section = CollapsibleSection(title="Content Test", expanded=True)
        content = QLabel("I am the content")

        try:
            section.setContentWidget(content)
        except Exception as exc:
            pytest.fail(f"setContentWidget() raised: {exc}")

        assert section._content_widget is content

    def test_should_replace_content_when_set_content_widget_is_called_twice(
        self, qt_widget_cleanup
    ) -> None:
        """Test that calling setContentWidget() again replaces the content."""
        section = CollapsibleSection(expanded=True)
        first = QLabel("First content")
        second = QLabel("Second content")

        section.setContentWidget(first)
        section.setContentWidget(second)

        assert section._content_widget is second

    def test_should_have_header_always_visible(self, qt_widget_cleanup) -> None:
        """Test that the header widget is always visible regardless of state."""
        section = CollapsibleSection(title="Header Test", expanded=False)

        assert section._header.isVisible() or not section.isVisible()
        # After showing, header must be visible
        section.show()
        QApplication.processEvents()
        assert section._header.isVisible()

    def test_should_not_raise_when_set_theme_is_called(self, qt_widget_cleanup) -> None:
        """Test setTheme() does not raise for dark and light themes."""
        section = CollapsibleSection()

        try:
            section.setTheme("dark")
            section.setTheme("light")
        except Exception as exc:
            pytest.fail(f"setTheme() raised an exception: {exc}")

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle() does not raise."""
        section = CollapsibleSection()

        try:
            section.refreshStyle()
        except Exception as exc:
            pytest.fail(f"refreshStyle() raised an exception: {exc}")

    def test_should_handle_empty_title_when_title_is_empty_string(
        self, qt_widget_cleanup
    ) -> None:
        """Test section creation with empty title string."""
        section = CollapsibleSection(title="")
        assert section.title == ""

        section.title = "New title"
        assert section.title == "New title"

    def test_should_handle_toggle_on_collapsed_section_with_content(
        self, qt_widget_cleanup
    ) -> None:
        """Test toggle with content widget set."""
        section = CollapsibleSection(expanded=False)
        content = QWidget()
        content.setFixedHeight(100)
        section.setContentWidget(content)

        section.toggle()  # expand
        assert section.is_expanded

        section.toggle()  # collapse
        assert not section.is_expanded
