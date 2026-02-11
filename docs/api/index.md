# API Reference

Complete API reference for **EzQt Widgets** library.

## Overview

The EzQt Widgets API provides **16 specialized Qt widgets** organized into **4 modules**. All widgets are fully typed, support Qt signals, and can be styled with QSS (Qt Style Sheets).

## Quick Reference

| Component           | Description                    | Documentation                          |
| ------------------- | ------------------------------ | -------------------------------------- |
| [Button](button.md) | Date, icon, and loader buttons | Specialized button widgets             |
| [Input](input.md)   | Advanced input fields          | Auto-complete, search, password        |
| [Label](label.md)   | Interactive label widgets      | Tags, hover effects, status indicators |
| [Misc](misc.md)     | Utility widgets                | Timers, drag-drop, toggles, selectors  |

## Import Examples

All widgets can be imported directly from the package:

```python
from ezqt_widgets import ToggleSwitch, DateButton, AutoCompleteInput
```

Or from submodules:

```python
from ezqt_widgets.button import DateButton
from ezqt_widgets.input import AutoCompleteInput
from ezqt_widgets.label import IndicatorLabel
from ezqt_widgets.misc import ToggleSwitch
```

---

## Modules

| Module              | Widgets                                                                                           | Description                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Button](button.md) | `DateButton`, `DatePickerDialog`, `IconButton`, `LoaderButton`                                    | Specialized buttons with calendar, icons and loading animations |
| [Input](input.md)   | `AutoCompleteInput`, `PasswordInput`, `SearchInput`, `TabReplaceTextEdit`                         | Input fields with auto-completion, search and advanced editing  |
| [Label](label.md)   | `ClickableTagLabel`, `FramedLabel`, `HoverLabel`, `IndicatorLabel`                                | Interactive labels with tags, hover effects and LED indicators  |
| [Misc](misc.md)     | `CircularTimer`, `DraggableList`, `DraggableItem`, `OptionSelector`, `ToggleIcon`, `ToggleSwitch` | Utility widgets: timers, drag & drop, toggles, selectors        |

---

## API Design Principles

### Type Safety

EzQt Widgets provides complete type hints for all public APIs:

- **Full type annotations** - Python 3.10+ type hints throughout
- **IDE support** - Excellent auto-completion and error detection
- **Type checking** - Compatible with mypy, pyright, and other type checkers
- **Runtime validation** - Type hints used for parameter validation

```python
from ezqt_widgets import DateButton, ToggleSwitch
from PySide6.QtCore import QDate

# Type-safe widget creation
date_btn: DateButton = DateButton(placeholder="Select date")
switch: ToggleSwitch = ToggleSwitch(checked=True)

# Type-safe signal connections
def handle_date(date: QDate) -> None:
    print(f"Date: {date.toString()}")

date_btn.dateChanged.connect(handle_date)
```

### Qt Integration

Seamless integration with PySide6 and Qt framework:

- **Native Qt Signals** - Standard Qt signal/slot mechanism
- **QWidget inheritance** - All widgets inherit from Qt base classes
- **Qt properties** - Widgets expose Qt properties for binding
- **Event handling** - Standard Qt event system support

```python
from ezqt_widgets import ToggleSwitch
from PySide6.QtCore import Signal, QObject

class MyController(QObject):
    stateChanged = Signal(bool)

    def __init__(self):
        super().__init__()
        self.switch = ToggleSwitch()
        self.switch.toggled.connect(self.stateChanged.emit)
```

### QSS Customization

Full Qt stylesheet support for visual customization:

- **QSS styling** - Complete Qt stylesheet customization
- **Pseudo-states** - Support for `:hover`, `:pressed`, `:disabled`, etc.
- **Custom properties** - Widgets can be styled with custom QSS properties
- **Theme support** - Easy to create custom themes

```python
from ezqt_widgets import DateButton

date_btn = DateButton()
date_btn.setStyleSheet("""
    DateButton {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    DateButton:hover {
        background-color: #2980b9;
    }
""")
```

### Animation Support

Smooth animations with configurable easing curves:

- **QPropertyAnimation** - Built-in property animations
- **Easing curves** - Configurable easing functions
- **Duration control** - Adjustable animation timing
- **Performance** - Optimized for smooth 60 FPS animations

```python
from ezqt_widgets import ToggleSwitch
from PySide6.QtCore import QEasingCurve

switch = ToggleSwitch(
    animation_duration=300,  # milliseconds
    animation_curve=QEasingCurve.Type.OutCubic
)
```

---

## Quick Start Example

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=True)
switch.toggled.connect(lambda state: print(f"Switch: {state}"))
switch.show()

app.exec()
```

---

## Installation

```bash
pip install ezqt-widgets
```

For development installation:

```bash
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt_widgets
pip install -e ".[dev]"
```

---

## Detailed Documentation

Select a module from the navigation menu or the table above to view detailed widget documentation with:

- Complete method signatures
- Signal descriptions
- Property documentation
- Usage examples
- QSS styling examples

## Module Documentation

| Module              | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| [Button](button.md) | Specialized buttons with calendar, icons, and loading       |
| [Input](input.md)   | Input fields with auto-completion and advanced editing      |
| [Label](label.md)   | Interactive labels with tags, hover effects, and indicators |
| [Misc](misc.md)     | Utility widgets: timers, drag & drop, toggles, selectors    |

---

## Need Help?

- **Quick Start**: See [Getting Started](../getting-started.md)
- **Examples**: Check out [Examples](../examples/index.md)
- **Guides**: Read [User Guides](../guides/index.md)
- **Issues**: Report bugs on [GitHub](https://github.com/neuraaak/ezqt-widgets/issues)
