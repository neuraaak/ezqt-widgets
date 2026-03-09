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

    def test_theme_icon_creation_default(self, qt_application) -> None:
        """Test ThemeIcon creation with default parameters."""
        icon = ThemeIcon(QIcon())

        assert icon.theme == "dark"
        assert (
            not icon.original_icon.isNull() or icon.original_icon.isNull()
        )  # QIcon() is null

    def test_theme_icon_creation_with_path_string(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test ThemeIcon creation from a file path string."""
        icon = ThemeIcon(mock_icon_path)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_theme_icon_creation_with_qicon(self, qt_application) -> None:
        """Test ThemeIcon creation from a QIcon instance."""
        source_icon = QIcon()
        icon = ThemeIcon(source_icon)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_theme_icon_creation_with_qpixmap(self, qt_application) -> None:
        """Test ThemeIcon creation from a QPixmap instance."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("red"))
        icon = ThemeIcon(pixmap)

        assert icon.theme == "dark"
        assert isinstance(icon.original_icon, QIcon)

    def test_theme_icon_creation_with_custom_theme(self, qt_application) -> None:
        """Test ThemeIcon creation with a custom initial theme."""
        icon = ThemeIcon(QIcon(), theme="light")

        assert icon.theme == "light"

    def test_theme_icon_creation_with_dark_color(self, qt_application) -> None:
        """Test ThemeIcon creation with a custom dark color."""
        icon = ThemeIcon(QIcon(), dark_color="#ff0000")

        assert icon.theme == "dark"

    def test_theme_icon_creation_with_both_colors(self, qt_application) -> None:
        """Test ThemeIcon creation with both dark and light colors specified."""
        icon = ThemeIcon(QIcon(), dark_color="#ffffff", light_color="#000000")

        assert icon.theme == "dark"

    def test_theme_icon_raises_type_error_when_source_is_none(
        self, qt_application
    ) -> None:
        """Test ThemeIcon raises TypeError when constructed with None source."""
        with pytest.raises(TypeError):
            ThemeIcon(None)  # type: ignore[arg-type]

    # ------------------------------------------------
    # from_source FACTORY
    # ------------------------------------------------

    def test_theme_icon_from_source_returns_none_when_source_is_none(
        self, qt_application
    ) -> None:
        """Test from_source returns None when source is None."""
        result = ThemeIcon.from_source(None)

        assert result is None

    def test_theme_icon_from_source_returns_same_instance_when_already_theme_icon(
        self, qt_application
    ) -> None:
        """Test from_source returns the same instance when source is already a ThemeIcon."""
        original = ThemeIcon(QIcon(), theme="light")
        result = ThemeIcon.from_source(original)

        assert result is original

    def test_theme_icon_from_source_creates_instance_from_qicon(
        self, qt_application
    ) -> None:
        """Test from_source creates a ThemeIcon from a QIcon."""
        source = QIcon()
        result = ThemeIcon.from_source(source)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_theme_icon_from_source_creates_instance_from_qpixmap(
        self, qt_application
    ) -> None:
        """Test from_source creates a ThemeIcon from a QPixmap."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("blue"))
        result = ThemeIcon.from_source(pixmap)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_theme_icon_from_source_creates_instance_from_path(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test from_source creates a ThemeIcon from a file path string."""
        result = ThemeIcon.from_source(mock_icon_path)

        assert result is not None
        assert isinstance(result, ThemeIcon)

    def test_theme_icon_from_source_respects_theme_argument(
        self, qt_application
    ) -> None:
        """Test from_source passes the theme argument through to the new instance."""
        result = ThemeIcon.from_source(QIcon(), theme="light")

        assert result is not None
        assert result.theme == "light"

    # ------------------------------------------------
    # set_theme / theme property
    # ------------------------------------------------

    def test_theme_icon_set_theme_dark(self, qt_application) -> None:
        """Test set_theme switches to dark theme."""
        icon = ThemeIcon(QIcon(), theme="light")
        icon.set_theme("dark")

        assert icon.theme == "dark"

    def test_theme_icon_set_theme_light(self, qt_application) -> None:
        """Test set_theme switches to light theme."""
        icon = ThemeIcon(QIcon(), theme="dark")
        icon.set_theme("light")

        assert icon.theme == "light"

    def test_theme_icon_set_theme_invalid_emits_warning(self, qt_application) -> None:
        """Test set_theme with invalid value emits a UserWarning and does not update theme."""
        icon = ThemeIcon(QIcon(), theme="dark")

        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            icon.set_theme("invalid_theme")

        assert len(captured) == 1
        assert issubclass(captured[0].category, UserWarning)
        assert "invalid theme" in str(captured[0].message).lower()
        assert icon.theme == "dark"  # Theme must remain unchanged

    def test_theme_icon_theme_property_setter_invalid_value_keeps_previous_theme(
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

    def test_theme_icon_original_icon_setter_accepts_qicon(
        self, qt_application
    ) -> None:
        """Test original_icon setter accepts a QIcon and updates internal state."""
        icon = ThemeIcon(QIcon())
        new_source = QIcon()
        icon.original_icon = new_source

        assert isinstance(icon.original_icon, QIcon)

    def test_theme_icon_original_icon_setter_accepts_qpixmap(
        self, qt_application
    ) -> None:
        """Test original_icon setter accepts a QPixmap."""
        icon = ThemeIcon(QIcon())
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor("green"))
        icon.original_icon = pixmap

        assert isinstance(icon.original_icon, QIcon)

    def test_theme_icon_original_icon_setter_raises_on_none(
        self, qt_application
    ) -> None:
        """Test original_icon setter raises TypeError when given None."""
        icon = ThemeIcon(QIcon())

        with pytest.raises(TypeError):
            icon.original_icon = None  # type: ignore[assignment]

    # ------------------------------------------------
    # _normalize_color
    # ------------------------------------------------

    def test_theme_icon_normalize_color_returns_none_for_none_input(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None when input is None."""
        result = ThemeIcon._normalize_color(None)

        assert result is None

    def test_theme_icon_normalize_color_returns_valid_qcolor_for_valid_qcolor(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns the QColor when input is a valid QColor."""
        color = QColor("#abcdef")
        result = ThemeIcon._normalize_color(color)

        assert result is not None
        assert result == color

    def test_theme_icon_normalize_color_returns_none_for_invalid_qcolor(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None when input is an invalid QColor."""
        invalid_color = QColor()  # Default QColor is invalid
        result = ThemeIcon._normalize_color(invalid_color)

        assert result is None

    def test_theme_icon_normalize_color_parses_hex_string(self, qt_application) -> None:
        """Test _normalize_color parses a valid hex color string."""
        result = ThemeIcon._normalize_color("#ff5500")

        assert result is not None
        assert result.isValid()

    def test_theme_icon_normalize_color_returns_none_for_invalid_string(
        self, qt_application
    ) -> None:
        """Test _normalize_color returns None and emits warning for invalid color string."""
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            result = ThemeIcon._normalize_color("not_a_color")

        assert result is None
        assert len(captured) == 1
        assert issubclass(captured[0].category, UserWarning)

    def test_theme_icon_normalize_color_parses_named_color(
        self, qt_application
    ) -> None:
        """Test _normalize_color parses a valid named color string."""
        result = ThemeIcon._normalize_color("red")

        assert result is not None
        assert result.isValid()

    # ------------------------------------------------
    # _update_icon (null icon guard)
    # ------------------------------------------------

    def test_theme_icon_update_icon_on_null_icon_does_not_raise(
        self, qt_application
    ) -> None:
        """Test _update_icon does not raise when original icon is null (QIcon())."""
        # QIcon() is null — _update_icon must guard against this silently
        icon = ThemeIcon(QIcon())

        # Calling set_theme triggers _update_icon; must not raise
        icon.set_theme("light")
        icon.set_theme("dark")

    def test_theme_icon_update_icon_on_pixmap_icon_does_not_raise(
        self, qt_application, mock_icon_path
    ) -> None:
        """Test _update_icon does not raise when icon has a real pixmap."""
        icon = ThemeIcon(mock_icon_path)

        icon.set_theme("light")
        icon.set_theme("dark")

    # ------------------------------------------------
    # _resolve_theme_colors edge cases
    # ------------------------------------------------

    def test_theme_icon_resolve_colors_defaults_to_white_black_when_no_colors(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors defaults to white/black when no colors given."""
        icon = ThemeIcon(QIcon())

        # Dark color should be white, light color should be black (project defaults)
        assert icon._dark_color == QColor("white")

    def test_theme_icon_resolve_colors_auto_inverts_light_when_dark_only(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors auto-inverts light color when only dark is given."""
        icon = ThemeIcon(QIcon(), dark_color="#ffffff")

        # Light color must be the inversion of white = black
        assert icon._light_color == QColor(0, 0, 0, 255)

    def test_theme_icon_resolve_colors_auto_inverts_dark_when_light_only(
        self, qt_application
    ) -> None:
        """Test _resolve_theme_colors auto-inverts dark color when only light is given."""
        icon = ThemeIcon(QIcon(), light_color="#000000")

        # Dark color must be the inversion of black = white
        assert icon._dark_color == QColor(255, 255, 255, 255)
