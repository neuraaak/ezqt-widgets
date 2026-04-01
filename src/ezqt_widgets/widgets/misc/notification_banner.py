# ///////////////////////////////////////////////////////////////
# NOTIFICATION_BANNER - Notification Banner Widget
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Notification banner widget module.

Provides an animated slide-down notification banner that overlays the top
of a parent widget, supporting INFO, WARNING, ERROR, and SUCCESS levels
with theme-aware icons and auto-dismiss behavior.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import base64
import contextlib
from enum import Enum

# Third-party imports
from PySide6.QtCore import (
    QByteArray,
    QEasingCurve,
    QEvent,
    QPropertyAnimation,
    QRect,
    QSize,
    Qt,
    QTimer,
    Signal,
)
from PySide6.QtGui import QIcon, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QToolButton,
    QWidget,
)

# Local imports
from ..shared import SVG_ERROR, SVG_INFO, SVG_SUCCESS, SVG_WARNING
from .theme_icon import ThemeIcon

# ///////////////////////////////////////////////////////////////
# CONSTANTS
# ///////////////////////////////////////////////////////////////

_BANNER_HEIGHT: int = 48

_LEVEL_COLORS: dict[str, str] = {
    "INFO": "#3b82f6",
    "WARNING": "#f59e0b",
    "ERROR": "#ef4444",
    "SUCCESS": "#22c55e",
}

_LEVEL_SVG: dict[str, bytes] = {
    "INFO": SVG_INFO,
    "WARNING": SVG_WARNING,
    "ERROR": SVG_ERROR,
    "SUCCESS": SVG_SUCCESS,
}

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class NotificationLevel(Enum):
    """Severity level for a notification banner.

    Attributes:
        INFO: Informational message (blue).
        WARNING: Warning message (amber).
        ERROR: Error message (red).
        SUCCESS: Success message (green).
    """

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class NotificationBanner(QWidget):
    """Animated slide-down notification banner overlaying a parent widget.

    The banner slides in from the top of its parent widget and can
    auto-dismiss after a configurable duration. A close button is always
    visible for manual dismissal. The banner repositions itself when the
    parent is resized via event filtering.

    Features:
        - Slide-down animation via QPropertyAnimation on geometry
        - Four severity levels: INFO, WARNING, ERROR, SUCCESS
        - Auto-dismiss via QTimer when duration > 0
        - Manual close button (×)
        - Level icon via inline SVG rendered to ThemeIcon
        - Parent resize tracking via event filter

    Args:
        parent: The parent widget inside which the banner is displayed.
            Must be a valid QWidget (not None).

    Signals:
        dismissed(): Emitted when the banner is hidden (any cause).

    Example:
        >>> from ezqt_widgets import NotificationBanner, NotificationLevel
        >>> banner = NotificationBanner(parent=main_widget)
        >>> banner.dismissed.connect(lambda: print("Banner closed"))
        >>> banner.showNotification("File saved!", NotificationLevel.SUCCESS)
    """

    dismissed = Signal()

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(self, parent: QWidget) -> None:
        """Initialize the notification banner.

        Args:
            parent: The parent widget that hosts the banner overlay.
        """
        super().__init__(parent)
        self.setProperty("type", "NotificationBanner")

        # Initialize private state
        self._duration: int = 3000
        self._dismiss_timer: QTimer | None = None
        self._animation: QPropertyAnimation | None = None

        # Build UI before hiding
        self._setup_widget()

        # Start hidden
        self.setGeometry(0, 0, parent.width(), 0)
        self.hide()

        # Install event filter on parent to track resizes
        parent.installEventFilter(self)

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _setup_widget(self) -> None:
        """Setup the widget layout and child components."""
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setFixedHeight(0)  # Hidden initially

        # Icon label
        self._icon_label = QLabel()
        self._icon_label.setFixedSize(QSize(20, 20))
        self._icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Message label
        self._message_label = QLabel()
        self._message_label.setStyleSheet(
            "color: white; font-weight: 500; background: transparent;"
        )
        self._message_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self._message_label.setWordWrap(False)

        # Close button
        self._close_btn = QToolButton()
        self._close_btn.setText("×")
        self._close_btn.setFixedSize(QSize(24, 24))
        self._close_btn.setStyleSheet(
            "QToolButton { color: white; border: none; font-size: 16px; "
            "background: transparent; } "
            "QToolButton:hover { background: rgba(255,255,255,0.2); border-radius: 4px; }"
        )
        self._close_btn.clicked.connect(self._dismiss)

        # Layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 8, 8)
        layout.setSpacing(8)
        layout.addWidget(self._icon_label)
        layout.addWidget(self._message_label)
        layout.addStretch()
        layout.addWidget(self._close_btn)

        # Animation target property: geometry
        self._animation = QPropertyAnimation(self, b"geometry")
        self._animation.setDuration(250)
        self._animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    @staticmethod
    def _build_icon(level: NotificationLevel) -> ThemeIcon | None:
        """Build a ThemeIcon from the inline SVG for the given level.

        Args:
            level: The notification level.

        Returns:
            A ThemeIcon with white coloring, or None on failure.
        """
        svg_bytes = _LEVEL_SVG.get(level.value, SVG_INFO)
        encoded = base64.b64encode(svg_bytes)
        decoded = base64.b64decode(encoded)
        renderer = QSvgRenderer(QByteArray(decoded))
        if not renderer.isValid():
            return None

        pixmap = QPixmap(QSize(16, 16))
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        icon = QIcon(pixmap)
        return ThemeIcon.from_source(icon)

    def _apply_level_style(self, level: NotificationLevel) -> None:
        """Apply background color and icon for the given level.

        Args:
            level: The notification level to apply.
        """
        color = _LEVEL_COLORS.get(level.value, "#3b82f6")
        self.setStyleSheet(
            f"NotificationBanner {{ background-color: {color}; border-radius: 0px; }}"
        )

        icon = self._build_icon(level)
        if icon is not None:
            self._icon_label.setPixmap(icon.pixmap(QSize(16, 16)))
        else:
            self._icon_label.clear()

    def _slide_in(self) -> None:
        """Animate the banner sliding down to full height."""
        if self._animation is None:
            return
        parent = self.parentWidget()
        if parent is None:
            return

        start_rect = QRect(0, 0, parent.width(), 0)
        end_rect = QRect(0, 0, parent.width(), _BANNER_HEIGHT)

        self.setGeometry(start_rect)
        self.show()
        self.raise_()

        self._animation.setStartValue(start_rect)
        self._animation.setEndValue(end_rect)
        self._animation.start()

    def _slide_out(self) -> None:
        """Animate the banner sliding up and then emit dismissed."""
        animation = self._animation
        if animation is None:
            self._finish_dismiss()
            return
        parent = self.parentWidget()
        if parent is None:
            self._finish_dismiss()
            return

        current = self.geometry()
        end_rect = QRect(0, 0, parent.width(), 0)

        animation.setStartValue(current)
        animation.setEndValue(end_rect)
        animation.finished.connect(self._finish_dismiss)
        animation.start()

    def _finish_dismiss(self) -> None:
        """Hide the widget and emit the dismissed signal."""
        # Disconnect to avoid cumulative connections on next show
        animation = self._animation
        if animation is None:
            self.hide()
            self.dismissed.emit()
            return
        with contextlib.suppress(RuntimeError):
            animation.finished.disconnect(self._finish_dismiss)
        self.hide()
        self.dismissed.emit()

    def _stop_timer(self) -> None:
        """Stop the auto-dismiss timer if active."""
        if self._dismiss_timer is not None:
            self._dismiss_timer.stop()
            self._dismiss_timer.deleteLater()
            self._dismiss_timer = None

    def _dismiss(self) -> None:
        """Dismiss the banner with slide-out animation."""
        self._stop_timer()
        self._slide_out()

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def showNotification(
        self,
        message: str,
        level: NotificationLevel = NotificationLevel.INFO,
        duration: int = 3000,
    ) -> None:
        """Display a notification banner with the given message and level.

        Args:
            message: The text to display in the banner.
            level: The severity level (default: NotificationLevel.INFO).
            duration: Display duration in milliseconds. Use 0 for a
                permanent banner that requires manual dismissal
                (default: 3000).
        """
        self._stop_timer()
        self._duration = duration

        self._message_label.setText(message)
        self._apply_level_style(level)
        self._slide_in()

        if duration > 0:
            self._dismiss_timer = QTimer(self)
            self._dismiss_timer.setSingleShot(True)
            self._dismiss_timer.timeout.connect(self._dismiss)
            self._dismiss_timer.start(duration)

    # ///////////////////////////////////////////////////////////////
    # EVENT HANDLERS
    # ///////////////////////////////////////////////////////////////

    def eventFilter(self, obj: object, event: QEvent) -> bool:
        """Track parent resize events to reposition the banner.

        Args:
            obj: The object that generated the event.
            event: The event.

        Returns:
            False to allow normal event propagation.
        """
        if obj is self.parentWidget() and event.type() == QEvent.Type.Resize:
            parent = self.parentWidget()
            if parent is not None and self.isVisible():
                self.setGeometry(0, 0, parent.width(), _BANNER_HEIGHT)
        return False

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

__all__ = ["NotificationBanner", "NotificationLevel"]
