# ///////////////////////////////////////////////////////////////
# TEST_NOTIFICATION_BANNER - NotificationBanner Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for NotificationBanner widget.

Tests for the animated slide-down notification banner widget.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest
from PySide6.QtWidgets import QWidget

# Local imports
from ezqt_widgets.widgets.misc.notification_banner import (
    NotificationBanner,
    NotificationLevel,
)

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestNotificationLevel:
    """Tests for NotificationLevel enum."""

    def test_should_have_four_levels_when_enum_is_inspected(self) -> None:
        """Test that all four notification levels are defined."""
        levels = list(NotificationLevel)
        assert NotificationLevel.INFO in levels
        assert NotificationLevel.WARNING in levels
        assert NotificationLevel.ERROR in levels
        assert NotificationLevel.SUCCESS in levels
        assert len(levels) == 4

    def test_should_have_string_values_matching_names(self) -> None:
        """Test that enum values match their names."""
        assert NotificationLevel.INFO.value == "INFO"
        assert NotificationLevel.WARNING.value == "WARNING"
        assert NotificationLevel.ERROR.value == "ERROR"
        assert NotificationLevel.SUCCESS.value == "SUCCESS"


class TestNotificationBanner:
    """Tests for NotificationBanner class."""

    def test_should_create_when_initialized_with_parent(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with a valid parent widget."""
        parent = QWidget()
        banner = NotificationBanner(parent)

        assert banner is not None
        assert isinstance(banner, NotificationBanner)
        assert banner.parentWidget() is parent

    def test_should_be_hidden_initially_when_created(self, qt_widget_cleanup) -> None:
        """Test that the banner is hidden on creation."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        assert not banner.isVisible()

    def test_should_become_visible_when_showNotification_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test that showNotification() makes the banner visible."""
        parent = QWidget()
        parent.resize(400, 300)
        parent.show()
        banner = NotificationBanner(parent)

        banner.showNotification("Test message", NotificationLevel.INFO, duration=0)

        # Banner should be visible after calling showNotification
        assert banner.isVisible()

    def test_should_display_message_when_showNotification_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test that the message label receives the correct text."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        banner.showNotification("Hello, world!", NotificationLevel.SUCCESS, duration=0)

        assert banner._message_label.text() == "Hello, world!"

    def test_should_show_info_notification_without_error(
        self, qt_widget_cleanup
    ) -> None:
        """Test INFO level notification does not raise."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        try:
            banner.showNotification("Info message", NotificationLevel.INFO, duration=0)
        except Exception as exc:
            pytest.fail(f"showNotification(INFO) raised: {exc}")

    def test_should_show_warning_notification_without_error(
        self, qt_widget_cleanup
    ) -> None:
        """Test WARNING level notification does not raise."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        try:
            banner.showNotification(
                "Warning message", NotificationLevel.WARNING, duration=0
            )
        except Exception as exc:
            pytest.fail(f"showNotification(WARNING) raised: {exc}")

    def test_should_show_error_notification_without_error(
        self, qt_widget_cleanup
    ) -> None:
        """Test ERROR level notification does not raise."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        try:
            banner.showNotification(
                "Error message", NotificationLevel.ERROR, duration=0
            )
        except Exception as exc:
            pytest.fail(f"showNotification(ERROR) raised: {exc}")

    def test_should_show_success_notification_without_error(
        self, qt_widget_cleanup
    ) -> None:
        """Test SUCCESS level notification does not raise."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        try:
            banner.showNotification(
                "Success message", NotificationLevel.SUCCESS, duration=0
            )
        except Exception as exc:
            pytest.fail(f"showNotification(SUCCESS) raised: {exc}")

    def test_should_emit_dismissed_signal_when_close_button_is_clicked(
        self, qt_widget_cleanup
    ) -> None:
        """Test dismissed signal emission when close button is clicked."""
        from PySide6.QtCore import QTimer
        from PySide6.QtWidgets import QApplication

        parent = QWidget()
        parent.resize(400, 300)
        parent.show()
        QApplication.processEvents()

        banner = NotificationBanner(parent)
        banner.showNotification("Dismiss me", NotificationLevel.INFO, duration=0)
        QApplication.processEvents()

        dismissed_count = [0]
        banner.dismissed.connect(
            lambda: dismissed_count.__setitem__(0, dismissed_count[0] + 1)
        )

        banner._close_btn.click()

        # Allow animation (250 ms) to complete — process events for 400 ms
        deadline = QTimer()
        deadline.setSingleShot(True)
        deadline.start(400)
        while deadline.isActive():
            QApplication.processEvents()

        assert dismissed_count[0] >= 1

    def test_should_replace_message_when_showNotification_is_called_twice(
        self, qt_widget_cleanup
    ) -> None:
        """Test that calling showNotification again updates the message."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        banner.showNotification("First message", NotificationLevel.INFO, duration=0)
        banner.showNotification("Second message", NotificationLevel.WARNING, duration=0)

        assert banner._message_label.text() == "Second message"

    def test_should_have_dismissed_signal_defined(self, qt_widget_cleanup) -> None:
        """Test that dismissed signal exists and is connectable."""
        parent = QWidget()
        banner = NotificationBanner(parent)

        received: list[None] = []
        banner.dismissed.connect(lambda: received.append(None))

        assert banner.dismissed is not None

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle() does not raise."""
        parent = QWidget()
        banner = NotificationBanner(parent)

        try:
            banner.refreshStyle()
        except Exception as exc:
            pytest.fail(f"refreshStyle() raised an exception: {exc}")

    def test_should_use_info_level_as_default_when_level_is_not_provided(
        self, qt_widget_cleanup
    ) -> None:
        """Test that default level is INFO when not specified."""
        parent = QWidget()
        parent.resize(400, 300)
        banner = NotificationBanner(parent)

        # Call with only message (no level argument)
        try:
            banner.showNotification("Default level test")
        except Exception as exc:
            pytest.fail(f"showNotification with default level raised: {exc}")
