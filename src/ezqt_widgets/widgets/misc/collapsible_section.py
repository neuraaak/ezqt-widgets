# ///////////////////////////////////////////////////////////////
# COLLAPSIBLE_SECTION - Collapsible Section Widget
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Collapsible section widget module.

Provides an accordion-style section widget with a clickable header and
smooth expand/collapse animation using QPropertyAnimation on maximumHeight.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import contextlib

# Third-party imports
from PySide6.QtCore import (
    QEasingCurve,
    QPropertyAnimation,
    QSize,
    Qt,
    Signal,
)
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

# Local imports
from ...types import WidgetParent
from .toggle_icon import ToggleIcon

# ///////////////////////////////////////////////////////////////
# CONSTANTS
# ///////////////////////////////////////////////////////////////

_ANIMATION_DURATION: int = 200

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class _HeaderWidget(QWidget):
    """Internal clickable header for CollapsibleSection.

    Emits a clicked signal when the user presses anywhere on the header.
    """

    clicked = Signal()

    def __init__(self, parent: WidgetParent = None) -> None:
        """Initialize the header widget."""
        super().__init__(parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Emit clicked on left mouse button press.

        Args:
            event: The mouse event.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class CollapsibleSection(QWidget):
    """Accordion-style section widget with animated expand/collapse.

    The header is always visible. Clicking anywhere on the header (or
    calling toggle()) animates the content area between 0 height and its
    natural size hint height.

    Features:
        - Clickable header with title label and ToggleIcon chevron
        - Smooth height animation via QPropertyAnimation on maximumHeight
        - Supports an arbitrary QWidget as content via setContentWidget()
        - expand()/collapse()/toggle() public API
        - Theme propagation to the ToggleIcon chevron

    Args:
        parent: The parent widget (default: None).
        title: Header title text (default: "").
        expanded: Initial expanded state (default: True).

    Properties:
        title: Get or set the header title text.
        is_expanded: Get the current expanded state.

    Signals:
        expandedChanged(bool): Emitted when the expanded state changes.

    Example:
        >>> from ezqt_widgets import CollapsibleSection
        >>> section = CollapsibleSection(title="Settings", expanded=False)
        >>> section.setContentWidget(my_form_widget)
        >>> section.expandedChanged.connect(lambda e: print(f"Expanded: {e}"))
        >>> section.show()
    """

    expandedChanged = Signal(bool)

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        parent: WidgetParent = None,
        *,
        title: str = "",
        expanded: bool = True,
    ) -> None:
        """Initialize the collapsible section."""
        super().__init__(parent)
        self.setProperty("type", "CollapsibleSection")

        # Initialize private state
        self._expanded: bool = expanded
        self._content_widget: QWidget | None = None
        self._animation: QPropertyAnimation | None = None

        # Setup UI
        self._setup_widget(title)
        self._setup_animation()

        # Apply initial state without animation
        self._apply_initial_state()

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _setup_widget(self, title: str) -> None:
        """Setup the widget layout, header, and content area.

        Args:
            title: Initial header title text.
        """
        # ---- Header ----
        self._header = _HeaderWidget(self)
        self._header.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        self._title_label = QLabel(title)
        self._title_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        # ToggleIcon acts as chevron: "opened" = expanded, "closed" = collapsed
        self._toggle_icon = ToggleIcon(
            icon_size=14,
            initial_state="opened" if self._expanded else "closed",
        )
        self._toggle_icon.setFixedSize(QSize(20, 20))

        header_layout = QHBoxLayout(self._header)
        header_layout.setContentsMargins(8, 6, 8, 6)
        header_layout.setSpacing(6)
        header_layout.addWidget(self._toggle_icon)
        header_layout.addWidget(self._title_label)
        header_layout.addStretch()

        self._header.clicked.connect(self.toggle)

        # ---- Content area ----
        self._content_area = QWidget()
        self._content_area.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        self._content_layout = QVBoxLayout(self._content_area)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(0)

        # ---- Main layout ----
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self._header)
        main_layout.addWidget(self._content_area)

    def _setup_animation(self) -> None:
        """Setup the QPropertyAnimation on maximumHeight of the content area."""
        self._animation = QPropertyAnimation(self._content_area, b"maximumHeight")
        self._animation.setDuration(_ANIMATION_DURATION)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

    def _apply_initial_state(self) -> None:
        """Apply the initial expanded/collapsed state without animation."""
        if self._expanded:
            # Allow natural height
            self._content_area.setMaximumHeight(16777215)  # Qt QWIDGETSIZE_MAX
        else:
            self._content_area.setMaximumHeight(0)

    def _get_content_height(self) -> int:
        """Calculate the target expanded height of the content area.

        Returns:
            The content area's size hint height, minimum 0.
        """
        if self._content_widget is not None:
            hint = self._content_widget.sizeHint().height()
        else:
            hint = self._content_area.sizeHint().height()
        return max(0, hint)

    def _run_animation(self, expanding: bool) -> None:
        """Run the expand or collapse animation.

        Args:
            expanding: True to expand, False to collapse.
        """
        if self._animation is None:
            return

        current = self._content_area.maximumHeight()
        # Cap the current value to avoid QWIDGETSIZE_MAX as start
        if current > 16777214:
            current = self._get_content_height()

        if expanding:
            end = self._get_content_height()
            if end == 0:
                end = 100  # Fallback height for empty content
        else:
            end = 0

        self._animation.setStartValue(current)
        self._animation.setEndValue(end)
        self._animation.start()

        # After expanding, release the maximum height cap
        if expanding:
            self._animation.finished.connect(self._on_expand_finished)

    def _on_expand_finished(self) -> None:
        """Release the maximumHeight cap after expand animation completes."""
        with contextlib.suppress(RuntimeError):
            self._animation.finished.disconnect(self._on_expand_finished)  # type: ignore[union-attr]
        self._content_area.setMaximumHeight(16777215)

    # ///////////////////////////////////////////////////////////////
    # PROPERTIES
    # ///////////////////////////////////////////////////////////////

    @property
    def title(self) -> str:
        """Get the header title text.

        Returns:
            The current title string.
        """
        return self._title_label.text()

    @title.setter
    def title(self, value: str) -> None:
        """Set the header title text.

        Args:
            value: The new title string.
        """
        self._title_label.setText(str(value))

    @property
    def is_expanded(self) -> bool:
        """Get the current expanded state.

        Returns:
            True if the section is expanded, False if collapsed.
        """
        return self._expanded

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def setContentWidget(self, widget: QWidget) -> None:
        """Set the widget displayed in the collapsible content area.

        Replaces any previously set content widget. The section keeps
        its current expanded/collapsed state.

        Args:
            widget: The widget to display as content.
        """
        # Remove previous content
        if self._content_widget is not None:
            self._content_layout.removeWidget(self._content_widget)
            self._content_widget.setParent(None)  # type: ignore[call-overload]

        self._content_widget = widget
        self._content_layout.addWidget(widget)

        # Re-apply state to reflect new content height
        self._apply_initial_state()

    def expand(self) -> None:
        """Expand the content area with animation."""
        if self._expanded:
            return
        self._expanded = True
        self._toggle_icon.setStateOpened()
        self._run_animation(expanding=True)
        self.expandedChanged.emit(True)

    def collapse(self) -> None:
        """Collapse the content area with animation."""
        if not self._expanded:
            return
        self._expanded = False
        self._toggle_icon.setStateClosed()
        self._run_animation(expanding=False)
        self.expandedChanged.emit(False)

    def toggle(self) -> None:
        """Toggle between expanded and collapsed states."""
        if self._expanded:
            self.collapse()
        else:
            self.expand()

    def setTheme(self, theme: str) -> None:
        """Update the toggle icon color for the given theme.

        Can be connected directly to a theme-change signal to keep
        the icon in sync with the application's color scheme.

        Args:
            theme: The new theme (``"dark"`` or ``"light"``).
        """
        self._toggle_icon.setTheme(theme)

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

__all__ = ["CollapsibleSection"]
