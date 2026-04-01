# Label widgets

Interactive and styled label widgets: clickable tags, framed labels, hover icons, and LED status indicators.

---

## ClickableTagLabel

A `QFrame` that behaves as a toggleable tag with a selected and an unselected state.

::: ezqt_widgets.widgets.label.clickable_tag_label.ClickableTagLabel
options:
members_order: source

---

## FramedLabel

A `QFrame` containing a `QLabel`, providing the layout and styling flexibility of a frame with the simplicity of a label interface.

::: ezqt_widgets.widgets.label.framed_label.FramedLabel
options:
members_order: source

---

## HoverLabel

A `QLabel` that shows a floating icon in its right margin when the mouse hovers over it.

::: ezqt_widgets.widgets.label.hover_label.HoverLabel
options:
members_order: source

---

## IndicatorLabel

A `QFrame` combining a text label and a circular colored LED to represent a named status.

::: ezqt_widgets.widgets.label.indicator_label.IndicatorLabel
options:
members_order: source

---

## ClickableTagLabel

A `QFrame` that behaves as a toggleable tag. Clicking it switches between a selected and an unselected state and emits the corresponding signals.

**Signals:**

| Signal           | Signature | Emitted when                                       |
| ---------------- | --------- | -------------------------------------------------- |
| `clicked`        | `()`      | The tag is clicked                                 |
| `toggle_keyword` | `(str)`   | The tag is toggled; the string is the tag's `name` |
| `stateChanged`   | `(bool)`  | The `enabled` state changes; `True` means selected |

**Constructor parameters:**

| Parameter      | Type              | Default     | Description                                           |
| -------------- | ----------------- | ----------- | ----------------------------------------------------- |
| `name`         | `str`             | `""`        | Text displayed inside the tag                         |
| `enabled`      | `bool`            | `False`     | Initial selected state                                |
| `status_color` | `str`             | `"#0078d4"` | Color of the text when selected (any valid CSS color) |
| `min_width`    | `int \| None`     | `None`      | Minimum width; auto-calculated if `None`              |
| `min_height`   | `int \| None`     | `None`      | Minimum height; auto-calculated if `None`             |
| `parent`       | `QWidget \| None` | `None`      | Parent widget                                         |

**Properties:**

| Property       | Type          | Description                                                     |
| -------------- | ------------- | --------------------------------------------------------------- |
| `name`         | `str`         | Gets or sets the tag text; updates the display immediately      |
| `enabled`      | `bool`        | Gets or sets the selected state; emits `stateChanged` on change |
| `status_color` | `str`         | Gets or sets the color used when selected                       |
| `min_width`    | `int \| None` | Gets or sets the minimum width                                  |
| `min_height`   | `int \| None` | Gets or sets the minimum height                                 |

**Methods:**

| Method           | Signature    | Description                   |
| ---------------- | ------------ | ----------------------------- |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet |

**Keyboard support:** Space, Enter, and Return keys toggle the tag when it has focus.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ClickableTagLabel

app = QApplication([])

tag = ClickableTagLabel(name="Python", enabled=False, status_color="#0078d4")
tag.stateChanged.connect(lambda selected: print(f"Selected: {selected}"))
tag.toggle_keyword.connect(lambda kw: print(f"Toggled: {kw}"))
tag.show()

app.exec()
```

::: ezqt_widgets.widgets.label.clickable_tag_label.ClickableTagLabel

---

## FramedLabel

A `QFrame` containing a `QLabel`, providing the layout and styling flexibility of a frame with the simplicity of a label interface.

**Signals:**

| Signal        | Signature | Emitted when                                    |
| ------------- | --------- | ----------------------------------------------- |
| `textChanged` | `(str)`   | The `text` property is set to a different value |

**Constructor parameters:**

| Parameter     | Type               | Default                        | Description                                                                 |
| ------------- | ------------------ | ------------------------------ | --------------------------------------------------------------------------- |
| `text`        | `str`              | `""`                           | Initial label text                                                          |
| `parent`      | `QWidget \| None`  | `None`                         | Parent widget                                                               |
| `alignment`   | `Qt.AlignmentFlag` | `Qt.AlignmentFlag.AlignCenter` | Text alignment                                                              |
| `style_sheet` | `str \| None`      | `None`                         | Custom stylesheet applied to the QFrame; defaults to transparent background |
| `min_width`   | `int \| None`      | `None`                         | Minimum width                                                               |
| `min_height`  | `int \| None`      | `None`                         | Minimum height                                                              |

**Properties:**

| Property     | Type               | Description                                                |
| ------------ | ------------------ | ---------------------------------------------------------- |
| `text`       | `str`              | Gets or sets the label text; emits `textChanged` on change |
| `alignment`  | `Qt.AlignmentFlag` | Gets or sets the text alignment                            |
| `min_width`  | `int \| None`      | Gets or sets the minimum width                             |
| `min_height` | `int \| None`      | Gets or sets the minimum height                            |

**Methods:**

| Method           | Signature    | Description                   |
| ---------------- | ------------ | ----------------------------- |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import FramedLabel

app = QApplication([])

label = FramedLabel(text="Section Title", min_height=30)
label.textChanged.connect(lambda t: print(f"New text: {t}"))
label.text = "Updated Title"
label.show()

app.exec()
```

::: ezqt_widgets.widgets.label.framed_label.FramedLabel

---

## HoverLabel

A `QLabel` that shows a floating icon in its right margin when the mouse hovers over it. Clicking the icon emits `hoverIconClicked`.

**Signals:**

| Signal             | Signature | Emitted when                                              |
| ------------------ | --------- | --------------------------------------------------------- |
| `hoverIconClicked` | `()`      | The hover icon area is clicked with the left mouse button |

**Constructor parameters:**

| Parameter      | Type                              | Default         | Description                                             |
| -------------- | --------------------------------- | --------------- | ------------------------------------------------------- |
| `parent`       | `QWidget \| None`                 | `None`          | Parent widget                                           |
| `icon`         | `QIcon \| QPixmap \| str \| None` | `None`          | Icon to display on hover; supports paths, URLs, and SVG |
| `text`         | `str`                             | `""`            | Label text                                              |
| `opacity`      | `float`                           | `0.5`           | Opacity of the hover icon (0.0–1.0)                     |
| `icon_size`    | `QSize \| tuple[int, int]`        | `QSize(16, 16)` | Size of the hover icon                                  |
| `icon_color`   | `QColor \| str \| None`           | `None`          | Optional color overlay applied to the icon              |
| `icon_padding` | `int`                             | `8`             | Pixels of right padding reserved for the icon           |
| `icon_enabled` | `bool`                            | `True`          | Whether the hover icon is shown                         |
| `min_width`    | `int \| None`                     | `None`          | Minimum width                                           |

**Properties:**

| Property       | Type                    | Description                                     |
| -------------- | ----------------------- | ----------------------------------------------- |
| `opacity`      | `float`                 | Gets or sets the icon opacity                   |
| `hover_icon`   | `QIcon \| None`         | Gets or sets the hover icon; `None` hides it    |
| `icon_size`    | `QSize`                 | Gets or sets the icon size                      |
| `icon_color`   | `QColor \| str \| None` | Gets or sets the color overlay                  |
| `icon_padding` | `int`                   | Gets or sets the right-side padding in pixels   |
| `icon_enabled` | `bool`                  | Gets or sets whether the icon is shown on hover |

**Methods:**

| Method           | Signature    | Description                                         |
| ---------------- | ------------ | --------------------------------------------------- |
| `clearIcon()`    | `() -> None` | Removes the hover icon and clears the right padding |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet                       |

!!! note "URL icons"
Icon URLs are fetched asynchronously. The icon appears after the network
response completes.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import HoverLabel

app = QApplication([])

label = HoverLabel(
    text="Hover me",
    icon="https://img.icons8.com/?size=100&id=8329&format=png&color=000000",
    opacity=0.7,
    icon_color="#FF4444",
)
label.hoverIconClicked.connect(lambda: print("icon clicked"))
label.show()

app.exec()
```

::: ezqt_widgets.widgets.label.hover_label.HoverLabel

---

## IndicatorLabel

A `QFrame` combining a text label and a circular colored LED to represent a named status. States are defined by a `status_map` dictionary.

**Signals:**

| Signal          | Signature | Emitted when           |
| --------------- | --------- | ---------------------- |
| `statusChanged` | `(str)`   | The status key changes |

**Constructor parameters:**

| Parameter        | Type                                | Default     | Description                              |
| ---------------- | ----------------------------------- | ----------- | ---------------------------------------- |
| `parent`         | `QWidget \| None`                   | `None`      | Parent widget                            |
| `status_map`     | `dict[str, dict[str, str]] \| None` | `None`      | State definitions; see format below      |
| `initial_status` | `str`                               | `"neutral"` | Key of the status to display on creation |

**`status_map` format:**

Each key is a status name. Each value is a dict with three required keys:

```python
{
    "neutral": {"text": "Waiting",  "state": "none",  "color": "#A0A0A0"},
    "online":  {"text": "Online",   "state": "ok",    "color": "#4CAF50"},
    "partial": {"text": "Degraded", "state": "warn",  "color": "#FFC107"},
    "offline": {"text": "Offline",  "state": "ko",    "color": "#F44336"},
}
```

- `text`: string shown in the label
- `state`: value set as the Qt `state` property (for QSS selectors)
- `color`: any valid CSS color string for the LED circle

**Default `status_map`** (used when `status_map` is `None`):

| Key         | text               | state   | color   |
| ----------- | ------------------ | ------- | ------- |
| `"neutral"` | Waiting            | none    | #A0A0A0 |
| `"online"`  | Online             | ok      | #4CAF50 |
| `"partial"` | Services disrupted | partial | #FFC107 |
| `"offline"` | Offline            | ko      | #F44336 |

**Properties:**

| Property | Type  | Description                                                      |
| -------- | ----- | ---------------------------------------------------------------- |
| `status` | `str` | Gets or sets the current status key; setting calls `setStatus()` |

**Methods:**

| Method           | Signature               | Description                                                                             |
| ---------------- | ----------------------- | --------------------------------------------------------------------------------------- |
| `setStatus()`    | `(status: str) -> None` | Sets the status and updates the display; raises `ValueError` if key not in `status_map` |
| `refreshStyle()` | `() -> None`            | Re-applies the QSS stylesheet                                                           |

!!! warning "Unknown status key"
`setStatus()` raises `ValueError` if the given key is not present in `status_map`.
Always ensure the key exists before calling it.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import IndicatorLabel

app = QApplication([])

status_map = {
    "idle":    {"text": "Idle",       "state": "none",  "color": "#808080"},
    "running": {"text": "Running",    "state": "ok",    "color": "#4CAF50"},
    "error":   {"text": "Error",      "state": "error", "color": "#F44336"},
}
indicator = IndicatorLabel(status_map=status_map, initial_status="idle")
indicator.statusChanged.connect(lambda s: print(f"Status: {s}"))
indicator.status = "running"
indicator.show()

app.exec()
```

::: ezqt_widgets.widgets.label.indicator_label.IndicatorLabel
