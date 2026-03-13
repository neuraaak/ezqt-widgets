# ///////////////////////////////////////////////////////////////
# TEST_THEME_ICON - ThemeIcon Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for ThemeIcon widget.

Tests for the theme-aware icon that automatically adapts its color
based on the active application theme (dark/light).
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import warnings

# Third-party imports
import pytest
from PySide6.QtGui import QColor, QIcon, QPixmap

# Local imports
from ezqt_widgets.widgets.misc.theme_icon import ThemeIcon

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestThemeIcon:
    """Test cases for ThemeIcon widget."""

    # ------------------------------------------------
    # CONSTRUCTION
    # ------------------------------------------------

    def test_should_have_default_properties_when_created_without_parameters(
        self, qt_application
    ) -> None:
        """Test ThemeIcon creation with default parameters."""
        icon = ThemeIcon(QIcon())

        assert icon.theme == "dark"
        assert (
            not icon.original_icon.isNull() or icon.original_icon.isNull()
        )  # QIcon() is null

    def test_should_accept_path_string_when_created_with_path(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test ThemeIcon creation from a file path string."""
        icon = ThemeIcon(mock_icon_path)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_should_accept_qicon_when_created_with_qicon(self, qt_application) -> None:
        """Test ThemeIcon creation from a QIcon instance."""
        source_icon = QIcon()
        icon = ThemeIcon(source_icon)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_should_accept_qpixmap_when_created_with_qpixmap(
        self, qt_application
    ) -> None:
        """Test ThemeIcon creation from a QPixmap instance."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("red"))
        icon = ThemeIcon(pixmap)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_should_use_custom_theme_when_created_with_theme_parameter(
        self, qt_application
    ) -> None:
        """Test ThemeIcon creation with a custom initial theme."""
        icon = ThemeIcon(QIcon(), theme="light")

        assert icon.theme == "light"

    def test_should_accept_dark_color_when_created_with_dark_color_parameter(
        self, qt_application
    ) -> None:
        """Test ThemeIcon creation with a custom dark color."""
        icon = ThemeIcon(QIcon(), dark_color="#ff0000")

        assert icon.theme == "dark"

    def test_should_store_both_colors_when_created_with_light_and_dark_colors(
        self, qt_application
    ) -> None:
        """Test ThemeIcon creation with both dark and light colors specified."""
        icon = ThemeIcon(QIcon(), dark_color="#ffffff", light_color="#000000")

        assert icon.theme == "dark"

    def test_should_raise_type_error_when_source_is_none(self, qt_application) -> None:
        """Test ThemeIcon raises TypeError when constructed with None source."""
        with pytest.raises(TypeError):
            ThemeIcon(None)  # type: ignore[arg-type]

    # ------------------------------------------------
    # from_source FACTORY
    # ------------------------------------------------

    def test_should_return_none_when_from_source_receives_none(
        self, qt_application
    ) -> None:
        """Test from_source returns None when source is None."""
        result = ThemeIcon.from_source(None)

        assert result is None

    def test_should_return_same_instance_when_source_is_already_theme_icon(
        self, qt_application
    ) -> None:
        """Test from_source returns the same instance when source is already a ThemeIcon."""
        original = ThemeIcon(QIcon(), theme="light")
        result = ThemeIcon.from_source(original)

        assert result is original

    def test_should_create_instance_from_qicon_when_from_source_is_called(
        self, qt_application
    ) -> None:
        """Test from_source creates a ThemeIcon from a QIcon."""
        source = QIcon()
        result = ThemeIcon.from_source(source)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_should_create_instance_from_qpixmap_when_from_source_is_called(
        self, qt_application
    ) -> None:
        """Test from_source creates a ThemeIcon from a QPixmap."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("blue"))
        result = ThemeIcon.from_source(pixmap)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_should_create_instance_from_path_when_from_source_is_called(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test from_source creates a ThemeIcon from a file path string."""
        result = ThemeIcon.from_source(mock_icon_path)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_should_respect_theme_argument_when_from_source_is_called(
        self, qt_application
    ) -> None:
        """Test from_source passes the theme argument through to the new instance."""
        result = ThemeIcon.from_source(QIcon(), theme="light")

        assert result is not None
        assert result.theme == "light"

    # ------------------------------------------------
    # set_theme / theme property
    # ------------------------------------------------

    def test_should_set_dark_theme_when_set_theme_is_called_with_dark(
        self, qt_application
    ) -> None:
        """Test set_theme switches to dark theme."""
        icon = ThemeIcon(QIcon(), theme="light")
        icon.set_theme("dark")

        assert icon.theme == "dark"

    def test_should_set_light_theme_when_set_theme_is_called_with_light(
        self, qt_application
    ) -> None:
        """Test set_theme switches to light theme."""
        icon = ThemeIcon(QIcon(), theme="dark")
        icon.set_theme("light")

        assert icon.theme == "light"

    def test_should_emit_warning_when_set_theme_is_called_with_invalid_value(
        self, qt_application
    ) -> None:
        """Test set_theme with invalid value emits a UserWarning and does not update theme."""
        icon = ThemeIcon(QIcon(), theme="dark")

        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            icon.set_theme("invalid_theme")

        assert len(captured) == 1
        assert issubclass(captured[0].category, UserWarning)
        assert "invalid theme" in str(captured[0].message).lower()
        assert icon.theme == "dark"  # Theme must remain unchanged

    def test_should_keep_previous_theme_when_theme_setter_receives_invalid_value(
        self, qt_application
    ) -> None:
        """Test theme property setter with invalid value keeps previous theme unchanged."""
        icon = ThemeIcon(QIcon(), theme="light")

        with warnings.catch_warnings(record=True):
            warnings.simplefilter("always")
            icon.theme = "bogus"

        assert icon.theme == "light"

    # ------------------------------------------------
    # original_icon property
    # ------------------------------------------------

    def test_should_accept_qicon_when_original_icon_setter_is_called(
        self, qt_application
    ) -> None:
        """Test original_icon setter accepts a QIcon and updates internal state."""
        icon = ThemeIcon(QIcon())
        new_source = QIcon()
        icon.original_icon = new_source

        assert isinstance(icon.original_icon, QIcon)

    def test_should_accept_qpixmap_when_original_icon_setter_is_called(
        self, qt_application
    ) -> None:
        """Test original_icon setter accepts a QPixmap."""
        icon = ThemeIcon(QIcon())
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("green"))
        icon.original_icon = pixmap

        assert isinstance(icon.original_icon, QIcon)

    def test_should_raise_when_original_icon_setter_receives_none(
        self, qt_application
    ) -> None:
        """Test original_icon setter raises TypeError when given None."""
        icon = ThemeIcon(QIcon())

        with pytest.raises(TypeError):
            icon.original_icon = None  # type: ignore[assignment]

    # ------------------------------------------------
    # _normalize_color
    # ------------------------------------------------

    def test_should_return_none_when_normalize_color_receives_none(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None when input is None."""
        result = ThemeIcon._normalize_color(None)

        assert result is None

    def test_should_return_valid_qcolor_when_normalize_color_receives_valid_qcolor(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns the QColor when input is a valid QColor."""
        color = QColor("#abcdef")
        result = ThemeIcon._normalize_color(color)

        assert result is not None
        assert result == color

    def test_should_return_none_when_normalize_color_receives_invalid_qcolor(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None when input is an invalid QColor."""
        invalid_color = QColor()  # Default QColor is invalid
        result = ThemeIcon._normalize_color(invalid_color)

        assert result is None

    def test_should_parse_hex_string_when_normalize_color_receives_hex_string(
        self, qt_application
    ) -> None:
        """Test _normalize_color parses a valid hex color string."""
        result = ThemeIcon._normalize_color("#ff5500")

        assert result is not None
        assert result.isValid()

    def test_should_return_none_when_normalize_color_receives_invalid_string(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None and emits warning for invalid color string."""
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            result = ThemeIcon._normalize_color("not_a_color")

        assert result is None
        assert len(captured) == 1
        assert issubclass(captured[0].category, UserWarning)

    def test_should_parse_named_color_when_normalize_color_receives_color_name(
        self, qt_application
    ) -> None:
        """Test _normalize_color parses a valid named color string."""
        result = ThemeIcon._normalize_color("red")

        assert result is not None
        assert result.isValid()

    # ------------------------------------------------
    # _update_icon (null icon guard)
    # ------------------------------------------------

    def test_should_not_raise_when_update_icon_is_called_with_null_icon(
        self, qt_application
    ) -> None:
        """Test _update_icon does not raise when original icon is null (QIcon())."""
        # QIcon() is null — _update_icon must guard against this silently
        icon = ThemeIcon(QIcon())

        # Calling set_theme triggers _update_icon; must not raise
        icon.set_theme("light")
        icon.set_theme("dark")

    def test_should_not_raise_when_update_icon_is_called_with_pixmap_icon(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test _update_icon does not raise when icon has a real pixmap."""
        icon = ThemeIcon(mock_icon_path)

        icon.set_theme("light")
        icon.set_theme("dark")

    # ------------------------------------------------
    # _resolve_theme_colors edge cases
    # ------------------------------------------------

    def test_should_default_to_white_and_black_when_no_colors_are_set(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors defaults to white/black when no colors given."""
        icon = ThemeIcon(QIcon())

        # Dark color should be white, light color should be black (project defaults)
        assert icon._dark_color == QColor("white")

    def test_should_auto_invert_to_light_when_only_dark_color_is_set(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors auto-inverts light color when only dark is given."""
        icon = ThemeIcon(QIcon(), dark_color="#ffffff")

        # Light color must be the inversion of white = black
        assert icon._light_color == QColor(0, 0, 0, 255)

    def test_should_auto_invert_to_dark_when_only_light_color_is_set(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors auto-inverts dark color when only light is given."""
        icon = ThemeIcon(QIcon(), light_color="#000000")

        # Dark color must be the inversion of black = white
        assert icon._dark_color == QColor(255, 255, 255, 255)
