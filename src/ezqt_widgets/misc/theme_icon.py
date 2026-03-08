# ///////////////////////////////////////////////////////////////
# THEME_ICON - Theme-Aware Icon Widget
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Theme-aware icon module.

Provides a QIcon subclass that automatically adapts its color to match the
current application theme (light/dark) for PySide6 applications.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import warnings

# Third-party imports
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPixmap

# Local imports
from ..types import IconSourceExtended

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class ThemeIcon(QIcon):
    """QIcon subclass with automatic theme-based color adaptation.

    This icon adapts its color based on the specified theme:
        - Dark theme: icon rendered in the resolved dark color.
        - Light theme: icon rendered in the resolved light color.

    The icon can be updated dynamically by calling :meth:`set_theme`
    when the application theme changes.

    Args:
        icon: The source icon (``QIcon``, ``QPixmap``, or path string).
        theme: The initial theme (``"dark"`` or ``"light"``, default: ``"dark"``).
        dark_color: Optional color for dark theme (hex or ``rgb(...)`` string).
        light_color: Optional color for light theme (hex or ``rgb(...)`` string).

    Raises:
        TypeError: If ``icon`` is ``None``.

    Properties:
        theme: Get or set the active theme.
        original_icon: Get or set the source icon.

    Example:
        >>> from ezqt_widgets.misc.theme_icon import ThemeIcon
        >>> # Basic usage with automatic white/black color adaptation
        >>> icon = ThemeIcon("path/to/icon.png", theme="dark")
        >>> button.setIcon(icon)
        >>> # Custom colors for each theme
        >>> icon = ThemeIcon("icon.png", dark_color="#FFFFFF", light_color="#333333")
        >>> # Factory method from any source (QIcon, QPixmap, path, or None)
        >>> themed = ThemeIcon.from_source("icon.svg", theme="light")
        >>> # Adapt to a new theme dynamically
        >>> icon.set_theme("light")
    """

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        icon: IconSourceExtended,
        theme: str = "dark",
        dark_color: QColor | str | None = None,
        light_color: QColor | str | None = None,
    ) -> None:
        """Initialize the theme icon.

        Args:
            icon: The source icon (``QIcon``, ``QPixmap``, or path string).
            theme: The initial theme (``"dark"`` or ``"light"``).
            dark_color: Optional color for dark theme (hex or ``rgb(...)`` string).
            light_color: Optional color for light theme (hex or ``rgb(...)`` string).

        Raises:
            TypeError: If ``icon`` is ``None``.
        """
        super().__init__()
        self._original_icon: QIcon = self._to_qicon(icon)
        self._theme: str = theme
        self._dark_color, self._light_color = self._resolve_theme_colors(
            dark_color, light_color
        )
        self._update_icon()

    # ///////////////////////////////////////////////////////////////
    # PROPERTIES
    # ///////////////////////////////////////////////////////////////

    @property
    def theme(self) -> str:
        """Get the current theme.

        Returns:
            The current theme (``"dark"`` or ``"light"``).
        """
        return self._theme

    @theme.setter
    def theme(self, value: str) -> None:
        """Set the current theme and update the icon color.

        Args:
            value: The new theme (``"dark"`` or ``"light"``).
        """
        if value not in ("dark", "light"):
            warnings.warn(
                f"ThemeIcon: invalid theme '{value}', expected 'dark' or 'light'.",
                stacklevel=2,
            )
            return
        self._theme = value
        self._update_icon()

    @property
    def original_icon(self) -> QIcon:
        """Get the original (uncolored) source icon.

        Returns:
            The original icon.
        """
        return self._original_icon

    @original_icon.setter
    def original_icon(self, value: IconSourceExtended) -> None:
        """Set the source icon and refresh the themed version.

        Args:
            value: The new icon source (``QIcon``, ``QPixmap``, or path string).

        Raises:
            TypeError: If ``value`` is ``None``.
        """
        self._original_icon = self._to_qicon(value)
        self._update_icon()

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    @classmethod
    def from_source(
        cls,
        source: IconSourceExtended,
        theme: str = "dark",
        dark_color: QColor | str | None = None,
        light_color: QColor | str | None = None,
    ) -> ThemeIcon | None:
        """Create a ThemeIcon from any supported source.

        Args:
            source: The icon source (ThemeIcon, QIcon, QPixmap, or path string).
            theme: The initial theme (``"dark"`` or ``"light"``).
            dark_color: Optional color for dark theme (hex or ``rgb(...)`` string).
            light_color: Optional color for light theme (hex or ``rgb(...)`` string).

        Returns:
            A ThemeIcon instance or None if ``source`` is None.
        """
        if source is None:
            return None
        if isinstance(source, cls):
            return source
        return cls(
            source,
            theme=theme,
            dark_color=dark_color,
            light_color=light_color,
        )

    def set_theme(self, theme: str) -> None:
        """Update the icon color for the given theme.

        Convenience method equivalent to setting the :attr:`theme` property.

        Args:
            theme: The new theme (``"dark"`` or ``"light"``).
        """
        self.theme = theme

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    @staticmethod
    def _normalize_color(value: QColor | str | None) -> QColor | None:
        """Normalize an input color value.

        Args:
            value: Color input (QColor, hex string, or ``rgb(...)`` string).

        Returns:
            A valid QColor, or None if input is invalid.
        """
        if value is None:
            return None
        if isinstance(value, QColor):
            return value if value.isValid() else None
        color = QColor(value)
        if not color.isValid():
            warnings.warn(
                f"ThemeIcon: invalid color '{value}', expected hex or rgb(...).",
                stacklevel=2,
            )
            return None
        return color

    @staticmethod
    def _invert_color(color: QColor) -> QColor:
        """Invert an RGB color.

        Args:
            color: The color to invert.

        Returns:
            The inverted color, preserving alpha.
        """
        return QColor(
            255 - color.red(),
            255 - color.green(),
            255 - color.blue(),
            color.alpha(),
        )

    def _resolve_theme_colors(
        self, dark_color: QColor | str | None, light_color: QColor | str | None
    ) -> tuple[QColor, QColor]:
        """Resolve theme colors with fallback and auto-inversion.

        If both are None, defaults to white/black.
        If only one is provided, the other is auto-inverted.
        """
        normalized_dark = self._normalize_color(dark_color)
        normalized_light = self._normalize_color(light_color)

        if normalized_dark is None and normalized_light is None:
            return QColor(Qt.GlobalColor.white), QColor(Qt.GlobalColor.black)

        if normalized_dark is None and normalized_light is not None:
            return self._invert_color(normalized_light), normalized_light

        if normalized_dark is not None and normalized_light is None:
            return normalized_dark, self._invert_color(normalized_dark)

        assert normalized_dark is not None and normalized_light is not None
        return normalized_dark, normalized_light

    def _to_qicon(self, source: IconSourceExtended) -> QIcon:
        """Convert an icon source to a QIcon instance.

        Args:
            source: The icon source to convert.

        Returns:
            A QIcon instance.

        Raises:
            TypeError: If ``source`` is ``None``.
        """
        if source is None:
            raise TypeError(
                "ThemeIcon requires a non-None icon source "
                "(QIcon, QPixmap, or path string)."
            )
        if isinstance(source, str):
            return QIcon(source)
        if isinstance(source, QPixmap):
            return QIcon(source)
        return source  # QIcon or ThemeIcon (subclass of QIcon)

    def _update_icon(self) -> None:
        """Recolor the icon to match the current theme.

        - Dark theme: renders the icon in the resolved dark color.
        - Light theme: renders the icon in the resolved light color.
        """
        available_sizes = self._original_icon.availableSizes()
        if not available_sizes:
            warnings.warn(
                "ThemeIcon: original icon has no available sizes.",
                stacklevel=2,
            )
            return

        # Determine target color
        new_color = self._dark_color if self._theme == "dark" else self._light_color

        # Build the recolored pixmap
        pixmap = self._original_icon.pixmap(available_sizes[0])
        image = pixmap.toImage()

        new_pixmap = QPixmap(image.size())
        new_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(new_pixmap)
        painter.drawImage(0, 0, image)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(image.rect(), new_color)
        painter.end()

        # Replace the current icon content with the recolored version
        self.swap(QIcon())
        self.addPixmap(new_pixmap)
