# ///////////////////////////////////////////////////////////////
# SHARED - Shared Constants Package
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
Shared constants package.

Exports all shared widget constants (animation durations, icon sizes,
and SVG icon bytes) for use across all widget modules.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Local imports
from ._defaults import (
    ANIMATION_DURATION_FAST,
    ANIMATION_DURATION_NORMAL,
    ANIMATION_DURATION_SLOW,
    ICON_SIZE_LARGE,
    ICON_SIZE_NORMAL,
    ICON_SIZE_SMALL,
    ICON_SIZE_XLARGE,
    SVG_CALENDAR,
    SVG_CHECK,
    SVG_CHEVRON_DOWN,
    SVG_CHEVRON_RIGHT,
    SVG_CLOSE,
    SVG_CROSS,
    SVG_ERROR,
    SVG_EYE_CLOSED,
    SVG_EYE_OPEN,
    SVG_FOLDER,
    SVG_INFO,
    SVG_SEARCH,
    SVG_SPINNER,
    SVG_SUCCESS,
    SVG_WARNING,
)

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    "ANIMATION_DURATION_FAST",
    "ANIMATION_DURATION_NORMAL",
    "ANIMATION_DURATION_SLOW",
    "ICON_SIZE_LARGE",
    "ICON_SIZE_NORMAL",
    "ICON_SIZE_SMALL",
    "ICON_SIZE_XLARGE",
    "SVG_CALENDAR",
    "SVG_CHECK",
    "SVG_CHEVRON_DOWN",
    "SVG_CHEVRON_RIGHT",
    "SVG_CLOSE",
    "SVG_CROSS",
    "SVG_ERROR",
    "SVG_EYE_CLOSED",
    "SVG_EYE_OPEN",
    "SVG_FOLDER",
    "SVG_INFO",
    "SVG_SEARCH",
    "SVG_SPINNER",
    "SVG_SUCCESS",
    "SVG_WARNING",
]
