# ///////////////////////////////////////////////////////////////
# TEST_TOGGLE_SWITCH - ToggleSwitch Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for ToggleSwitch widget.

Tests for the modern toggle switch widget.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent

# Local imports
from ezqt_widgets.widgets.misc.toggle_switch import ToggleSwitch

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestToggleSwitch:
    """Test cases for ToggleSwitch widget."""

    def test_should_have_default_properties_when_created(self, qt_application) -> None:
        """Test ToggleSwitch creation with default parameters."""
        switch = ToggleSwitch()

        assert not switch.checked  # Default state
        assert switch.width == 50
        assert switch.height == 24
        assert switch.animation  # Animation enabled by default

    def test_should_use_custom_colors_when_created_with_parameters(
        self, qt_application
    ) -> None:
        """Test ToggleSwitch creation with custom parameters."""
        switch = ToggleSwitch(checked=True, width=80, height=30, animation=False)

        assert switch.checked
        assert switch.width == 80
        assert switch.height == 30
        assert not switch.animation

    def test_should_update_state_when_set_checked_is_called(
        self, qt_application
    ) -> None:
        """Test setting checked state."""
        switch = ToggleSwitch()

        switch.checked = True
        assert switch.checked

        switch.checked = False
        assert not switch.checked

    def test_should_change_state_when_toggle_is_called(self, qt_application) -> None:
        """Test toggling the switch."""
        switch = ToggleSwitch(checked=False)

        # Toggle from False to True
        switch.toggle()
        assert switch.checked

        # Toggle from True to False
        switch.toggle()
        assert not switch.checked

    def test_should_update_width_when_set_width_is_called(self, qt_application) -> None:
        """Test setting width."""
        switch = ToggleSwitch()

        switch.width = 100
        assert switch.width == 100

    def test_should_update_height_when_set_height_is_called(
        self, qt_application
    ) -> None:
        """Test setting height."""
        switch = ToggleSwitch()

        switch.height = 40
        assert switch.height == 40

    def test_should_configure_animation_duration_when_set_animation_is_called(
        self, qt_application
    ) -> None:
        """Test setting animation."""
        switch = ToggleSwitch()

        switch.animation = False
        assert not switch.animation

        switch.animation = True
        assert switch.animation

    def test_should_emit_toggled_signal_when_state_changes(
        self, qt_application
    ) -> None:
        """Test toggle switch signals."""
        switch = ToggleSwitch()

        toggled_called = False

        def on_toggled(_state: bool) -> None:
            nonlocal toggled_called
            toggled_called = True

        switch.toggled.connect(on_toggled)

        # Toggle the switch
        switch.toggle()
        assert toggled_called

    def test_should_return_valid_size_hints_when_queried(
        self, qt_widget_cleanup
    ) -> None:
        """Test size hint methods."""
        switch = ToggleSwitch()

        # Force widget initialization
        switch.show()
        switch.resize(100, 100)

        size_hint = switch.sizeHint()
        assert size_hint.width() == 50  # Default width
        assert size_hint.height() == 24  # Default height

        min_size_hint = switch.minimumSizeHint()
        assert min_size_hint.width() == 50
        assert min_size_hint.height() == 24

    def test_should_toggle_state_when_mouse_is_pressed(self, qt_widget_cleanup) -> None:
        """Test mouse press event."""
        switch = ToggleSwitch(checked=False)
        initial_state = switch.checked

        # Simulate mouse press with real Qt event
        mouse_event = QMouseEvent(
            QMouseEvent.Type.MouseButtonPress,
            QPoint(10, 10),
            QPoint(10, 10),
            Qt.MouseButton.LeftButton,
            Qt.MouseButton.LeftButton,
            Qt.KeyboardModifier.NoModifier,
        )
        switch.mousePressEvent(mouse_event)

        # State should have changed
        assert switch.checked != initial_state
