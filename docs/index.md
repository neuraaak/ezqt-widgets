# Welcome to EzQt Widgets Documentation

[![PyPI](https://img.shields.io/badge/PyPI-ezqt--widgets-orange.svg)](https://pypi.org/project/ezqt-widgets/)
[![PyPI version](https://img.shields.io/pypi/v/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezqt-widgets)](https://pypi.org/project/ezqt-widgets/)
[![License](https://img.shields.io/pypi/l/ezqt-widgets)](https://github.com/neuraaak/ezqt_widgets/blob/main/LICENSE)

<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
  <img src="https://raw.githubusercontent.com/neuraaak/ezplog/refs/heads/main/docs/assets/logo-min.png" alt="Ezpl Logo" style="width: 80px; height: 80px; flex-shrink: 0;">
  <div>
    <strong>EzQt Widgets</strong> is a modern collection of custom and reusable Qt widgets for <strong>PySide6</strong> featuring advanced animated components, full type hints, and a simple API suitable for professional desktop applications.
  </div>
</div>![Ezpl logo]

## ✨ Key Features

- **✅ 16 Specialized Widgets**: Organized in 4 modules (button, input, label, misc)
- **✅ Smooth Animations**: Built-in `QPropertyAnimation` with configurable easing curves
- **✅ Fully Typed API**: Complete Python 3.10+ type hints for excellent IDE support
- **✅ Native Qt Signals**: Seamless integration with Qt's signal/slot system
- **✅ QSS Styling Support**: Full Qt stylesheet customization capabilities
- **✅ Built-in CLI**: Interactive command-line tool to explore and test widgets
- **✅ Comprehensive Tests**: 211+ unit tests with ~75% code coverage
- **✅ Production Ready**: Battle-tested components for professional applications

## 🚀 Quick Start

### Installation

```bash
pip install ezqt-widgets
```

Or from source:

```bash
git clone https://github.com/neuraaak/ezqt_widgets.git
cd ezqt_widgets && pip install .
```

### First Widget

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=True, width=60, height=28)
switch.toggled.connect(lambda state: print(f"Switch: {state}"))
switch.show()

app.exec()
```

## 📚 Documentation Structure

| Section                               | Description                                |
| ------------------------------------- | ------------------------------------------ |
| [Getting Started](getting-started.md) | Installation, basic usage, and first steps |
| [API Reference](api/index.md)         | Complete API documentation for all widgets |
| [User Guides](guides/index.md)        | In-depth guides and tutorials              |
| [Examples](examples/index.md)         | Practical examples and use cases           |
| [CLI Reference](cli/index.md)         | Command-line interface documentation       |

## 🎯 Main Components

EzQt Widgets provides **16 widgets** organized into **4 modules**:

### Button Module

- **`DateButton`** – Date picker button with integrated calendar dialog
- **`DatePickerDialog`** – Standalone calendar dialog for date selection
- **`IconButton`** – Button with icon support and optional text label
- **`LoaderButton`** – Button with integrated loading animation

### Input Module

- **`AutoCompleteInput`** – Text input with intelligent auto-completion
- **`PasswordInput`** – Secure password input with visibility toggle
- **`SearchInput`** – Search field with history management
- **`TabReplaceTextEdit`** – Advanced text editor with tab replacement

### Label Module

- **`ClickableTagLabel`** – Interactive tag label with toggle state
- **`FramedLabel`** – Label with customizable frame styling
- **`HoverLabel`** – Label with hover icon display
- **`IndicatorLabel`** – Status indicator with colored LED and states

### Misc Module

- **`CircularTimer`** – Animated circular countdown timer
- **`DraggableList`** – List widget with drag-and-drop reordering
- **`DraggableItem`** – Individual draggable list item component
- **`OptionSelector`** – Option selector with animated indicator
- **`ToggleIcon`** – Toggleable icon with open/closed states
- **`ToggleSwitch`** – Modern toggle switch with smooth animation

For detailed documentation, see [API Reference](api/index.md).

## 🧪 Testing

Comprehensive test suite covering all widgets and edge cases:

| Metric      | Value             |
| ----------- | ----------------- |
| Total tests | 211+              |
| Passing     | 211+ (100%)       |
| Coverage    | ~75%              |
| Test types  | Unit, Integration |

Run tests with:

```bash
pytest tests/
# Or using the CLI
ezqt test --unit
```

See the [Testing Guide](guides/testing.md) for complete details.

## 📦 Core Dependencies

- **PySide6 >= 6.7.3** – Qt for Python framework
- **Python >= 3.10** – Modern Python with type hints support
- **typing_extensions >= 4.0.0** – Extended typing support

## 🎨 Widget Categories

| Module                  | Widgets | Description                                                 |
| ----------------------- | ------- | ----------------------------------------------------------- |
| [Button](api/button.md) | 4       | Specialized buttons with calendar, icons, and loading       |
| [Input](api/input.md)   | 4       | Input fields with auto-completion and advanced editing      |
| [Label](api/label.md)   | 4       | Interactive labels with tags, hover effects, and indicators |
| [Misc](api/misc.md)     | 5       | Utility widgets: timers, drag & drop, toggles, selectors    |

## 📝 License

MIT License – See [LICENSE](https://github.com/neuraaak/ezqt_widgets/blob/main/LICENSE) file for details.

## 🔗 Links

- **Repository**: [https://github.com/neuraaak/ezqt_widgets](https://github.com/neuraaak/ezqt_widgets)
- **PyPI**: [https://pypi.org/project/ezqt-widgets/](https://pypi.org/project/ezqt-widgets/)
- **Issues**: [https://github.com/neuraaak/ezqt_widgets/issues](https://github.com/neuraaak/ezqt_widgets/issues)
- **Documentation**: [https://neuraaak.github.io/ezqt-widgets/](https://neuraaak.github.io/ezqt-widgets/)

---

**EzQt Widgets** – Modern, typed, and beautiful Qt widgets for Python. 🚀
