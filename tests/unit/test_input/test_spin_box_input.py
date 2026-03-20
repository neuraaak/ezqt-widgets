# ///////////////////////////////////////////////////////////////
# TEST_SPIN_BOX_INPUT - SpinBoxInput Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for SpinBoxInput widget.

Tests for the custom numeric spin box with integrated decrement and
increment buttons.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QWheelEvent

# Local imports
from ezqt_widgets.widgets.input.spin_box_input import SpinBoxInput

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestSpinBoxInput:
    """Tests for SpinBoxInput class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        spin = SpinBoxInput()

        assert spin is not None
        assert isinstance(spin, SpinBoxInput)
        assert spin.value == 0
        assert spin.minimum == 0
        assert spin.maximum == 100
        assert spin.step == 1
        assert spin.prefix == ""
        assert spin.suffix == ""

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom keyword arguments."""
        spin = SpinBoxInput(
            value=50,
            minimum=10,
            maximum=200,
            step=5,
            prefix="$",
            suffix=" items",
        )

        assert spin.value == 50
        assert spin.minimum == 10
        assert spin.maximum == 200
        assert spin.step == 5
        assert spin.prefix == "$"
        assert spin.suffix == " items"

    def test_should_clamp_initial_value_when_value_is_out_of_range(
        self, qt_widget_cleanup
    ) -> None:
        """Test that initial value is clamped to [minimum, maximum]."""
        spin_low = SpinBoxInput(value=-50, minimum=0, maximum=100)
        assert spin_low.value == 0

        spin_high = SpinBoxInput(value=200, minimum=0, maximum=100)
        assert spin_high.value == 100

    def test_should_update_value_when_set_value_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test setValue() clamps and updates."""
        spin = SpinBoxInput(minimum=0, maximum=100)

        spin.setValue(42)
        assert spin.value == 42

        spin.setValue(-10)  # Below minimum
        assert spin.value == 0

        spin.setValue(150)  # Above maximum
        assert spin.value == 100

    def test_should_update_value_via_property_setter(self, qt_widget_cleanup) -> None:
        """Test value property setter."""
        spin = SpinBoxInput(minimum=0, maximum=50)

        spin.value = 25
        assert spin.value == 25

    def test_should_increment_value_when_step_up_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test stepUp() increments by step and clamps at maximum."""
        spin = SpinBoxInput(value=95, minimum=0, maximum=100, step=10)

        spin.stepUp()
        assert spin.value == 100  # Clamped at maximum

        spin.setValue(50)
        spin.stepUp()
        assert spin.value == 60

    def test_should_decrement_value_when_step_down_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test stepDown() decrements by step and clamps at minimum."""
        spin = SpinBoxInput(value=5, minimum=0, maximum=100, step=10)

        spin.stepDown()
        assert spin.value == 0  # Clamped at minimum

        spin.setValue(50)
        spin.stepDown()
        assert spin.value == 40

    def test_should_update_minimum_when_minimum_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test minimum property setter re-clamps current value."""
        spin = SpinBoxInput(value=5, minimum=0, maximum=100)

        spin.minimum = 10
        assert spin.minimum == 10
        assert spin.value == 10  # Re-clamped

    def test_should_update_maximum_when_maximum_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test maximum property setter re-clamps current value."""
        spin = SpinBoxInput(value=80, minimum=0, maximum=100)

        spin.maximum = 50
        assert spin.maximum == 50
        assert spin.value == 50  # Re-clamped

    def test_should_clamp_step_to_minimum_1_when_set_to_zero_or_negative(
        self, qt_widget_cleanup
    ) -> None:
        """Test that step is always at least 1."""
        spin = SpinBoxInput()

        spin.step = 0
        assert spin.step == 1

        spin.step = -5
        assert spin.step == 1

        spin.step = 10
        assert spin.step == 10

    def test_should_update_prefix_when_prefix_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test prefix property setter."""
        spin = SpinBoxInput()

        spin.prefix = "€"
        assert spin.prefix == "€"

    def test_should_update_suffix_when_suffix_setter_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test suffix property setter."""
        spin = SpinBoxInput()

        spin.suffix = " kg"
        assert spin.suffix == " kg"

    def test_should_emit_value_changed_signal_when_value_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test valueChanged signal emission."""
        spin = SpinBoxInput(value=10)

        received: list[int] = []
        spin.valueChanged.connect(received.append)

        spin.setValue(20)
        assert len(received) == 1
        assert received[0] == 20

    def test_should_not_emit_value_changed_when_value_is_unchanged(
        self, qt_widget_cleanup
    ) -> None:
        """Test that valueChanged is NOT emitted when value does not change."""
        spin = SpinBoxInput(value=50)

        received: list[int] = []
        spin.valueChanged.connect(received.append)

        spin.setValue(50)  # Same value
        assert len(received) == 0

    def test_should_increment_on_wheel_up_event(self, qt_widget_cleanup) -> None:
        """Test mouse wheel up increments the value."""
        spin = SpinBoxInput(value=10, minimum=0, maximum=100, step=5)

        wheel_event = QWheelEvent(
            QPoint(0, 0),
            spin.mapToGlobal(QPoint(0, 0)),
            QPoint(0, 120),
            QPoint(0, 120),
            Qt.MouseButton.NoButton,
            Qt.KeyboardModifier.NoModifier,
            Qt.ScrollPhase.NoScrollPhase,
            False,
        )
        spin.wheelEvent(wheel_event)

        assert spin.value == 15

    def test_should_decrement_on_wheel_down_event(self, qt_widget_cleanup) -> None:
        """Test mouse wheel down decrements the value."""
        spin = SpinBoxInput(value=10, minimum=0, maximum=100, step=5)

        wheel_event = QWheelEvent(
            QPoint(0, 0),
            spin.mapToGlobal(QPoint(0, 0)),
            QPoint(0, -120),
            QPoint(0, -120),
            Qt.MouseButton.NoButton,
            Qt.KeyboardModifier.NoModifier,
            Qt.ScrollPhase.NoScrollPhase,
            False,
        )
        spin.wheelEvent(wheel_event)

        assert spin.value == 5

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle() does not raise."""
        spin = SpinBoxInput()

        try:
            spin.refreshStyle()
        except Exception as exc:
            pytest.fail(f"refreshStyle() raised an exception: {exc}")

    def test_should_handle_equal_min_max_when_range_is_degenerate(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget with minimum == maximum."""
        spin = SpinBoxInput(value=5, minimum=5, maximum=5)

        assert spin.value == 5
        spin.stepUp()
        assert spin.value == 5
        spin.stepDown()
        assert spin.value == 5
