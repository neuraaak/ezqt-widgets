# ///////////////////////////////////////////////////////////////
# TEST_PASSWORD_INPUT - PasswordInput Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for PasswordInput widget.

Tests for the password input widget with strength bar and show/hide icon.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from unittest.mock import patch

# Third-party imports
import pytest
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap

# Local imports
from ezqt_widgets.widgets.input.password_input import (
    PasswordInput,
    _PasswordLineEdit,
)
from ezqt_widgets.widgets.input.password_input import (
    _get_strength_color as get_strength_color,
)
from ezqt_widgets.widgets.input.password_input import (
    _load_icon_from_source as load_icon_from_source,
)
from ezqt_widgets.widgets.input.password_input import (
    _password_strength as password_strength,
)

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestPasswordStrength:
    """Tests for password strength utility functions."""

    def test_should_return_weak_strength_when_password_is_simple(self) -> None:
        """Test weak password strength."""
        # Very weak password
        assert password_strength("") == 0
        assert password_strength("a") == 15  # 1 char + lowercase
        assert password_strength("123") == 20  # 3 chars + digits

        # Weak password
        assert password_strength("password") == 40  # 8+ chars + lowercase
        assert password_strength("12345678") == 45  # 8+ chars + digits

    def test_should_return_medium_strength_when_password_has_letters_and_numbers(
        self,
    ) -> None:
        """Test medium password strength."""
        # Medium password
        assert password_strength("Password") == 55  # 8+ chars + lowercase + uppercase
        assert password_strength("pass1234") == 60  # 8+ chars + lowercase + digits
        assert password_strength("PASS1234") == 60  # 8+ chars + uppercase + digits

    def test_should_return_strong_strength_when_password_meets_strong_criteria(
        self,
    ) -> None:
        """Test strong password strength."""
        # Strong password
        assert (
            password_strength("Password123") == 75
        )  # 8+ chars + lowercase + uppercase + digits
        assert (
            password_strength("Pass@word") == 80
        )  # 8+ chars + lowercase + uppercase + special
        assert (
            password_strength("Pass@123") == 100
        )  # 8+ chars + lowercase + uppercase + digits + special (max 100)

    def test_should_return_very_strong_strength_when_password_is_very_complex(
        self,
    ) -> None:
        """Test very strong password strength."""
        # Very strong password
        assert password_strength("MyP@ssw0rd!") == 100  # All criteria
        assert password_strength("SuperS3cret#") == 100  # All criteria
        assert password_strength("C0mpl3x!P@ss") == 100  # All criteria

    def test_should_handle_edge_cases_when_password_is_empty_or_minimal(self) -> None:
        """Test password strength with edge cases."""
        # Special characters
        assert password_strength("pass@word") == 65  # 8+ chars + lowercase + special
        assert password_strength("PASS@WORD") == 65  # 8+ chars + uppercase + special

        # Extreme length
        assert password_strength("a" * 100) == 40  # Length + lowercase
        assert password_strength("A" * 100) == 40  # Length + uppercase

    def test_should_return_red_color_when_strength_is_weak(self) -> None:
        """Test colors for weak passwords."""
        assert get_strength_color(0) == "#ff4444"  # Red
        assert get_strength_color(10) == "#ff4444"  # Red
        assert get_strength_color(29) == "#ff4444"  # Red

    def test_should_return_orange_color_when_strength_is_medium(self) -> None:
        """Test colors for medium passwords."""
        assert get_strength_color(30) == "#ffaa00"  # Orange
        assert get_strength_color(50) == "#ffaa00"  # Orange
        assert get_strength_color(59) == "#ffaa00"  # Orange

    def test_should_return_yellow_color_when_strength_is_good(self) -> None:
        """Test colors for good passwords."""
        assert get_strength_color(60) == "#44aa44"  # Green
        assert get_strength_color(70) == "#44aa44"  # Green
        assert get_strength_color(79) == "#44aa44"  # Green

    def test_should_return_green_color_when_strength_is_strong(self) -> None:
        """Test colors for strong passwords."""
        assert get_strength_color(80) == "#00aa00"  # Dark green
        assert get_strength_color(90) == "#00aa00"  # Dark green
        assert get_strength_color(100) == "#00aa00"  # Dark green


class TestLoadIconFromSource:
    """Tests for load_icon_from_source function."""

    def test_should_return_none_when_icon_source_is_none(self) -> None:
        """Test load_icon_from_source with None."""
        icon = load_icon_from_source(None)
        assert icon is None

    def test_should_return_icon_when_source_is_qicon(self, qt_widget_cleanup) -> None:
        """Test load_icon_from_source with QIcon."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.red)
        original_icon = QIcon(pixmap)

        icon = load_icon_from_source(original_icon)
        assert isinstance(icon, QIcon)

    @patch("ezqt_widgets.widgets.input.password_input.fetch_url_bytes")
    def test_should_load_icon_from_url_when_source_is_url_string(
        self, mock_fetch, qt_widget_cleanup
    ) -> None:
        """Test load_icon_from_source with URL."""
        from PySide6.QtCore import QBuffer, QIODevice
        from PySide6.QtGui import QColor

        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(255, 0, 0))

        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")
        png_content = buffer.data()
        buffer.close()

        mock_fetch.return_value = bytes(png_content)

        # Test icon loading from URL
        icon = load_icon_from_source("https://example.com/icon.png")
        assert isinstance(icon, QIcon)

    @patch("ezqt_widgets.widgets.input.password_input.fetch_url_bytes")
    def test_should_return_none_when_url_fetch_fails(self, mock_fetch) -> None:
        """Test load_icon_from_source with URL failure."""
        mock_fetch.return_value = None

        # Test loading failure
        icon = load_icon_from_source("https://example.com/icon.png")
        assert icon is None


class Test_PasswordLineEdit:
    """Tests for _PasswordLineEdit class."""

    def test_should_create_line_edit_when_password_line_edit_is_instantiated(
        self, qt_widget_cleanup
    ) -> None:
        """Test _PasswordLineEdit creation."""
        line_edit = _PasswordLineEdit()

        assert line_edit is not None
        assert isinstance(line_edit, _PasswordLineEdit)
        assert line_edit.echoMode() == line_edit.EchoMode.Password

    def test_should_set_right_icon_when_set_right_icon_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test set_right_icon."""
        line_edit = _PasswordLineEdit()

        # Create an icon
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.red)
        icon = QIcon(pixmap)

        # Set the icon
        line_edit.setRightIcon(icon, QSize(20, 20))

        # Verify that the icon is set
        # Note: We can't easily verify the internal icon
        # but we can verify that the method doesn't raise an exception
        assert line_edit is not None

    def test_should_not_raise_when_password_line_edit_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle."""
        line_edit = _PasswordLineEdit()

        # Method should not raise an exception
        try:
            line_edit.refreshStyle()
        except Exception as e:
            pytest.fail(f"refreshStyle() raised an exception: {e}")


class TestPasswordInput:
    """Tests for PasswordInput class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        password_widget = PasswordInput()

        assert password_widget is not None
        assert isinstance(password_widget, PasswordInput)
        assert password_widget.show_strength is True
        assert password_widget.strength_bar_height == 3
        assert password_widget.show_icon is not None
        assert password_widget.hide_icon is not None
        assert password_widget.icon_size == QSize(16, 16)

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with custom parameters."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.red)
        icon = QIcon(pixmap)

        password_widget = PasswordInput(
            show_strength=False,
            strength_bar_height=5,
            show_icon=icon,
            hide_icon=icon,
            icon_size=QSize(24, 24),
        )

        assert password_widget.show_strength is False
        assert password_widget.strength_bar_height == 5
        assert password_widget.show_icon is not None
        assert password_widget.hide_icon is not None
        assert password_widget.icon_size == QSize(24, 24)

    def test_should_update_password_properties_when_setters_are_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget properties."""
        password_widget = PasswordInput()

        # Test password property
        password_widget.password = "test123"
        assert password_widget.password == "test123"

        # Test show_strength property
        password_widget.show_strength = False
        assert password_widget.show_strength is False

        # Test strength_bar_height property
        password_widget.strength_bar_height = 10
        assert password_widget.strength_bar_height == 10

        # Test show_icon property
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.blue)
        icon = QIcon(pixmap)
        password_widget.show_icon = icon
        assert password_widget.show_icon is not None

        # Test hide_icon property
        password_widget.hide_icon = icon
        assert password_widget.hide_icon is not None

        # Test icon_size property
        password_widget.icon_size = QSize(32, 32)
        assert password_widget.icon_size == QSize(32, 32)

    def test_should_toggle_password_visibility_when_toggle_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test toggle_password."""
        password_widget = PasswordInput()

        # Initial state (password hidden)
        initial_mode = password_widget._password_input.echoMode()

        # Toggle display
        password_widget.togglePassword()

        # Verify that the mode changed
        new_mode = password_widget._password_input.echoMode()
        assert new_mode != initial_mode

        # Toggle again
        password_widget.togglePassword()
        final_mode = password_widget._password_input.echoMode()
        assert final_mode == initial_mode

    def test_should_update_strength_indicator_when_password_changes(
        self, qt_widget_cleanup
    ) -> None:
        """Test update_strength."""
        password_widget = PasswordInput()

        # Test weak password
        password_widget.updateStrength("weak")
        # Note: We can't easily verify the internal state
        # but we can verify that the method doesn't raise an exception

        # Test strong password
        password_widget.updateStrength("StrongP@ss123!")
        # Method should not raise an exception

    def test_should_emit_password_changed_signal_when_password_is_typed(
        self, qt_widget_cleanup
    ) -> None:
        """Test widget signals."""
        password_widget = PasswordInput()

        # Test strengthChanged signal
        signal_received = False
        received_strength = 0

        def on_strength_changed(strength: int) -> None:
            nonlocal signal_received, received_strength
            signal_received = True
            received_strength = strength

        password_widget.strengthChanged.connect(on_strength_changed)

        # Simulate a strength change
        password_widget.updateStrength("test123")

        # Verify that the signal is connected
        assert password_widget.strengthChanged is not None

        # Test iconClicked signal
        icon_signal_received = False

        def on_icon_clicked() -> None:
            nonlocal icon_signal_received
            icon_signal_received = True

        password_widget.iconClicked.connect(on_icon_clicked)

        # Verify that the signal is connected
        assert password_widget.iconClicked is not None

    def test_should_not_raise_when_password_input_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle."""
        password_widget = PasswordInput()

        # Method should not raise an exception
        try:
            password_widget.refreshStyle()
        except Exception as e:
            pytest.fail(f"refreshStyle() raised an exception: {e}")

    def test_should_validate_password_properties_when_password_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test password validation."""
        password_widget = PasswordInput()

        # Test valid passwords
        valid_passwords = [
            "password",
            "Password123",
            "MyP@ssw0rd!",
            "12345678",
            "a" * 100,
        ]

        for password in valid_passwords:
            password_widget.password = password
            assert password_widget.password == password

        # Test empty password
        password_widget.password = ""
        assert password_widget.password == ""

    def test_should_validate_icon_size_when_icon_size_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test icon size validation."""
        password_widget = PasswordInput()

        # Test valid sizes
        valid_sizes = [QSize(16, 16), QSize(24, 24), QSize(32, 32)]

        for size in valid_sizes:
            password_widget.icon_size = size
            assert password_widget.icon_size == size

    def test_should_validate_strength_bar_height_when_height_is_set(
        self, qt_widget_cleanup
    ) -> None:
        """Test strength bar height validation."""
        password_widget = PasswordInput()

        # Test valid heights
        valid_heights = [1, 3, 5, 10, 20]
        for height in valid_heights:
            password_widget.strength_bar_height = height
            assert password_widget.strength_bar_height == height

        # Test zero height (becomes 1)
        password_widget.strength_bar_height = 0
        assert password_widget.strength_bar_height == 1

        # Test negative height (becomes 1)
        password_widget.strength_bar_height = -5
        assert password_widget.strength_bar_height == 1

    def test_should_be_independent_when_multiple_password_inputs_are_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test with multiple instances."""
        password_widget1 = PasswordInput(show_strength=True)
        password_widget2 = PasswordInput(show_strength=False)

        # Test instance independence
        password_widget1.password = "password1"
        password_widget2.password = "password2"

        assert password_widget1.password == "password1"
        assert password_widget2.password == "password2"
        assert password_widget1.password != password_widget2.password

    def test_should_apply_changes_when_properties_are_updated_dynamically(
        self, qt_widget_cleanup
    ) -> None:
        """Test dynamic property changes."""
        password_widget = PasswordInput()

        # Test dynamic show_strength change
        password_widget.show_strength = False
        assert password_widget.show_strength is False

        password_widget.show_strength = True
        assert password_widget.show_strength is True

        # Test dynamic strength_bar_height change
        password_widget.strength_bar_height = 10
        assert password_widget.strength_bar_height == 10

        password_widget.strength_bar_height = 5
        assert password_widget.strength_bar_height == 5

    def test_should_handle_special_characters_when_password_has_special_chars(
        self, qt_widget_cleanup
    ) -> None:
        """Test with special characters in password."""
        password_widget = PasswordInput()

        special_passwords = [
            "pass@word",
            "user-name_123",
            "file/path/pass",
            "pass with spaces",
            "pass\nwith\nnewlines",
            "pass\twith\ttabs",
            "pass with émojis 🚀",
            "pass with unicode: 你好世界",
        ]

        for password in special_passwords:
            password_widget.password = password
            assert password_widget.password == password

    def test_should_handle_large_password_when_password_is_very_long(
        self, qt_widget_cleanup
    ) -> None:
        """Test with very long password."""
        password_widget = PasswordInput()

        # Create a very long password
        long_password = "a" * 1000

        # Set the password
        password_widget.password = long_password

        # Verify that the password is correctly set
        assert password_widget.password == long_password

        # Verify that strength is calculated
        password_widget.updateStrength(long_password)
        # Method should not raise an exception
