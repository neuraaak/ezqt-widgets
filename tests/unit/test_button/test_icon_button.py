# ///////////////////////////////////////////////////////////////
# TEST_ICON_BUTTON - IconButton Widget Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Unit tests for IconButton widget.

Tests for the enhanced button widget with flexible icon and text support.
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
from ezqt_widgets.widgets.button.icon_button import IconButton

pytestmark = pytest.mark.unit

# ///////////////////////////////////////////////////////////////
# TEST CLASSES
# ///////////////////////////////////////////////////////////////


class TestColorizePixmap:
    """Tests for colorize_pixmap function."""

    def test_should_colorize_pixel_data_when_colorize_pixmap_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Basic test for colorize_pixmap."""
        # Create a test pixmap
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.white)

        # Test colorization
        result = IconButton._colorize_pixmap(pixmap, "#FF0000", 0.8)

        # Verifications
        assert result is not None
        assert result.size() == pixmap.size()
        assert result.width() == 16
        assert result.height() == 16

    def test_should_preserve_transparency_when_colorize_pixmap_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test with transparent opacity."""
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.white)

        result = IconButton._colorize_pixmap(pixmap, "#00FF00", 0.0)

        assert result is not None
        assert result.size() == pixmap.size()


class TestLoadIconFromSource:
    """Tests for load_icon_from_source function."""

    def test_should_return_none_when_source_is_none(self, qt_widget_cleanup) -> None:
        """Test with None source."""
        result = IconButton._load_icon_from_source(None)
        assert result is None

    def test_should_return_icon_when_source_is_qicon(self, qt_widget_cleanup) -> None:
        """Test with existing QIcon."""
        # Create a test QIcon
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.red)
        icon = QIcon(pixmap)

        result = IconButton._load_icon_from_source(icon)

        assert result is not None
        assert isinstance(result, QIcon)

    def test_should_load_icon_from_file_when_source_is_file_path(
        self, mock_icon_path
    ) -> None:
        """Test with file path."""
        result = IconButton._load_icon_from_source(mock_icon_path)

        assert result is not None
        assert isinstance(result, QIcon)

    def test_should_load_icon_from_svg_when_source_is_svg_path(
        self, mock_svg_path
    ) -> None:
        """Test with SVG file."""
        result = IconButton._load_icon_from_source(mock_svg_path)

        assert result is not None
        assert isinstance(result, QIcon)

    @patch("ezqt_widgets.widgets.button.icon_button.fetch_url_bytes")
    def test_should_load_icon_from_url_when_source_is_url(
        self, mock_fetch, qt_widget_cleanup
    ) -> None:
        """Test with URL."""
        # Create a valid PNG using QPixmap
        from PySide6.QtCore import QBuffer, QIODevice
        from PySide6.QtGui import QColor

        # Create a 16x16 red pixmap
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(255, 0, 0))  # Red

        # Convert to PNG bytes
        buffer = QBuffer()
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        pixmap.save(buffer, "PNG")
        png_content = buffer.data()
        buffer.close()

        mock_fetch.return_value = bytes(png_content)

        result = IconButton._load_icon_from_source("https://example.com/icon.png")

        assert result is not None
        assert isinstance(result, QIcon)
        mock_fetch.assert_called_once_with("https://example.com/icon.png")

    @patch("ezqt_widgets.widgets.button.icon_button.fetch_url_bytes")
    def test_should_return_none_when_url_fetch_fails(self, mock_fetch) -> None:
        """Test with invalid URL."""
        mock_fetch.return_value = None

        result = IconButton._load_icon_from_source("https://invalid-url.com/icon.png")

        assert result is None


class TestIconButton:
    """Tests for IconButton class."""

    def test_should_have_default_properties_when_created(
        self, qt_widget_cleanup
    ) -> None:
        """Test creation with default parameters."""
        button = IconButton()

        assert button is not None
        assert isinstance(button, IconButton)
        assert button.text == ""
        assert button.icon_size == QSize(20, 20)
        assert button.text_visible is True
        assert button.spacing == 10

    def test_should_use_custom_properties_when_created_with_parameters(
        self, qt_widget_cleanup, mock_icon_path
    ) -> None:
        """Test creation with custom parameters."""
        icon = QIcon(mock_icon_path)
        button = IconButton(
            icon=icon,
            text="Test Button",
            icon_size=QSize(32, 32),
            text_visible=False,
            spacing=15,
        )

        assert button.icon is not None
        assert button.text == "Test Button"
        assert button.icon_size == QSize(32, 32)
        assert button.text_visible is False
        assert button.spacing == 15

    def test_should_update_properties_when_setters_are_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test button properties."""
        button = IconButton()

        # Test icon property
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.blue)
        icon = QIcon(pixmap)

        button.icon = icon
        assert button.icon is not None

        # Test text property
        button.text = "New Text"
        assert button.text == "New Text"

        # Test icon_size property
        button.icon_size = QSize(24, 24)
        assert button.icon_size == QSize(24, 24)

        # Test text_visible property
        button.text_visible = False
        assert button.text_visible is False

        # Test spacing property
        button.spacing = 20
        assert button.spacing == 20

    def test_should_emit_clicked_signal_when_button_is_clicked(
        self, qt_widget_cleanup
    ) -> None:
        """Test button signals."""
        button = IconButton()

        # Test iconChanged signal
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.green)
        icon = QIcon(pixmap)

        signal_received = False

        def on_icon_changed(new_icon: QIcon) -> None:
            nonlocal signal_received
            signal_received = True
            assert new_icon is not None

        button.iconChanged.connect(on_icon_changed)
        button.icon = icon

        # Verify that the signal was emitted
        assert signal_received

        # Test textChanged signal
        text_signal_received = False

        def on_text_changed(new_text: str) -> None:
            nonlocal text_signal_received
            text_signal_received = True
            assert new_text == "Signal Test"

        button.textChanged.connect(on_text_changed)
        button.text = "Signal Test"

        # Verify that the signal was emitted
        assert text_signal_received

    def test_should_not_raise_when_methods_are_called(self, qt_widget_cleanup) -> None:
        """Test button methods."""
        button = IconButton(text="Test", icon=QIcon())

        # Test clearIcon
        button.clearIcon()
        assert button.icon is None

        # Test clearText
        button.clearText()
        assert button.text == ""

        # Test toggleTextVisibility
        initial_visibility = button.text_visible
        button.toggleTextVisibility()
        assert button.text_visible != initial_visibility

        button.toggleTextVisibility()
        assert button.text_visible == initial_visibility

    def test_should_return_valid_size_hints_when_queried(
        self, qt_widget_cleanup
    ) -> None:
        """Test size hint methods."""
        button = IconButton(text="Test Button", icon=QIcon())

        # Test sizeHint
        size_hint = button.sizeHint()
        assert size_hint is not None
        assert isinstance(size_hint, QSize)
        assert size_hint.width() > 0
        assert size_hint.height() > 0

        # Test minimumSizeHint
        min_size_hint = button.minimumSizeHint()
        assert min_size_hint is not None
        assert isinstance(min_size_hint, QSize)
        assert min_size_hint.width() > 0
        assert min_size_hint.height() > 0

    def test_should_update_icon_color_when_set_icon_color_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test set_icon_color method."""
        # Create a button with icon
        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.GlobalColor.white)
        icon = QIcon(pixmap)
        button = IconButton(icon=icon)

        # Test colorization
        button.setIconColor("#FF0000", 0.7)

        # Verify that the icon was modified
        assert button.icon is not None

    def test_should_not_raise_when_refresh_style_is_called(
        self, qt_widget_cleanup
    ) -> None:
        """Test refreshStyle method."""
        button = IconButton()

        # Method should not raise an exception
        try:
            button.refreshStyle()
        except Exception as e:
            pytest.fail(f"refreshStyle() raised an exception: {e}")

    def test_should_have_minimum_dimensions_when_instantiated(
        self, qt_widget_cleanup
    ) -> None:
        """Test minimum dimensions."""
        button = IconButton(min_width=100, min_height=50)

        assert button.min_width == 100
        assert button.min_height == 50

        # Modify dimensions
        button.min_width = 150
        button.min_height = 75

        assert button.min_width == 150
        assert button.min_height == 75

        # Test with None
        button.min_width = None
        button.min_height = None

        assert button.min_width is None
        assert button.min_height is None

    # ------------------------------------------------
    # New feature tests
    # ------------------------------------------------

    def test_should_emit_icon_load_failed_when_url_fetch_returns_none(
        self, qt_widget_cleanup
    ) -> None:
        """Test that iconLoadFailed is emitted when a URL fetch returns no data."""
        button = IconButton()

        failed_urls: list[str] = []
        button.iconLoadFailed.connect(failed_urls.append)

        url = "https://example.com/missing.png"
        # Simulate fetcher callback with data=None
        button._pending_icon_url = url
        button._on_icon_url_fetched(url, None)

        assert url in failed_urls

    def test_should_not_emit_icon_load_failed_when_url_does_not_match(
        self, qt_widget_cleanup
    ) -> None:
        """Test that iconLoadFailed is not emitted for stale/mismatched URLs."""
        button = IconButton()

        failed_urls: list[str] = []
        button.iconLoadFailed.connect(failed_urls.append)

        button._pending_icon_url = "https://example.com/current.png"
        # Deliver result for a different URL
        button._on_icon_url_fetched("https://example.com/old.png", None)

        assert len(failed_urls) == 0
