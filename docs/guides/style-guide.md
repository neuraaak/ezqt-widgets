# EzQt Widgets -- QSS Style Guide

This document defines the QSS style conventions for the project's custom widgets.

## General Principles

- Use consistent colors, borders and rounded corners across all widgets.
- Prefer specific QSS selectors for each component.
- Centralize colors and spacing for easier maintenance.

---

## Inputs

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

## Labels

### ClickableTagLabel

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

Use the `status_color` property to customize the selected text color.

### HoverLabel

```css
HoverLabel {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
```

### IndicatorLabel

```css
IndicatorLabel {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
```

---

## Buttons

### DateButton

```css
DateButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
  selection-color: #ffffff;
  selection-background-color: #0078d4;
}
DateButton:hover {
  border: 1px solid #666666;
}
DateButton:focus {
  border: 1px solid #0078d4;
}
```

### LoaderButton

```css
LoaderButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
LoaderButton:hover {
  border: 1px solid #666666;
}
LoaderButton:focus {
  border: 1px solid #0078d4;
}
```

### IconButton

```css
IconButton {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}
IconButton:hover {
  border: 1px solid #666666;
}
IconButton:focus {
  border: 1px solid #0078d4;
}
```

---

## Misc

### CircularTimer

!!! note
This widget does not use QSS. Colors are controlled via Python properties:

    - `ring_color`: progression arc color
    - `node_color`: center color
    - `ring_width_mode`: arc thickness (`"small"`, `"medium"`, `"large"`)

```python
timer = CircularTimer(
    ring_color="#0078d4",
    node_color="#ffffff",
    ring_width_mode="medium",
    loop=True,
)
```

### OptionSelector

```css
OptionSelector {
  background-color: #2d2d2d;
  border: 1px solid #444444;
  border-radius: 4px;
}

/* Animated selector */
OptionSelector [type="OptionSelector_Selector"] {
  background-color: #0078d4;
  border: none;
  border-radius: 4px;
}
```

### ToggleIcon

```css
ToggleIcon {
  background-color: #2d2d2d;
  border: none;
  border-radius: 4px;
}
```

### ToggleSwitch

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

### DraggableList

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

The `dragging="true"` state is automatically applied during drag & drop.

---

## Best Practices

- Type properties are automatically defined in the widget code.
- Document each QSS section in this file.
- Test appearance across different OS and Qt themes.
- Use consistent colors for selection (`selection-color` and `selection-background-color`).
- Adapt colors to match your application's design system.
