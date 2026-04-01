# ///////////////////////////////////////////////////////////////
# EXAMPLES THEME - Theme Loader
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""Theme helpers for example scripts."""

from __future__ import annotations

import re

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from pathlib import Path

# Third-party imports
import yaml
from PySide6.QtWidgets import QApplication, QWidget

# ///////////////////////////////////////////////////////////////
# CONSTANTS
# ///////////////////////////////////////////////////////////////

_THEME_QSS = "main.qss"
_THEME_CONFIG = "theme.yaml"


# ///////////////////////////////////////////////////////////////
# PUBLIC FUNCTIONS
# ///////////////////////////////////////////////////////////////


def apply_theme(target: QApplication | QWidget) -> None:
    """Apply the example theme to the target.

    Args:
        target: QApplication or QWidget to receive the stylesheet.
    """
    base_dir = Path(__file__).resolve().parents[1]
    qss_path = base_dir / "bin" / _THEME_QSS
    palette_path = base_dir / "bin" / _THEME_CONFIG

    if not qss_path.exists() or not palette_path.exists():
        target.setStyleSheet("")
        return

    try:
        with palette_path.open("r", encoding="utf-8") as palette_file:
            config = yaml.safe_load(palette_file) or {}
        palette = config.get("palette", {})

        with qss_path.open("r", encoding="utf-8") as qss_file:
            qss = qss_file.read()

        qss = _replace_css_vars(qss, palette)
        qss = _replace_legacy_vars(qss, palette)
        target.setStyleSheet(qss)
    except (OSError, ValueError, yaml.YAMLError):
        target.setStyleSheet("")


# ///////////////////////////////////////////////////////////////
# INTERNAL HELPERS
# ///////////////////////////////////////////////////////////////


def _replace_css_vars(qss: str, palette: dict[str, str]) -> str:
    pattern = re.compile(r"var\(--([a-zA-Z0-9_]+)\)")

    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        return str(palette.get(key, match.group(0)))

    return pattern.sub(repl, qss)


def _replace_legacy_vars(qss: str, palette: dict[str, str]) -> str:
    pattern = re.compile(r"\$_[a-zA-Z0-9_]+")

    def repl(match: re.Match[str]) -> str:
        raw = match.group(0)
        key = raw.lstrip("$_")
        return str(palette.get(key, raw))

    return pattern.sub(repl, qss)
