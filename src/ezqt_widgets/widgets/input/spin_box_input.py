# ///////////////////////////////////////////////////////////////
# SPIN_BOX_INPUT - Spin Box Input Widget
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Spin box input widget module.

Provides a fully custom numeric spin box widget with integrated decrement
and increment buttons, mouse wheel support, and real-time validation.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator, QWheelEvent
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QSizePolicy,
    QToolButton,
    QWidget,
)

# Local imports
from ...types import WidgetParent

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class SpinBoxInput(QWidget):
    """Custom numeric spin box with integrated decrement and increment buttons.

    Provides a fully stylable numeric input with − and + buttons flanking
    a central QLineEdit. Supports mouse wheel increments and real-time
    QIntValidator clamping.

    Features:
        - Decrement (−) and increment (+) QToolButtons
        - Central QLineEdit with QIntValidator
        - Mouse wheel increments/decrements by step
        - Value clamped between minimum and maximum at all times
        - Optional prefix and suffix labels
        - Signal emitted only when value changes

    Args:
        parent: The parent widget (default: None).
        value: Initial value (default: 0).
        minimum: Minimum allowed value (default: 0).
        maximum: Maximum allowed value (default: 100).
        step: Step size for increment/decrement (default: 1).
        prefix: String prepended to the displayed value (default: "").
        suffix: String appended to the displayed value (default: "").

    Properties:
        value: Get or set the current integer value.
        minimum: Get or set the minimum allowed value.
        maximum: Get or set the maximum allowed value.
        step: Get or set the step size.
        prefix: Get or set the display prefix.
        suffix: Get or set the display suffix.

    Signals:
        valueChanged(int): Emitted when the value changes.

    Example:
        >>> from ezqt_widgets import SpinBoxInput
        >>> spin = SpinBoxInput(value=10, minimum=0, maximum=100, step=5)
        >>> spin.valueChanged.connect(lambda v: print(f"Value: {v}"))
        >>> spin.show()
    """

    valueChanged = Signal(int)

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        parent: WidgetParent = None,
        *,
        value: int = 0,
        minimum: int = 0,
        maximum: int = 100,
        step: int = 1,
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """Initialize the spin box input."""
        super().__init__(parent)
        self.setProperty("type", "SpinBoxInput")

        # Initialize private state
        self._minimum: int = minimum
        self._maximum: int = maximum
        self._step: int = max(1, step)
        self._prefix: str = prefix
        self._suffix: str = suffix
        self._value: int = max(minimum, min(maximum, value))

        # Enable mouse wheel focus
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        # Setup UI
        self._setup_widget()

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _setup_widget(self) -> None:
        """Setup the widget layout and child components."""
        # Decrement button
        self._btn_dec = QToolButton()
        self._btn_dec.setText("−")
        self._btn_dec.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self._btn_dec.setCursor(Qt.CursorShape.PointingHandCursor)
        self._btn_dec.clicked.connect(self.stepDown)

        # Central QLineEdit
        self._line_edit = QLineEdit()
        self._line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._line_edit.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self._validator = QIntValidator(self._minimum, self._maximum)
        self._line_edit.setValidator(self._validator)
        self._line_edit.editingFinished.connect(self._on_editing_finished)
        self._line_edit.textChanged.connect(self._on_text_changed)

        # Increment button
        self._btn_inc = QToolButton()
        self._btn_inc.setText("+")
        self._btn_inc.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self._btn_inc.setCursor(Qt.CursorShape.PointingHandCursor)
        self._btn_inc.clicked.connect(self.stepUp)

        # Layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self._btn_dec)
        layout.addWidget(self._line_edit)
        layout.addWidget(self._btn_inc)

        # Initial display
        self._update_display()

    def _update_display(self) -> None:
        """Refresh the QLineEdit text with prefix, value, and suffix."""
        # Block signals to avoid re-entrant _on_text_changed
        self._line_edit.blockSignals(True)
        self._line_edit.setText(f"{self._prefix}{self._value}{self._suffix}")
        self._line_edit.blockSignals(False)

    def _on_editing_finished(self) -> None:
        """Commit the text value on editing finished."""
        raw = self._line_edit.text()
        # Strip prefix/suffix before parsing
        raw = raw.removeprefix(self._prefix).removesuffix(self._suffix)
        try:
            parsed = int(raw)
        except ValueError:
            self._update_display()
            return
        self.setValue(parsed)

    def _on_text_changed(self, text: str) -> None:
        """Attempt live parsing; silently ignore incomplete input.

        Args:
            text: The current text in the QLineEdit.
        """
        raw = text.removeprefix(self._prefix).removesuffix(self._suffix)
        try:
            parsed = int(raw)
            clamped = max(self._minimum, min(self._maximum, parsed))
            if clamped != self._value:
                # Do not call setValue to avoid display loop; update state only
                self._value = clamped
                self.valueChanged.emit(self._value)
        except ValueError:
            pass

    # ///////////////////////////////////////////////////////////////
    # PROPERTIES
    # ///////////////////////////////////////////////////////////////

    @property
    def value(self) -> int:
        """Get the current integer value.

        Returns:
            The current value.
        """
        return self._value

    @value.setter
    def value(self, val: int) -> None:
        """Set the current value, clamped between minimum and maximum.

        Args:
            val: The new value.
        """
        self.setValue(val)

    @property
    def minimum(self) -> int:
        """Get the minimum allowed value.

        Returns:
            The current minimum.
        """
        return self._minimum

    @minimum.setter
    def minimum(self, val: int) -> None:
        """Set the minimum allowed value.

        Args:
            val: The new minimum value.
        """
        self._minimum = int(val)
        self._validator.setBottom(self._minimum)
        self.setValue(self._value)

    @property
    def maximum(self) -> int:
        """Get the maximum allowed value.

        Returns:
            The current maximum.
        """
        return self._maximum

    @maximum.setter
    def maximum(self, val: int) -> None:
        """Set the maximum allowed value.

        Args:
            val: The new maximum value.
        """
        self._maximum = int(val)
        self._validator.setTop(self._maximum)
        self.setValue(self._value)

    @property
    def step(self) -> int:
        """Get the step size for increment/decrement.

        Returns:
            The current step size.
        """
        return self._step

    @step.setter
    def step(self, val: int) -> None:
        """Set the step size for increment/decrement.

        Args:
            val: The new step size (minimum 1).
        """
        self._step = max(1, int(val))

    @property
    def prefix(self) -> str:
        """Get the display prefix.

        Returns:
            The current prefix string.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, val: str) -> None:
        """Set the display prefix.

        Args:
            val: The new prefix string.
        """
        self._prefix = str(val)
        self._update_display()

    @property
    def suffix(self) -> str:
        """Get the display suffix.

        Returns:
            The current suffix string.
        """
        return self._suffix

    @suffix.setter
    def suffix(self, val: str) -> None:
        """Set the display suffix.

        Args:
            val: The new suffix string.
        """
        self._suffix = str(val)
        self._update_display()

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def setValue(self, value: int) -> None:
        """Set the value, clamped between minimum and maximum.

        Args:
            value: The new value to set.
        """
        clamped = max(self._minimum, min(self._maximum, int(value)))
        if clamped != self._value:
            self._value = clamped
            self._update_display()
            self.valueChanged.emit(self._value)
        else:
            # Always refresh display to show prefix/suffix
            self._update_display()

    def stepUp(self) -> None:
        """Increment the value by step, clamped at maximum."""
        self.setValue(self._value + self._step)

    def stepDown(self) -> None:
        """Decrement the value by step, clamped at minimum."""
        self.setValue(self._value - self._step)

    # ///////////////////////////////////////////////////////////////
    # EVENT HANDLERS
    # ///////////////////////////////////////////////////////////////

    def wheelEvent(self, event: QWheelEvent) -> None:
        """Handle mouse wheel to increment or decrement by step.

        Args:
            event: The wheel event.
        """
        delta = event.angleDelta().y()
        if delta > 0:
            self.stepUp()
        elif delta < 0:
            self.stepDown()
        event.accept()

    # ///////////////////////////////////////////////////////////////
    # STYLE METHODS
    # ///////////////////////////////////////////////////////////////

    def refreshStyle(self) -> None:
        """Refresh the widget style.

        Useful after dynamic stylesheet changes.
        """
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()


# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = ["SpinBoxInput"]
