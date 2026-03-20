# Miscellaneous Widgets

Utility widgets: animated circular timer, drag-and-drop list, option selector, theme-aware icon, toggleable icon, modern toggle switch, animated notification banner, and collapsible accordion section.

---

## CircularTimer

A `QWidget` that draws an animated arc representing elapsed time. The arc grows clockwise from the 12 o'clock position.

**Signals:**

| Signal           | Signature | Emitted when                                          |
| ---------------- | --------- | ----------------------------------------------------- |
| `timerReset`     | `()`      | `resetTimer()` is called                              |
| `clicked`        | `()`      | The widget is clicked                                 |
| `cycleCompleted` | `()`      | One full cycle ends (whether or not `loop` is `True`) |

**Constructor parameters:**

| Parameter         | Type                             | Default     | Description                                                              |
| ----------------- | -------------------------------- | ----------- | ------------------------------------------------------------------------ |
| `parent`          | `QWidget \| None`                | `None`      | Parent widget                                                            |
| `duration`        | `int`                            | `5000`      | Total cycle duration in milliseconds                                     |
| `ring_color`      | `QColor \| str`                  | `"#0078d4"` | Color of the progress arc; supports hex, rgb(), rgba(), and named colors |
| `node_color`      | `QColor \| str`                  | `"#2d2d2d"` | Fill color of the inner circle                                           |
| `ring_width_mode` | `"small" \| "medium" \| "large"` | `"medium"`  | Dynamic arc thickness preset                                             |
| `pen_width`       | `int \| float \| None`           | `None`      | Explicit arc thickness; takes priority over `ring_width_mode` if set     |
| `loop`            | `bool`                           | `False`     | Whether the animation restarts automatically at the end of each cycle    |

**Properties:**

| Property          | Type            | Description                                     |
| ----------------- | --------------- | ----------------------------------------------- |
| `duration`        | `int`           | Gets or sets the cycle duration in milliseconds |
| `elapsed`         | `int`           | Gets or sets the elapsed time in milliseconds   |
| `running`         | `bool`          | Read-only; `True` while the timer is active     |
| `ring_color`      | `QColor`        | Gets or sets the arc color                      |
| `node_color`      | `QColor`        | Gets or sets the inner circle color             |
| `ring_width_mode` | `str`           | Gets or sets the thickness preset               |
| `pen_width`       | `float \| None` | Gets or sets an explicit arc thickness          |
| `loop`            | `bool`          | Gets or sets whether the timer loops            |

**Methods:**

| Method           | Signature    | Description                                                 |
| ---------------- | ------------ | ----------------------------------------------------------- |
| `startTimer()`   | `() -> None` | Starts the animation from the current elapsed position      |
| `stopTimer()`    | `() -> None` | Stops the animation and resets elapsed to 0                 |
| `resetTimer()`   | `() -> None` | Resets elapsed to 0 and emits `timerReset` without stopping |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet                               |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import CircularTimer

app = QApplication([])

timer = CircularTimer(duration=10000, ring_color="#0078d4", loop=True)
timer.cycleCompleted.connect(lambda: print("cycle done"))
timer.clicked.connect(timer.resetTimer)
timer.startTimer()
timer.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.circular_timer.CircularTimer

---

## DraggableItem

A `QFrame` representing a single item in a `DraggableList`. It embeds a `HoverLabel` whose hover icon triggers removal.

**Signals:**

| Signal        | Signature | Emitted when                                         |
| ------------- | --------- | ---------------------------------------------------- |
| `itemClicked` | `(str)`   | The item is clicked; the string is `item_id`         |
| `itemRemoved` | `(str)`   | The removal icon is clicked; the string is `item_id` |

**Constructor parameters:**

| Parameter | Type                              | Default | Description                                                 |
| --------- | --------------------------------- | ------- | ----------------------------------------------------------- |
| `item_id` | `str`                             | —       | Unique identifier for this item (required)                  |
| `text`    | `str`                             | —       | Text displayed in the item (required)                       |
| `parent`  | `QWidget \| None`                 | `None`  | Parent widget                                               |
| `icon`    | `QIcon \| QPixmap \| str \| None` | `None`  | Icon for the HoverLabel; defaults to an icons8 drag icon    |
| `compact` | `bool`                            | `False` | Compact display mode (reduced height: 24–32 px vs 40–60 px) |

**Properties:**

| Property     | Type   | Description                                            |
| ------------ | ------ | ------------------------------------------------------ |
| `icon_color` | `str`  | Gets or sets the icon color of the internal HoverLabel |
| `compact`    | `bool` | Gets or sets compact mode; adjusts height constraints  |

**Methods:**

| Method           | Signature    | Description                   |
| ---------------- | ------------ | ----------------------------- |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet |

!!! note "Usage with DraggableList"
`DraggableItem` is designed to be managed by `DraggableList`.
Use `DraggableList.addItem()` rather than instantiating `DraggableItem` directly in most cases.

::: ezqt_widgets.widgets.misc.draggable_list.DraggableItem

---

## DraggableList

A `QWidget` containing a scrollable list of `DraggableItem` instances that can be reordered by drag-and-drop and removed individually.

**Signals:**

| Signal         | Signature         | Emitted when                                                                             |
| -------------- | ----------------- | ---------------------------------------------------------------------------------------- |
| `itemMoved`    | `(str, int, int)` | An item is dropped at a new position; args are `item_id`, `old_position`, `new_position` |
| `itemRemoved`  | `(str, int)`      | An item is removed; args are `item_id`, `position`                                       |
| `itemAdded`    | `(str, int)`      | An item is added; args are `item_id`, `position`                                         |
| `itemClicked`  | `(str)`           | An item is clicked; the string is `item_id`                                              |
| `orderChanged` | `(list)`          | The item order changes; the list is the new ordered `item_id` list                       |

**Constructor parameters:**

| Parameter         | Type                | Default | Description                                     |
| ----------------- | ------------------- | ------- | ----------------------------------------------- |
| `parent`          | `QWidget \| None`   | `None`  | Parent widget                                   |
| `items`           | `list[str] \| None` | `None`  | Initial list of item identifiers                |
| `allow_drag_drop` | `bool`              | `True`  | Whether drag-and-drop reordering is permitted   |
| `allow_remove`    | `bool`              | `True`  | Whether items can be removed via the hover icon |
| `max_height`      | `int`               | `300`   | Maximum widget height in pixels                 |
| `min_width`       | `int`               | `150`   | Minimum widget width in pixels                  |
| `compact`         | `bool`              | `False` | Compact display mode for all items              |

**Properties:**

| Property          | Type        | Description                                                                         |
| ----------------- | ----------- | ----------------------------------------------------------------------------------- |
| `items`           | `list[str]` | Gets or sets the full item list (returns a copy); setting rebuilds all item widgets |
| `item_count`      | `int`       | Read-only; number of items currently in the list                                    |
| `allow_drag_drop` | `bool`      | Gets or sets whether drag-and-drop is allowed                                       |
| `allow_remove`    | `bool`      | Gets or sets whether item removal is allowed; updates all existing items            |
| `icon_color`      | `str`       | Gets or sets the icon color for all items                                           |
| `compact`         | `bool`      | Gets or sets compact mode for all items                                             |
| `min_width`       | `int`       | Gets or sets the minimum widget width                                               |

**Methods:**

| Method              | Signature                                   | Description                                                                             |
| ------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------- |
| `addItem()`         | `(item_id: str, text: str \| None) -> None` | Adds an item; `text` defaults to `item_id` if `None`; no-op if `item_id` already exists |
| `removeItem()`      | `(item_id: str) -> bool`                    | Removes the item with the given id; returns `True` if found and removed                 |
| `clearItems()`      | `() -> None`                                | Removes all items and emits `orderChanged([])`                                          |
| `moveItem()`        | `(item_id: str, new_position: int) -> bool` | Moves an item to a new 0-based position; returns `True` on success                      |
| `getItemPosition()` | `(item_id: str) -> int`                     | Returns the 0-based position of the item, or -1 if not found                            |
| `refreshStyle()`    | `() -> None`                                | Re-applies the QSS stylesheet                                                           |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import DraggableList

app = QApplication([])

task_list = DraggableList(
    items=["design", "implement", "test", "deploy"],
    allow_drag_drop=True,
    allow_remove=True,
    compact=False,
)
task_list.itemMoved.connect(
    lambda id, old, new: print(f"Moved '{id}' from {old} to {new}")
)
task_list.itemRemoved.connect(
    lambda id, pos: print(f"Removed '{id}' at position {pos}")
)
task_list.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.draggable_list.DraggableList

---

## OptionSelector

A `QFrame` displaying a horizontal or vertical row of text options with an animated selector rectangle that slides to the chosen option.

**Signals:**

| Signal           | Signature | Emitted when                      |
| ---------------- | --------- | --------------------------------- |
| `clicked`        | `()`      | Any option is clicked             |
| `valueChanged`   | `(str)`   | The selected option text changes  |
| `valueIdChanged` | `(int)`   | The selected option index changes |

**Constructor parameters:**

| Parameter            | Type              | Default        | Description                                       |
| -------------------- | ----------------- | -------------- | ------------------------------------------------- |
| `items`              | `list[str]`       | —              | List of option texts to display (required)        |
| `default_id`         | `int`             | `0`            | Index of the initially selected option            |
| `min_width`          | `int \| None`     | `None`         | Minimum width                                     |
| `min_height`         | `int \| None`     | `None`         | Minimum height                                    |
| `orientation`        | `str`             | `"horizontal"` | Layout: `"horizontal"` or `"vertical"`            |
| `animation_duration` | `int`             | `300`          | Selector slide animation duration in milliseconds |
| `parent`             | `QWidget \| None` | `None`         | Parent widget                                     |

**Properties:**

| Property             | Type                  | Description                                         |
| -------------------- | --------------------- | --------------------------------------------------- |
| `value`              | `str`                 | Gets or sets the selected option by text            |
| `value_id`           | `int`                 | Gets or sets the selected option by index           |
| `options`            | `list[str]`           | Read-only; returns a copy of the options list       |
| `default_id`         | `int`                 | Gets or sets the default selection index            |
| `selected_option`    | `FramedLabel \| None` | Read-only; the currently selected option widget     |
| `orientation`        | `str`                 | Gets or sets the layout orientation                 |
| `min_width`          | `int \| None`         | Gets or sets minimum width                          |
| `min_height`         | `int \| None`         | Gets or sets minimum height                         |
| `animation_duration` | `int`                 | Gets or sets the animation duration in milliseconds |

**Methods:**

| Method                 | Signature                                    | Description                                                 |
| ---------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| `initializeSelector()` | `(default_id: int) -> None`                  | Positions the selector at the given index without animation |
| `addOption()`          | `(option_id: int, option_text: str) -> None` | Adds a new option at the given id position                  |
| `toggleSelection()`    | `(option_id: int) -> None`                   | Selects an option by id and animates the selector           |
| `moveSelector()`       | `(option: FramedLabel) -> None`              | Animates the selector to the given option widget            |
| `refreshStyle()`       | `() -> None`                                 | Re-applies the QSS stylesheet                               |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import OptionSelector

app = QApplication([])

selector = OptionSelector(
    items=["Day", "Week", "Month", "Year"],
    default_id=0,
    orientation="horizontal",
    animation_duration=250,
)
selector.valueChanged.connect(lambda v: print(f"Selected: {v}"))
selector.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.option_selector.OptionSelector

---

## ThemeIcon

A `QIcon` subclass that recolors itself to white (dark theme) or black (light theme) when the active theme changes. Custom colors for each theme can be specified.

**Constructor parameters:**

| Parameter     | Type                      | Default  | Description                                       |
| ------------- | ------------------------- | -------- | ------------------------------------------------- |
| `icon`        | `QIcon \| QPixmap \| str` | —        | Source icon (required); `None` raises `TypeError` |
| `theme`       | `str`                     | `"dark"` | Initial theme: `"dark"` or `"light"`              |
| `dark_color`  | `QColor \| str \| None`   | `None`   | Color applied in dark theme; defaults to white    |
| `light_color` | `QColor \| str \| None`   | `None`   | Color applied in light theme; defaults to black   |

**Properties:**

| Property        | Type    | Description                                                          |
| --------------- | ------- | -------------------------------------------------------------------- |
| `theme`         | `str`   | Gets or sets the active theme; setting recolors the icon immediately |
| `original_icon` | `QIcon` | Gets or sets the source icon; setting triggers a recolor             |

**Methods:**

| Method          | Signature                                                       | Description                                                                             |
| --------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `setTheme()`    | `(theme: str) -> None`                                          | Convenience alias for setting the `theme` property                                      |
| `from_source()` | `(source, theme, dark_color, light_color) -> ThemeIcon \| None` | Class method; returns `None` if `source` is `None`, otherwise wraps it in a `ThemeIcon` |

**Example:**

```python
from ezqt_widgets import ThemeIcon

# Auto dark/light colors (white in dark mode, black in light mode)
icon = ThemeIcon("path/to/icon.png", theme="dark")

# Custom colors
icon = ThemeIcon(
    "path/to/icon.svg",
    dark_color="#FFFFFF",
    light_color="#333333",
)

# Switch theme at runtime
icon.setTheme("light")

# Factory method — returns None if source is None
themed = ThemeIcon.from_source("path/to/icon.png", theme="dark")
```

::: ezqt_widgets.widgets.misc.theme_icon.ThemeIcon

---

## ToggleIcon

A `QLabel` that alternates between two icons representing an "opened" and a "closed" state. When no custom icons are provided, a built-in painted triangle arrow is used.

**Signals:**

| Signal         | Signature | Emitted when                                         |
| -------------- | --------- | ---------------------------------------------------- |
| `stateChanged` | `(str)`   | The state changes; value is `"opened"` or `"closed"` |
| `clicked`      | `()`      | The widget is clicked                                |

**Constructor parameters:**

| Parameter       | Type                              | Default    | Description                                                  |
| --------------- | --------------------------------- | ---------- | ------------------------------------------------------------ |
| `parent`        | `QWidget \| None`                 | `None`     | Parent widget                                                |
| `opened_icon`   | `QIcon \| QPixmap \| str \| None` | `None`     | Icon shown in the opened state; uses painted arrow if `None` |
| `closed_icon`   | `QIcon \| QPixmap \| str \| None` | `None`     | Icon shown in the closed state; uses painted arrow if `None` |
| `icon_size`     | `int`                             | `16`       | Icon size in pixels (square)                                 |
| `icon_color`    | `QColor \| str \| None`           | `None`     | Color applied to icons; defaults to semi-transparent white   |
| `initial_state` | `str`                             | `"closed"` | Starting state: `"opened"` or `"closed"`                     |
| `min_width`     | `int \| None`                     | `None`     | Minimum width                                                |
| `min_height`    | `int \| None`                     | `None`     | Minimum height                                               |

**Properties:**

| Property      | Type              | Description                                               |
| ------------- | ----------------- | --------------------------------------------------------- |
| `state`       | `str`             | Gets or sets the current state (`"opened"` or `"closed"`) |
| `opened_icon` | `QPixmap \| None` | Gets or sets the opened-state icon                        |
| `closed_icon` | `QPixmap \| None` | Gets or sets the closed-state icon                        |
| `icon_size`   | `int`             | Gets or sets the icon size in pixels                      |
| `icon_color`  | `QColor`          | Gets or sets the color applied to icons                   |
| `min_width`   | `int \| None`     | Gets or sets minimum width                                |
| `min_height`  | `int \| None`     | Gets or sets minimum height                               |

**Methods:**

| Method             | Signature    | Description                                |
| ------------------ | ------------ | ------------------------------------------ |
| `toggleState()`    | `() -> None` | Switches between `"opened"` and `"closed"` |
| `setStateOpened()` | `() -> None` | Forces state to `"opened"`                 |
| `setStateClosed()` | `() -> None` | Forces state to `"closed"`                 |
| `isOpened()`       | `() -> bool` | Returns `True` if state is `"opened"`      |
| `isClosed()`       | `() -> bool` | Returns `True` if state is `"closed"`      |
| `refreshStyle()`   | `() -> None` | Re-applies the QSS stylesheet              |

**Keyboard support:** Space, Enter, and Return keys toggle the state when the widget has focus.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleIcon

app = QApplication([])

toggle = ToggleIcon(initial_state="closed", icon_size=20)
toggle.stateChanged.connect(lambda s: print(f"State: {s}"))
toggle.toggleState()  # now "opened"
toggle.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.toggle_icon.ToggleIcon

---

## ToggleSwitch

A `QWidget` that renders an animated toggle switch with a sliding circle. Clicking or setting `checked` triggers a smooth animation.

**Signals:**

| Signal    | Signature | Emitted when                                      |
| --------- | --------- | ------------------------------------------------- |
| `toggled` | `(bool)`  | The checked state changes; value is the new state |

**Constructor parameters:**

| Parameter   | Type              | Default | Description                                 |
| ----------- | ----------------- | ------- | ------------------------------------------- |
| `parent`    | `QWidget \| None` | `None`  | Parent widget                               |
| `checked`   | `bool`            | `False` | Initial checked state                       |
| `width`     | `int`             | `50`    | Width of the switch in pixels (minimum 20)  |
| `height`    | `int`             | `24`    | Height of the switch in pixels (minimum 12) |
| `animation` | `bool`            | `True`  | Whether the circle slides with animation    |

**Properties:**

| Property    | Type   | Description                                                           |
| ----------- | ------ | --------------------------------------------------------------------- |
| `checked`   | `bool` | Gets or sets the toggle state; emits `toggled` and animates on change |
| `width`     | `int`  | Gets or sets the switch width                                         |
| `height`    | `int`  | Gets or sets the switch height                                        |
| `animation` | `bool` | Gets or sets whether animation is enabled                             |

**Methods:**

| Method           | Signature    | Description                         |
| ---------------- | ------------ | ----------------------------------- |
| `toggle()`       | `() -> None` | Inverts the current `checked` state |
| `refreshStyle()` | `() -> None` | Re-applies the QSS stylesheet       |

**Default colors (not configurable via constructor):**

| Element    | Off state            | On state             |
| ---------- | -------------------- | -------------------- |
| Background | `rgb(44, 49, 58)`    | `rgb(150, 205, 50)`  |
| Circle     | `rgb(255, 255, 255)` | `rgb(255, 255, 255)` |
| Border     | `rgb(52, 59, 72)`    | `rgb(52, 59, 72)`    |

Apply a QSS stylesheet to the parent or the application to override these colors.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=False, width=50, height=24, animation=True)
switch.toggled.connect(lambda on: print(f"On: {on}"))
switch.checked = True  # animates to the on position
switch.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.toggle_switch.ToggleSwitch

---

## NotificationBanner

An animated slide-down notification banner `QWidget` that overlays the top of a parent widget. The banner can auto-dismiss after a configurable duration, and always provides a manual close button.

### NotificationLevel

`NotificationLevel` is an `Enum` that sets the visual severity of the banner.

| Member    | Value       | Background color  |
| --------- | ----------- | ----------------- |
| `INFO`    | `"INFO"`    | `#3b82f6` (blue)  |
| `WARNING` | `"WARNING"` | `#f59e0b` (amber) |
| `ERROR`   | `"ERROR"`   | `#ef4444` (red)   |
| `SUCCESS` | `"SUCCESS"` | `#22c55e` (green) |

```python
from ezqt_widgets import NotificationLevel

level = NotificationLevel.SUCCESS
```

**Signals:**

| Signal      | Signature | Emitted when                                              |
| ----------- | --------- | --------------------------------------------------------- |
| `dismissed` | `()`      | The banner is hidden, whether by auto-dismiss or manually |

**Constructor parameters:**

| Parameter | Type      | Default | Description                                                          |
| --------- | --------- | ------- | -------------------------------------------------------------------- |
| `parent`  | `QWidget` | —       | The parent widget that hosts the banner overlay (required, not None) |

**Methods:**

| Method               | Signature                                                         | Description                                                     |
| -------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------- |
| `showNotification()` | `(message: str, level: NotificationLevel, duration: int) -> None` | Displays the banner with the given message, level, and duration |
| `refreshStyle()`     | `() -> None`                                                      | Re-applies the QSS stylesheet                                   |

**`showNotification()` parameters:**

| Parameter  | Type                | Default                  | Description                                                                    |
| ---------- | ------------------- | ------------------------ | ------------------------------------------------------------------------------ |
| `message`  | `str`               | —                        | Text displayed in the banner (required)                                        |
| `level`    | `NotificationLevel` | `NotificationLevel.INFO` | Severity level controlling background color and icon                           |
| `duration` | `int`               | `3000`                   | Display duration in milliseconds. Pass `0` for permanent (manual-only dismiss) |

**Behavior notes:**

- The banner is 48 px tall and spans the full width of the parent widget.
- Slide-in and slide-out use a `QPropertyAnimation` on geometry with an `OutCubic` easing curve (250 ms).
- Calling `showNotification()` while a banner is already visible cancels the previous auto-dismiss timer and replaces the content immediately.
- The banner tracks parent resize events via an event filter and repositions itself automatically while visible.
- The `parent` argument is mandatory. Passing `None` will raise an `AttributeError` at initialization.

**Example:**

```python
from PySide6.QtWidgets import QApplication, QWidget
from ezqt_widgets import NotificationBanner, NotificationLevel

app = QApplication([])

window = QWidget()
window.resize(600, 400)

banner = NotificationBanner(parent=window)
banner.dismissed.connect(lambda: print("Banner dismissed"))

# Show a success banner that auto-dismisses after 4 seconds
banner.showNotification(
    "Configuration saved successfully.",
    NotificationLevel.SUCCESS,
    duration=4000,
)

# Show a permanent error banner (requires manual close)
banner.showNotification(
    "Connection lost. Check network settings.",
    NotificationLevel.ERROR,
    duration=0,
)

window.show()
app.exec()
```

::: ezqt_widgets.widgets.misc.notification_banner.NotificationBanner

---

## CollapsibleSection

An accordion-style `QWidget` with a clickable header and smooth expand/collapse animation. The header is always visible; clicking it toggles the content area between its natural height and zero.

**Signals:**

| Signal            | Signature | Emitted when                                       |
| ----------------- | --------- | -------------------------------------------------- |
| `expandedChanged` | `(bool)`  | The expanded state changes; value is the new state |

**Constructor parameters:**

| Parameter  | Type              | Default | Description            |
| ---------- | ----------------- | ------- | ---------------------- |
| `parent`   | `QWidget \| None` | `None`  | Parent widget          |
| `title`    | `str`             | `""`    | Header title text      |
| `expanded` | `bool`            | `True`  | Initial expanded state |

**Properties:**

| Property      | Type   | Description                                                 |
| ------------- | ------ | ----------------------------------------------------------- |
| `title`       | `str`  | Gets or sets the header title text                          |
| `is_expanded` | `bool` | Read-only; `True` if the content area is currently expanded |

**Methods:**

| Method               | Signature                   | Description                                                                      |
| -------------------- | --------------------------- | -------------------------------------------------------------------------------- |
| `setContentWidget()` | `(widget: QWidget) -> None` | Sets the widget displayed in the collapsible area; replaces any previous content |
| `expand()`           | `() -> None`                | Expands the content area with animation; no-op if already expanded               |
| `collapse()`         | `() -> None`                | Collapses the content area with animation; no-op if already collapsed            |
| `toggle()`           | `() -> None`                | Toggles between expanded and collapsed states                                    |
| `setTheme()`         | `(theme: str) -> None`      | Updates the chevron icon color; connect to a `themeChanged` signal               |
| `refreshStyle()`     | `() -> None`                | Re-applies the QSS stylesheet                                                    |

**Behavior notes:**

- The expand/collapse animation operates on `maximumHeight` of the content area using `QPropertyAnimation` with an `InOutCubic` easing curve (200 ms).
- `expandedChanged` is emitted before the animation completes.
- Calling `setContentWidget()` replaces any previously set widget and re-applies the current expanded/collapsed state without animation.
- The header chevron uses a `ToggleIcon` and reflects the current state (chevron-down when expanded, chevron-right when collapsed).
- `setTheme()` propagates the theme to the internal `ToggleIcon` chevron.

**Example:**

```python
from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
from ezqt_widgets import CollapsibleSection

app = QApplication([])

# Build a form to use as content
form_widget = QWidget()
form_layout = QFormLayout(form_widget)
form_layout.addRow("Host:", QLineEdit("localhost"))
form_layout.addRow("Port:", QLineEdit("5432"))

section = CollapsibleSection(title="Database settings", expanded=False)
section.setContentWidget(form_widget)
section.expandedChanged.connect(lambda e: print(f"Expanded: {e}"))
section.show()

app.exec()
```

::: ezqt_widgets.widgets.misc.collapsible_section.CollapsibleSection
