# EzQt Widgets — QSS style guide

Per-widget QSS selector reference for `ezqt-widgets`. Each section lists the relevant
Qt property selectors and provides a minimal dark-theme stylesheet example.

!!! tip "Applying a global stylesheet"
    Set your stylesheet on the `QApplication` instance so it cascades to all widgets:

    ```python
    app = QApplication([])
    app.setStyleSheet(open("my_style.qss").read())
    ```

    Call `widget.refreshStyle()` after changing a widget's stylesheet at runtime to
    force the style engine to re-polish the widget.

!!! note "Type properties"
    Several widgets set a Qt `type` dynamic property on themselves (or on internal
    child frames). Use the `[type="..."]` attribute selector to target them in QSS.

---

## 🖋️ Input widgets

### AutoCompleteInput

```css
AutoCompleteInput {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  selection-color: #ffffff;
  selection-background-color: #0078d4;
}
AutoCompleteInput:hover {
  border: 1px solid #666666;
}
AutoCompleteInput:focus {
  border: 1px solid #0078d4;
}
```

### FilePickerInput

`FilePickerInput` is a composite widget. Target the outer frame and the internal
`QLineEdit` separately.

```css
FilePickerInput {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
FilePickerInput QLineEdit {
  background-color: transparent;
  border: none;
  color: #ffffff;
}
FilePickerInput QToolButton {
  background-color: transparent;
  border: none;
}
FilePickerInput QToolButton:hover {
  background-color: #3a3a3a;
  border-radius: 4px;
}
```

### PasswordInput

`PasswordInput` is a composite widget. Target the outer frame and the embedded
`QLineEdit` separately.

```css
PasswordInput {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
PasswordInput QLineEdit {
  background-color: transparent;
  border: none;
  color: #ffffff;
}
PasswordInput QProgressBar {
  background-color: #3a3a3a;
  border: none;
  border-radius: 2px;
}
PasswordInput QProgressBar::chunk {
  border-radius: 2px;
}
```

The strength bar color is set programmatically based on the score (red / orange /
green / dark green). Use `QProgressBar::chunk` only for border-radius overrides;
color overrides will be ignored at runtime.

### SearchInput

```css
SearchInput {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  selection-color: #ffffff;
  selection-background-color: #0078d4;
}
SearchInput:hover {
  border: 1px solid #666666;
}
SearchInput:focus {
  border: 1px solid #0078d4;
}
```

### SpinBoxInput

`SpinBoxInput` is a composite widget. Target the outer frame, the central
`QLineEdit`, and the flanking `QToolButton` controls separately.

```css
SpinBoxInput {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
SpinBoxInput QLineEdit {
  background-color: transparent;
  border: none;
  color: #ffffff;
  text-align: center;
}
SpinBoxInput QToolButton {
  background-color: transparent;
  border: none;
  color: #aaaaaa;
}
SpinBoxInput QToolButton:hover {
  background-color: #3a3a3a;
  color: #ffffff;
  border-radius: 4px;
}
SpinBoxInput QToolButton:pressed {
  background-color: #0078d4;
  color: #ffffff;
}
```

### TabReplaceTextEdit

```css
TabReplaceTextEdit {
  background-color: #2d2d2d;
  border-radius: 5px;
  padding: 10px;
  selection-color: #ffffff;
  selection-background-color: #0078d4;
}
TabReplaceTextEdit QScrollBar:vertical {
  width: 8px;
}
TabReplaceTextEdit QScrollBar:horizontal {
  height: 8px;
}
TabReplaceTextEdit:hover {
  border: 2px solid #666666;
}
TabReplaceTextEdit:focus {
  border: 2px solid #0078d4;
}
```

---

## 🏷️ Label widgets

### ClickableTagLabel

The widget sets a `status` dynamic property (`"selected"` or `"unselected"`) that
can be used as a QSS attribute selector.

```css
/* Unselected state */
ClickableTagLabel[status="unselected"] {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}

/* Selected state */
ClickableTagLabel[status="selected"] {
  background-color: #2d2d2d;
  border: 1px solid #0078d4;
  border-radius: 4px;
}

/* Inner label */
ClickableTagLabel QLabel {
  background-color: transparent;
  border: none;
  color: #ffffff;
}
```

Use the `status_color` constructor parameter to customize the selected text color
without overriding the QSS selector.

### FramedLabel

```css
FramedLabel {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
FramedLabel QLabel {
  background-color: transparent;
  border: none;
  color: #ffffff;
  padding: 4px 8px;
}
```

Use the `style_sheet` constructor parameter for per-instance overrides when a
global rule is not appropriate.

### HoverLabel

```css
HoverLabel {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
```

The hover icon is rendered via `QPainter` and is not addressable with QSS.
Use the `icon_color` and `opacity` constructor parameters to style it.

### IndicatorLabel

```css
IndicatorLabel {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
IndicatorLabel QLabel {
  background-color: transparent;
  border: none;
  color: #ffffff;
}
```

The LED circle color is driven by the `color` field of the active `status_map`
entry and is not controllable via QSS.

---

## 🔘 Button widgets

### DateButton

```css
DateButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  color: #ffffff;
}
DateButton:hover {
  border: 1px solid #666666;
}
DateButton:focus {
  border: 1px solid #0078d4;
}
```

### IconButton

```css
IconButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  color: #ffffff;
}
IconButton:hover {
  border: 1px solid #666666;
}
IconButton:focus {
  border: 1px solid #0078d4;
}
```

### LoaderButton

```css
LoaderButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  color: #ffffff;
}
LoaderButton:hover {
  border: 1px solid #666666;
}
LoaderButton:focus {
  border: 1px solid #0078d4;
}
```

---

## 🔧 Misc widgets

### CircularTimer

!!! note "No QSS support"
    `CircularTimer` is rendered entirely via `QPainter`. Use its Python properties
    instead of QSS:

    - `ring_color` — progression arc color
    - `node_color` — center fill color
    - `ring_width_mode` — arc thickness preset (`"small"`, `"medium"`, `"large"`)
    - `pen_width` — explicit arc thickness (overrides `ring_width_mode`)

    ```python
    timer = CircularTimer(
        ring_color="#0078d4",
        node_color="#1e1e1e",
        ring_width_mode="medium",
        loop=True,
    )
    ```

### CollapsibleSection

The header and the content area can be styled separately.

```css
CollapsibleSection {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 6px;
}

/* Header bar */
CollapsibleSection [type="CollapsibleSection_Header"] {
  background-color: #343b48;
  border-radius: 6px;
}

CollapsibleSection [type="CollapsibleSection_Header"]:hover {
  background-color: #3d4556;
}

/* Content area */
CollapsibleSection [type="CollapsibleSection_Content"] {
  background-color: #2d2d2d;
}
```

The header chevron icon color can be updated programmatically via `setTheme()`.

### DraggableList

The `dragging="true"` dynamic property is automatically applied to the item being
dragged, enabling a distinct drag-state style.

```css
DraggableList {
  background-color: #2c313a;
  border: 2px solid #343b48;
  border-radius: 6px;
  padding: 8px;
  color: rgb(255, 255, 255);
}

DraggableList QScrollArea {
  background-color: #1e2229;
  border: 2px solid #343b48;
  border-radius: 6px;
  padding: 4px 0px 4px 4px;
}

[type="DraggableItem"] {
  background-color: #2c313a;
  border: 1px solid #343b48;
  border-radius: 6px;
}

[type="DraggableItem"]:hover {
  background-color: #343b48;
  border: 2px solid #566070;
}

[type="DraggableItem"][dragging="true"] {
  background-color: #566070;
}

[type="DraggableItem"] QLabel {
  background-color: transparent;
  border: none;
}
```

### NotificationBanner

The banner background color is controlled by `NotificationLevel` and is not
overridable via QSS. Style the text and close button area:

```css
NotificationBanner {
  border-radius: 4px;
}

/* Message label */
NotificationBanner QLabel {
  background-color: transparent;
  color: #ffffff;
  font-weight: 600;
}

/* Close button */
NotificationBanner QToolButton {
  background-color: transparent;
  border: none;
  color: #ffffff;
}
NotificationBanner QToolButton:hover {
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 4px;
}
```

| `NotificationLevel` | Default background |
| ------------------- | ------------------ |
| `INFO`              | `#3b82f6`          |
| `WARNING`           | `#f59e0b`          |
| `ERROR`             | `#ef4444`          |
| `SUCCESS`           | `#22c55e`          |

### OptionSelector

The `[type="OptionSelector_Selector"]` pseudo-element targets the animated
selection rectangle that slides behind the active option.

```css
OptionSelector {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}

/* Animated selector rectangle */
OptionSelector [type="OptionSelector_Selector"] {
  background-color: #0078d4;
  border: none;
  border-radius: 4px;
}

/* Individual option labels */
OptionSelector FramedLabel {
  background-color: transparent;
  border: none;
  color: #cccccc;
}
```

### ThemeIcon

!!! note "No QSS support"
    `ThemeIcon` is a `QIcon` subclass, not a `QWidget`. It cannot be styled with
    QSS. Use the `dark_color` and `light_color` constructor parameters to set
    the recolor values per theme:

    ```python
    icon = ThemeIcon("path/to/icon.svg", dark_color="#FFFFFF", light_color="#333333")
    ```

### ToggleIcon

```css
ToggleIcon {
  background-color: #2d2d2d;
  border: none;
  border-radius: 4px;
}
```

The icon color is controlled by the `icon_color` constructor parameter and
`QColor` property, not by QSS.

### ToggleSwitch

The switch is drawn via `QPainter`. QSS applies only to the outer `QWidget`
boundary. The circle and track colors use the built-in defaults unless overridden
programmatically.

```css
ToggleSwitch {
  background-color: #2c313a;
  border: 2px solid #343b48;
  border-radius: 12px;
}
ToggleSwitch:hover {
  border: 2px solid #566070;
}
```

Default runtime colors (set via `QPainter`, not QSS):

| Element    | Off state            | On state             |
| ---------- | -------------------- | -------------------- |
| Background | `rgb(44, 49, 58)`    | `rgb(150, 205, 50)`  |
| Circle     | `rgb(255, 255, 255)` | `rgb(255, 255, 255)` |
| Border     | `rgb(52, 59, 72)`    | `rgb(52, 59, 72)`    |

---

## ✅ Best practices

- Apply global stylesheets to the `QApplication` instance for consistent appearance.
  Per-widget `setStyleSheet()` overrides are useful for dynamic theming.
- Call `refreshStyle()` after any programmatic stylesheet change to force the Qt
  style engine to re-polish the widget.
- Use dynamic property selectors (`[status="..."]`, `[type="..."]`, `[dragging="..."]`)
  to style state-dependent appearances without changing the class or adding extra
  widgets.
- Test your stylesheet under both the default Qt theme and a custom dark palette.
  Some color properties (especially `selection-background-color`) interact with the
  platform's native style engine.
- Keep color tokens centralised in one QSS file or a Python constant module.
  `ANIMATION_DURATION_*` and `ICON_SIZE_*` constants are available from
  `ezqt_widgets.widgets.shared` if you need to match widget timing in CSS
  transitions.
