# ///////////////////////////////////////////////////////////////
# DEFAULTS - Shared Widget Constants
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Shared widget constants module.

Centralises all constants shared across widget modules:
    - Animation durations
    - Default icon sizes (QSize)
    - SVG icon bytes for all common icons

SVG icons follow a consistent style:
    - viewBox="0 0 24 24"
    - fill="none"
    - stroke="currentColor" (or "white" for notification icons)
    - stroke-width="2"
    - stroke-linecap="round"
    - stroke-linejoin="round"
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
from PySide6.QtCore import QSize

# ///////////////////////////////////////////////////////////////
# CONSTANTS
# ///////////////////////////////////////////////////////////////

# ------------------------------------------------
# Animation durations (milliseconds)
# ------------------------------------------------

ANIMATION_DURATION_FAST: int = 150
"""Fast transitions (hover, quick feedback)."""

ANIMATION_DURATION_NORMAL: int = 250
"""Standard transitions (most animations)."""

ANIMATION_DURATION_SLOW: int = 400
"""Slow transitions (emphasis, complex animations)."""

# ------------------------------------------------
# Default icon sizes
# ------------------------------------------------

ICON_SIZE_SMALL: QSize = QSize(14, 14)
"""Small icon size (14x14 px)."""

ICON_SIZE_NORMAL: QSize = QSize(16, 16)
"""Normal icon size (16x16 px)."""

ICON_SIZE_LARGE: QSize = QSize(20, 20)
"""Large icon size (20x20 px)."""

ICON_SIZE_XLARGE: QSize = QSize(24, 24)
"""Extra-large icon size (24x24 px)."""

# ------------------------------------------------
# SVG icon bytes
# Each icon uses consistent style attributes.
# ------------------------------------------------

SVG_FOLDER: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2'
    b' 3h9a2 2 0 0 1 2 2z"/>'
    b"</svg>"
)
"""Folder / open-folder icon (from FilePickerInput)."""

SVG_SEARCH: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <circle cx="11" cy="11" r="8"/>'
    b'  <line x1="21" y1="21" x2="16.65" y2="16.65"/>'
    b"</svg>"
)
"""Search / magnifying-glass icon."""

SVG_EYE_OPEN: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>'
    b'  <circle cx="12" cy="12" r="3"/>'
    b"</svg>"
)
"""Eye (password visible) icon."""

SVG_EYE_CLOSED: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8'
    b"   a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12"
    b"   4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07"
    b'   a3 3 0 1 1-4.24-4.24"/>'
    b'  <line x1="1" y1="1" x2="23" y2="23"/>'
    b"</svg>"
)
"""Eye-closed (password hidden) icon."""

SVG_CALENDAR: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>'
    b'  <line x1="16" y1="2" x2="16" y2="6"/>'
    b'  <line x1="8" y1="2" x2="8" y2="6"/>'
    b'  <line x1="3" y1="10" x2="21" y2="10"/>'
    b"</svg>"
)
"""Calendar icon."""

SVG_CHEVRON_RIGHT: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <polyline points="9 18 15 12 9 6"/>'
    b"</svg>"
)
"""Chevron pointing right (collapsed state)."""

SVG_CHEVRON_DOWN: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <polyline points="6 9 12 15 18 9"/>'
    b"</svg>"
)
"""Chevron pointing down (expanded state)."""

SVG_CLOSE: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <line x1="18" y1="6" x2="6" y2="18"/>'
    b'  <line x1="6" y1="6" x2="18" y2="18"/>'
    b"</svg>"
)
"""Close / × icon."""

SVG_INFO: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"'
    b'  fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"'
    b'  stroke-linejoin="round">'
    b'  <circle cx="12" cy="12" r="10"/>'
    b'  <line x1="12" y1="8" x2="12" y2="8"/>'
    b'  <line x1="12" y1="12" x2="12" y2="16"/>'
    b"</svg>"
)
"""Info notification icon (white stroke, for coloured backgrounds)."""

SVG_WARNING: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"'
    b'  fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"'
    b'  stroke-linejoin="round">'
    b'  <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0'
    b'    1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'
    b'  <line x1="12" y1="9" x2="12" y2="13"/>'
    b'  <line x1="12" y1="17" x2="12.01" y2="17"/>'
    b"</svg>"
)
"""Warning notification icon (white stroke, for coloured backgrounds)."""

SVG_ERROR: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"'
    b'  fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"'
    b'  stroke-linejoin="round">'
    b'  <circle cx="12" cy="12" r="10"/>'
    b'  <line x1="15" y1="9" x2="9" y2="15"/>'
    b'  <line x1="9" y1="9" x2="15" y2="15"/>'
    b"</svg>"
)
"""Error notification icon (white stroke, for coloured backgrounds)."""

SVG_SUCCESS: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"'
    b'  fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"'
    b'  stroke-linejoin="round">'
    b'  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>'
    b'  <polyline points="22 4 12 14.01 9 11.01"/>'
    b"</svg>"
)
"""Success notification icon (white stroke, for coloured backgrounds)."""

SVG_SPINNER: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <line x1="12" y1="2" x2="12" y2="6"/>'
    b'  <line x1="12" y1="18" x2="12" y2="22"/>'
    b'  <line x1="4.93" y1="4.93" x2="7.76" y2="7.76"/>'
    b'  <line x1="16.24" y1="16.24" x2="19.07" y2="19.07"/>'
    b'  <line x1="2" y1="12" x2="6" y2="12"/>'
    b'  <line x1="18" y1="12" x2="22" y2="12"/>'
    b'  <line x1="4.93" y1="19.07" x2="7.76" y2="16.24"/>'
    b'  <line x1="16.24" y1="7.76" x2="19.07" y2="4.93"/>'
    b"</svg>"
)
"""Spinner / loading icon."""

SVG_CHECK: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <polyline points="20 6 9 17 4 12"/>'
    b"</svg>"
)
"""Checkmark / success icon."""

SVG_CROSS: bytes = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"'
    b' stroke="currentColor" stroke-width="2" stroke-linecap="round"'
    b' stroke-linejoin="round">'
    b'  <line x1="18" y1="6" x2="6" y2="18"/>'
    b'  <line x1="6" y1="6" x2="18" y2="18"/>'
    b"</svg>"
)
"""Cross / error icon."""

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Animation durations
    "ANIMATION_DURATION_FAST",
    "ANIMATION_DURATION_NORMAL",
    "ANIMATION_DURATION_SLOW",
    # Icon sizes
    "ICON_SIZE_SMALL",
    "ICON_SIZE_NORMAL",
    "ICON_SIZE_LARGE",
    "ICON_SIZE_XLARGE",
    # SVG icons
    "SVG_FOLDER",
    "SVG_SEARCH",
    "SVG_EYE_OPEN",
    "SVG_EYE_CLOSED",
    "SVG_CALENDAR",
    "SVG_CHEVRON_RIGHT",
    "SVG_CHEVRON_DOWN",
    "SVG_CLOSE",
    "SVG_INFO",
    "SVG_WARNING",
    "SVG_ERROR",
    "SVG_SUCCESS",
    "SVG_SPINNER",
    "SVG_CHECK",
    "SVG_CROSS",
]
