# Shared Constants

Centralized constants for animation durations, icon sizes, and SVG icon data used across all widget modules.

---

## Overview

`ezqt_widgets.widgets.shared.defaults` defines the canonical values shared across all widgets in the library. Using these constants instead of inline literals ensures that animation timings and icon sizes are consistent throughout an application.

The module contains three groups of constants:

- **Animation durations** — millisecond values for `QPropertyAnimation` duration
- **Icon sizes** — `QSize` instances for icon rendering
- **SVG icon bytes** — inline `bytes` objects for all common icons

---

## Import

```python
from ezqt_widgets.widgets.shared.defaults import (
    ANIMATION_DURATION_FAST,
    ANIMATION_DURATION_NORMAL,
    ANIMATION_DURATION_SLOW,
    ICON_SIZE_SMALL,
    ICON_SIZE_NORMAL,
    ICON_SIZE_LARGE,
    ICON_SIZE_XLARGE,
    SVG_FOLDER,
    SVG_SEARCH,
    # ... other SVG constants
)
```

---

## Animation Durations

Integer constants in milliseconds for use as `QPropertyAnimation.setDuration()` arguments.

| Constant                    | Value | Intended use                                      |
| --------------------------- | ----- | ------------------------------------------------- |
| `ANIMATION_DURATION_FAST`   | `150` | Hover states, quick feedback                      |
| `ANIMATION_DURATION_NORMAL` | `250` | Standard transitions (most animations)            |
| `ANIMATION_DURATION_SLOW`   | `400` | Emphasis animations, complex multi-step sequences |

```python
from PySide6.QtCore import QPropertyAnimation
from ezqt_widgets.widgets.shared.defaults import ANIMATION_DURATION_NORMAL

anim = QPropertyAnimation(widget, b"geometry")
anim.setDuration(ANIMATION_DURATION_NORMAL)
```

---

## Icon Sizes

`QSize` constants for icon rendering. Pass directly to `QLabel.setFixedSize()`, `QAbstractButton.setIconSize()`, or `QSvgRenderer` pixel map dimensions.

| Constant           | Value     | Typical use                        |
| ------------------ | --------- | ---------------------------------- |
| `ICON_SIZE_SMALL`  | `14 x 14` | Compact mode, tight layouts        |
| `ICON_SIZE_NORMAL` | `16 x 16` | Standard button and input icons    |
| `ICON_SIZE_LARGE`  | `20 x 20` | Notification icons, emphasis       |
| `ICON_SIZE_XLARGE` | `24 x 24` | Toolbar icons, large touch targets |

```python
from ezqt_widgets.widgets.shared.defaults import ICON_SIZE_NORMAL

button.setIconSize(ICON_SIZE_NORMAL)
```

---

## SVG Icon Bytes

Raw SVG data as `bytes` objects. All icons share a consistent style:

- `viewBox="0 0 24 24"`
- `fill="none"`
- `stroke="currentColor"` (or `"white"` for notification-level icons)
- `stroke-width="2"` (or `2.5` for notification icons)
- `stroke-linecap="round"`, `stroke-linejoin="round"`

### General-purpose icons (`stroke="currentColor"`)

| Constant            | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| `SVG_FOLDER`        | Open folder — used by `FilePickerInput`                     |
| `SVG_SEARCH`        | Magnifying glass — used by `SearchInput`                    |
| `SVG_EYE_OPEN`      | Eye (password visible) — used by `PasswordInput`            |
| `SVG_EYE_CLOSED`    | Eye with slash (password hidden) — used by `PasswordInput`  |
| `SVG_CALENDAR`      | Calendar grid — used by `DateButton`                        |
| `SVG_CHEVRON_RIGHT` | Right-pointing chevron — collapsed state indicator          |
| `SVG_CHEVRON_DOWN`  | Down-pointing chevron — expanded state indicator            |
| `SVG_CLOSE`         | Cross (×) — generic close action                            |
| `SVG_SPINNER`       | Eight-spoke spinner — used by `LoaderButton`                |
| `SVG_CHECK`         | Checkmark — success confirmation                            |
| `SVG_CROSS`         | Cross (×) — error or dismissal (alias of `SVG_CLOSE` style) |

### Notification icons (`stroke="white"`)

These icons use a white stroke for legibility on the colored backgrounds of `NotificationBanner`.

| Constant      | Level     | Description             |
| ------------- | --------- | ----------------------- |
| `SVG_INFO`    | `INFO`    | Circle with "i" dot     |
| `SVG_WARNING` | `WARNING` | Triangle with "!" lines |
| `SVG_ERROR`   | `ERROR`   | Circle with × lines     |
| `SVG_SUCCESS` | `SUCCESS` | Circle with checkmark   |

```python
from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt
from ezqt_widgets.widgets.shared.defaults import SVG_CHECK

renderer = QSvgRenderer(QByteArray(SVG_CHECK))
pixmap = QPixmap(QSize(16, 16))
pixmap.fill(Qt.GlobalColor.transparent)
painter = QPainter(pixmap)
renderer.render(painter)
painter.end()
```

---

::: ezqt_widgets.widgets.shared.defaults
options:
show_source: false
members: - ANIMATION_DURATION_FAST - ANIMATION_DURATION_NORMAL - ANIMATION_DURATION_SLOW - ICON_SIZE_SMALL - ICON_SIZE_NORMAL - ICON_SIZE_LARGE - ICON_SIZE_XLARGE - SVG_FOLDER - SVG_SEARCH - SVG_EYE_OPEN - SVG_EYE_CLOSED - SVG_CALENDAR - SVG_CHEVRON_RIGHT - SVG_CHEVRON_DOWN - SVG_CLOSE - SVG_INFO - SVG_WARNING - SVG_ERROR - SVG_SUCCESS - SVG_SPINNER - SVG_CHECK - SVG_CROSS
