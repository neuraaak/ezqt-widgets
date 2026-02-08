# EzQt Widgets

[![PyPI version](https://img.shields.io/pypi/v/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![License](https://img.shields.io/pypi/l/ezqt-widgets)](https://github.com/neuraaak/ezqt_widgets/blob/main/LICENSE)

**ezqt_widgets** is a collection of custom and reusable Qt widgets for PySide6.
It provides advanced, animated and fully typed graphical components to facilitate
the development of modern and ergonomic interfaces.

---

## Features

- **16 widgets** organized in 4 modules (button, input, label, misc)
- **Smooth animations** with `QPropertyAnimation` and easing curves
- **Fully typed API** with Python 3.10+ type hints
- **Native Qt signals** for inter-component communication
- **QSS styling** support for appearance customization
- **Built-in CLI** to explore and test widgets
- **Test suite** with 211+ unit tests

---

## Quick Install

```bash
pip install ezqt-widgets
```

---

## First Widget

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=True, width=60, height=28)
switch.toggled.connect(lambda state: print(f"Switch: {state}"))
switch.show()

app.exec()
```

---

## Available Modules

| Module                  | Widgets | Description                                  |
| ----------------------- | ------- | -------------------------------------------- |
| [Button](api/button.md) | 4       | Buttons with calendar, icons, loading        |
| [Input](api/input.md)   | 4       | Input with auto-completion, search, password |
| [Label](api/label.md)   | 4       | Clickable tags, hover, LED indicators        |
| [Misc](api/misc.md)     | 5       | Timers, drag & drop, toggles, selectors      |

---

## Links

- [API Reference](api/index.md) - Complete documentation for each widget
- [Getting Started](getting-started.md) - Installation and first steps
- [Examples](examples/index.md) - Code examples by category
- [QSS Style Guide](guides/style-guide.md) - Visual customization
- [GitHub Repository](https://github.com/neuraaak/ezqt_widgets)
- [PyPI Package](https://pypi.org/project/ezqt-widgets/)
