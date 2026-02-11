# ///////////////////////////////////////////////////////////////
# TEST_TYPES - Type Aliases Tests
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Tests for the types module.

This test file verifies that all type aliases are properly defined
and can be imported correctly.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QIcon, QPixmap
from PySide6.QtWidgets import QWidget

# Local imports
from ezqt_widgets.types import (
    AnimationDuration,
    ColorType,
    EventCallback,
    IconSource,
    IconSourceExtended,
    SizeType,
    ValueCallback,
    WidgetParent,
)

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestTypeAliases:
    """Test suite for type aliases."""

    def test_icon_source_import(self) -> None:
        """Test that IconSource type alias can be imported."""
        assert IconSource is not None

    def test_icon_source_extended_import(self) -> None:
        """Test that IconSourceExtended type alias can be imported."""
        assert IconSourceExtended is not None

    def test_size_type_import(self) -> None:
        """Test that SizeType type alias can be imported."""
        assert SizeType is not None

    def test_color_type_import(self) -> None:
        """Test that ColorType type alias can be imported."""
        assert ColorType is not None

    def test_widget_parent_import(self) -> None:
        """Test that WidgetParent type alias can be imported."""
        assert WidgetParent is not None

    def test_animation_duration_import(self) -> None:
        """Test that AnimationDuration type alias can be imported."""
        assert AnimationDuration is not None

    def test_event_callback_import(self) -> None:
        """Test that EventCallback type alias can be imported."""
        assert EventCallback is not None

    def test_value_callback_import(self) -> None:
        """Test that ValueCallback type alias can be imported."""
        assert ValueCallback is not None

    def test_icon_source_accepts_qicon(self) -> None:
        """Test that IconSource accepts QIcon type."""
        icon: IconSource = QIcon()
        assert isinstance(icon, QIcon)

    def test_icon_source_accepts_string(self) -> None:
        """Test that IconSource accepts string type."""
        icon: IconSource = "path/to/icon.png"
        assert isinstance(icon, str)

    def test_icon_source_accepts_none(self) -> None:
        """Test that IconSource accepts None type."""
        icon: IconSource = None
        assert icon is None

    def test_icon_source_extended_accepts_qicon(self) -> None:
        """Test that IconSourceExtended accepts QIcon type."""
        icon: IconSourceExtended = QIcon()
        assert isinstance(icon, QIcon)

    def test_icon_source_extended_accepts_qpixmap(self, qt_application) -> None:
        """Test that IconSourceExtended accepts QPixmap type."""
        icon: IconSourceExtended = QPixmap(16, 16)
        assert isinstance(icon, QPixmap)

    def test_icon_source_extended_accepts_string(self) -> None:
        """Test that IconSourceExtended accepts string type."""
        icon: IconSourceExtended = "path/to/icon.png"
        assert isinstance(icon, str)

    def test_icon_source_extended_accepts_none(self) -> None:
        """Test that IconSourceExtended accepts None type."""
        icon: IconSourceExtended = None
        assert icon is None

    def test_size_type_accepts_qsize(self) -> None:
        """Test that SizeType accepts QSize type."""
        size: SizeType = QSize(24, 24)
        assert isinstance(size, QSize)

    def test_size_type_accepts_tuple(self) -> None:
        """Test that SizeType accepts tuple type."""
        size: SizeType = (24, 24)
        assert isinstance(size, tuple)
        assert len(size) == 2

    def test_color_type_accepts_qcolor(self) -> None:
        """Test that ColorType accepts QColor type."""
        color: ColorType = QColor(255, 0, 0)
        assert isinstance(color, QColor)

    def test_color_type_accepts_string(self) -> None:
        """Test that ColorType accepts string type."""
        color: ColorType = "#FF0000"
        assert isinstance(color, str)

    def test_widget_parent_accepts_qwidget(self, qt_application) -> None:
        """Test that WidgetParent accepts QWidget type."""
        widget = QWidget()
        parent: WidgetParent = widget
        assert isinstance(parent, QWidget)

    def test_widget_parent_accepts_none(self) -> None:
        """Test that WidgetParent accepts None type."""
        parent: WidgetParent = None
        assert parent is None

    def test_animation_duration_is_int(self) -> None:
        """Test that AnimationDuration is int type."""
        duration: AnimationDuration = 200
        assert isinstance(duration, int)

    def test_event_callback_signature(self) -> None:
        """Test that EventCallback has correct signature."""

        def callback() -> None:
            pass

        cb: EventCallback = callback
        assert callable(cb)

    def test_value_callback_signature(self) -> None:
        """Test that ValueCallback has correct signature."""

        def callback(value: int) -> None:
            pass

        cb: ValueCallback = callback
        assert callable(cb)

    def test_all_types_exported(self) -> None:
        """Test that all type aliases are exported in __all__."""
        from ezqt_widgets import types

        expected_types = [
            "IconSource",
            "IconSourceExtended",
            "SizeType",
            "ColorType",
            "WidgetParent",
            "AnimationDuration",
            "EventCallback",
            "ValueCallback",
        ]

        for type_name in expected_types:
            assert type_name in types.__all__, f"{type_name} not in __all__"
            assert hasattr(types, type_name), f"{type_name} not defined"

    def test_types_importable_from_main_module(self) -> None:
        """Test that types can be imported from main module."""
        from ezqt_widgets import (
            AnimationDuration,
            ColorType,
            EventCallback,
            IconSource,
            IconSourceExtended,
            SizeType,
            ValueCallback,
            WidgetParent,
        )

        assert IconSource is not None
        assert IconSourceExtended is not None
        assert SizeType is not None
        assert ColorType is not None
        assert WidgetParent is not None
        assert AnimationDuration is not None
        assert EventCallback is not None
        assert ValueCallback is not None
