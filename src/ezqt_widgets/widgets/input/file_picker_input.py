# ///////////////////////////////////////////////////////////////
# FILE_PICKER_INPUT - File Picker Input Widget
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
File picker input widget module.

Provides a composite input widget combining a QLineEdit and a folder icon
button that opens a QFileDialog for file or directory selection.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import base64
from typing import Literal

# Third-party imports
from PySide6.QtCore import QByteArray, QSize, Qt, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QSizePolicy,
    QToolButton,
    QWidget,
)

# Local imports
from ...types import WidgetParent
from ..misc.theme_icon import ThemeIcon
from ..shared._defaults import SVG_FOLDER

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class FilePickerInput(QWidget):
    """Composite input widget combining a QLineEdit and a folder icon button.

    Clicking the folder button opens a QFileDialog (file or directory mode).
    The selected path is displayed in the QLineEdit. The widget supports
    theme-aware icon rendering via ThemeIcon.

    Features:
        - File or directory selection via QFileDialog
        - Editable QLineEdit for manual path entry
        - Theme-aware folder icon via ThemeIcon
        - Signals for file selection and path text changes
        - Configurable placeholder, filter, and dialog title

    Args:
        parent: The parent widget (default: None).
        placeholder: Placeholder text for the QLineEdit
            (default: "Select a file...").
        mode: Selection mode, either "file" or "directory"
            (default: "file").
        filter: File filter string for QFileDialog, e.g. "Images (*.png *.jpg)"
            (default: "").
        dialog_title: Title for the QFileDialog window (default: "").

    Properties:
        path: Get or set the current file/directory path.
        mode: Get or set the selection mode ("file" or "directory").
        placeholder_text: Get or set the QLineEdit placeholder text.
        filter: Get or set the file dialog filter string.
        dialog_title: Get or set the file dialog window title.

    Signals:
        fileSelected(str): Emitted when a path is chosen via the dialog.
        pathChanged(str): Emitted on every text change in the QLineEdit.

    Example:
        >>> from ezqt_widgets import FilePickerInput
        >>> picker = FilePickerInput(placeholder="Choose a CSV file...",
        ...                          filter="CSV files (*.csv)")
        >>> picker.fileSelected.connect(lambda p: print(f"Selected: {p}"))
        >>> picker.show()
    """

    fileSelected = Signal(str)
    pathChanged = Signal(str)

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(
        self,
        parent: WidgetParent = None,
        *,
        placeholder: str = "Select a file...",
        mode: Literal["file", "directory"] = "file",
        filter: str = "",  # noqa: A002
        dialog_title: str = "",
    ) -> None:
        """Initialize the file picker input."""
        super().__init__(parent)
        self.setProperty("type", "FilePickerInput")

        # Initialize private state
        self._mode: Literal["file", "directory"] = mode
        self._filter: str = filter
        self._dialog_title: str = dialog_title
        self._folder_icon: ThemeIcon | None = None

        # Setup UI
        self._setup_widget(placeholder)

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _setup_widget(self, placeholder: str) -> None:
        """Setup the widget layout and child components.

        Args:
            placeholder: Initial placeholder text for the QLineEdit.
        """
        # Build folder icon from inline SVG bytes
        self._folder_icon = self._build_folder_icon()

        # QLineEdit
        self._line_edit = QLineEdit()
        self._line_edit.setPlaceholderText(placeholder)
        self._line_edit.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self._line_edit.textChanged.connect(self.pathChanged.emit)

        # Folder button
        self._btn = QToolButton()
        self._btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self._btn.setCursor(Qt.CursorShape.PointingHandCursor)
        if self._folder_icon is not None:
            self._btn.setIcon(self._folder_icon)
            self._btn.setIconSize(QSize(16, 16))
        self._btn.clicked.connect(self._open_dialog)

        # Layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        layout.addWidget(self._line_edit)
        layout.addWidget(self._btn)

    @staticmethod
    def _build_folder_icon() -> ThemeIcon | None:
        """Build a ThemeIcon from the shared folder SVG.

        Returns:
            A ThemeIcon instance, or None if rendering fails.
        """
        svg_bytes = base64.b64decode(base64.b64encode(SVG_FOLDER))
        renderer = QSvgRenderer(QByteArray(svg_bytes))
        if not renderer.isValid():
            return None

        pixmap = QPixmap(QSize(16, 16))
        pixmap.fill(Qt.GlobalColor.transparent)
        from PySide6.QtGui import QPainter

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        icon = QIcon(pixmap)
        return ThemeIcon.from_source(icon)

    def _open_dialog(self) -> None:
        """Open the QFileDialog and update the path on selection."""
        title = self._dialog_title or (
            "Select Directory" if self._mode == "directory" else "Select File"
        )
        current = self._line_edit.text()

        if self._mode == "directory":
            selected = QFileDialog.getExistingDirectory(
                self,
                title,
                current,
            )
        else:
            selected, _ = QFileDialog.getOpenFileName(
                self,
                title,
                current,
                self._filter,
            )

        if selected:
            self._line_edit.setText(selected)
            self.fileSelected.emit(selected)

    # ///////////////////////////////////////////////////////////////
    # PROPERTIES
    # ///////////////////////////////////////////////////////////////

    @property
    def path(self) -> str:
        """Get the current path displayed in the QLineEdit.

        Returns:
            The current path string.
        """
        return self._line_edit.text()

    @path.setter
    def path(self, value: str) -> None:
        """Set the path displayed in the QLineEdit.

        Args:
            value: The new path string.
        """
        self._line_edit.setText(str(value))

    @property
    def mode(self) -> Literal["file", "directory"]:
        """Get the file dialog selection mode.

        Returns:
            The current mode ("file" or "directory").
        """
        return self._mode

    @mode.setter
    def mode(self, value: Literal["file", "directory"]) -> None:
        """Set the file dialog selection mode.

        Args:
            value: The new mode ("file" or "directory").
        """
        if value in ("file", "directory"):
            self._mode = value

    @property
    def placeholder_text(self) -> str:
        """Get the QLineEdit placeholder text.

        Returns:
            The current placeholder text.
        """
        return self._line_edit.placeholderText()

    @placeholder_text.setter
    def placeholder_text(self, value: str) -> None:
        """Set the QLineEdit placeholder text.

        Args:
            value: The new placeholder text.
        """
        self._line_edit.setPlaceholderText(str(value))

    @property
    def filter(self) -> str:  # noqa: A003
        """Get the file dialog filter string.

        Returns:
            The current filter string.
        """
        return self._filter

    @filter.setter
    def filter(self, value: str) -> None:  # noqa: A003
        """Set the file dialog filter string.

        Args:
            value: The new filter string (e.g. "Images (*.png *.jpg)").
        """
        self._filter = str(value)

    @property
    def dialog_title(self) -> str:
        """Get the file dialog window title.

        Returns:
            The current dialog title.
        """
        return self._dialog_title

    @dialog_title.setter
    def dialog_title(self, value: str) -> None:
        """Set the file dialog window title.

        Args:
            value: The new dialog title.
        """
        self._dialog_title = str(value)

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def clear(self) -> None:
        """Clear the current path from the QLineEdit."""
        self._line_edit.clear()

    def setTheme(self, theme: str) -> None:
        """Update the folder icon color for the given theme.

        Can be connected directly to a theme-change signal to keep
        the icon in sync with the application's color scheme.

        Args:
            theme: The new theme (``"dark"`` or ``"light"``).
        """
        if isinstance(self._folder_icon, ThemeIcon):
            self._folder_icon.setTheme(theme)
            self._btn.setIcon(self._folder_icon)

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

__all__ = ["FilePickerInput"]
