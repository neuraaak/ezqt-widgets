# EzQt Widgets

[![PyPI](https://img.shields.io/badge/PyPI-ezqt--widgets-orange.svg)](https://pypi.org/project/ezqt-widgets/)
[![PyPI version](https://img.shields.io/pypi/v/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![License](https://img.shields.io/pypi/l/ezqt-widgets)](https://github.com/neuraaak/ezqt-widgets/blob/main/LICENSE)

**EzQt Widgets** is a collection of custom and reusable Qt widgets for PySide6. It provides advanced, typed graphical components to facilitate the development of modern desktop interfaces.

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])
switch = ToggleSwitch(checked=False, width=50, height=24)
switch.toggled.connect(lambda state: print(f"On: {state}"))
switch.show()
app.exec()
```

---

## Requirements

| Dependency | Version           |
| ---------- | ----------------- |
| Python     | >= 3.11           |
| PySide6    | >= 6.7.3, < 7.0.0 |

---

## Widgets

EzQt Widgets exposes **23 public classes** organized in 4 modules.

### Button

| Widget             | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `DateButton`       | Button displaying a selected date; opens a calendar dialog on click |
| `DatePickerDialog` | Modal calendar dialog for date selection                            |
| `IconButton`       | Button with an icon from any source and optional text label         |
| `LoaderButton`     | Button with animated loading spinner, success, and error states     |

### Input

| Widget               | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| `AutoCompleteInput`  | QLineEdit with configurable auto-completion suggestions                              |
| `FilePickerInput`    | QLineEdit and folder button that opens a QFileDialog for file or directory selection |
| `PasswordInput`      | Password field with strength bar and visibility toggle                               |
| `SearchInput`        | Search field with keyboard-navigable submission history                              |
| `SpinBoxInput`       | Custom numeric spin box with − and + buttons and mouse wheel support                 |
| `TabReplaceTextEdit` | QPlainTextEdit that sanitizes pasted text by replacing tab characters                |

### Label

| Widget              | Description                                            |
| ------------------- | ------------------------------------------------------ |
| `ClickableTagLabel` | Toggleable tag label that emits signals on click       |
| `FramedLabel`       | QLabel inside a QFrame for advanced styling and layout |
| `HoverLabel`        | QLabel that displays a floating icon when hovered      |
| `IndicatorLabel`    | Status indicator with a configurable colored LED       |

### Misc

| Widget               | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| `CircularTimer`      | Animated circular progress arc with loop and click support                     |
| `CollapsibleSection` | Accordion-style section with clickable header and expand/collapse animation    |
| `DraggableItem`      | Single draggable item used inside a DraggableList                              |
| `DraggableList`      | Scrollable list with drag-and-drop reordering and item removal                 |
| `NotificationBanner` | Animated slide-down notification banner with INFO/WARNING/ERROR/SUCCESS levels |
| `OptionSelector`     | Animated option selector with single-selection radio behavior                  |
| `ThemeIcon`          | QIcon subclass that adapts color to the active dark/light theme                |
| `ToggleIcon`         | Label with two icons toggled between an open and closed state                  |
| `ToggleSwitch`       | Modern animated toggle switch                                                  |

---

## Documentation

| Section                               | Description                             |
| ------------------------------------- | --------------------------------------- |
| [Getting Started](getting-started.md) | Installation and first working example  |
| [API Reference](api/index.md)         | Full class-level API documentation      |
| [User Guides](guides/index.md)        | Task-oriented guides                    |
| [Examples](examples/index.md)         | Runnable examples organized by category |
| [CLI Reference](cli/index.md)         | `ezqt-widgets` command documentation    |
| [Changelog](changelog.md)             | Version history                         |

---

## Links

- **Repository**: [https://github.com/neuraaak/ezqt-widgets](https://github.com/neuraaak/ezqt-widgets)
- **PyPI**: [https://pypi.org/project/ezqt-widgets/](https://pypi.org/project/ezqt-widgets/)
- **Issues**: [https://github.com/neuraaak/ezqt-widgets/issues](https://github.com/neuraaak/ezqt-widgets/issues)
