# EzQt-Widgets

[![PyPI version](https://img.shields.io/pypi/v/ezqt-widgets?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezqt-widgets?style=flat&logo=python&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![PyPI status](https://img.shields.io/pypi/status/ezqt-widgets?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat&logo=github&logoColor=white)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/neuraaak/ezqt-widgets/publish-pypi.yml?style=flat&label=publish&logo=githubactions&logoColor=white)](https://github.com/neuraaak/ezqt-widgets/actions/workflows/publish-pypi.yml)
[![Docs](https://img.shields.io/badge/docs-Github%20Pages-blue?style=flat&logo=materialformkdocs&logoColor=white)](https://neuraaak.github.io/ezqt-widgets/)
[![uv](https://img.shields.io/badge/package%20manager-uv-DE5FE9?style=flat&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![linter](https://img.shields.io/badge/linter-ruff-orange?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![type checker](https://img.shields.io/badge/type%20checker-ty-orange?style=flat&logo=astral&logoColor=white)](https://github.com/astral-sh/ty)

![EzQt-Widgets Logo](docs/assets/logo-min.png)

**EzQt-Widgets** is a modern collection of custom and reusable Qt widgets for **PySide6** featuring advanced animated components, full type hints, and a simple API suitable for professional desktop applications.

## 📦 Installation

```bash
pip install ezqt-widgets
```

Or from source:

```bash
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt_widgets && pip install .
```

## 🚀 Quick Start

```python
from ezqt_widgets import DateButton, IconButton, ToggleSwitch, AutoCompleteInput
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Create widgets
date_button = DateButton(placeholder="Select a date")
icon_button = IconButton(icon="path/to/icon.png", text="Click me")
toggle = ToggleSwitch(checked=True)
auto_input = AutoCompleteInput(completions=["Option 1", "Option 2", "Option 3"])

# Connect signals
date_button.dateChanged.connect(lambda date: print(f"Date: {date}"))
icon_button.clicked.connect(lambda: print("Button clicked"))
toggle.toggled.connect(lambda checked: print(f"Toggle: {checked}"))

# Add to layout
layout.addWidget(date_button)
layout.addWidget(icon_button)
layout.addWidget(toggle)
layout.addWidget(auto_input)

window.setLayout(layout)
window.show()
app.exec()
```

## 🎯 Key Features

- **✅ PySide6 Compatible**: All widgets based on PySide6
- **✅ Full Type Hints**: Complete typing support for IDEs and linters
- **✅ Qt Signals**: Native integration with Qt signal system
- **✅ QSS Styling**: Complete Qt stylesheet support
- **✅ Smooth Animations**: Configurable animations with easing curves
- **✅ Accessibility**: Accessibility features support
- **✅ Comprehensive Tests**: Complete test suite (~211 tests, ~80% coverage)
- **✅ CLI Tools**: Command-line interface for examples and testing

## 📚 Documentation

Full documentation is available online: **[neuraaak.github.io/ezqt-widgets](https://neuraaak.github.io/ezqt-widgets/)**

- **[📖 Getting Started](https://neuraaak.github.io/ezqt_widgets/getting-started/)** – Installation and first steps
- **[🎯 API Reference](https://neuraaak.github.io/ezqt_widgets/api/)** – Complete widget reference (auto-generated)
- **[🎨 QSS Style Guide](https://neuraaak.github.io/ezqt_widgets/guides/style-guide/)** – QSS customization and best practices
- **[💡 Examples](https://neuraaak.github.io/ezqt_widgets/examples/)** – Usage examples and demonstrations
- **[🖥️ CLI](https://neuraaak.github.io/ezqt_widgets/cli/)** – Command-line interface guide
- **[🧪 Testing](https://neuraaak.github.io/ezqt_widgets/guides/testing/)** – Test suite documentation
- **[🔧 Development](https://neuraaak.github.io/ezqt_widgets/guides/development/)** – Environment setup and contribution

## 🧪 Testing

Comprehensive test suite with 211+ test cases covering all widgets.

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest tests/

# Run specific test types
python tests/run_tests.py --type unit

# With coverage
python tests/run_tests.py --coverage

# Using CLI
ezqt test --unit
ezqt test --coverage
```

See the **[Testing Guide](https://neuraaak.github.io/ezqt_widgets/guides/testing/)** for complete details.

## 🛠️ Development Setup

For contributors and developers:

```bash
# Clone and install in development mode
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt_widgets
pip install -e ".[dev]"

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Verify CLI installation
ezqt --version
ezqt info
```

See the **[Development Guide](https://neuraaak.github.io/ezqt_widgets/guides/development/)** for detailed setup instructions.

## 🎨 Available Widgets

### 🎛️ Button Widgets (3)

| Widget           | Description                                 |
| ---------------- | ------------------------------------------- |
| **DateButton**   | Date picker button with integrated calendar |
| **IconButton**   | Button with icon support and optional text  |
| **LoaderButton** | Button with integrated loading animation    |

### ⌨️ Input Widgets (3)

| Widget                 | Description                          |
| ---------------------- | ------------------------------------ |
| **AutoCompleteInput**  | Text field with autocompletion       |
| **SearchInput**        | Search field with history management |
| **TabReplaceTextEdit** | Text editor with tab replacement     |

### 🏷️ Label Widgets (4)

| Widget                | Description                       |
| --------------------- | --------------------------------- |
| **ClickableTagLabel** | Clickable tag with toggle state   |
| **FramedLabel**       | Framed label for advanced styling |
| **HoverLabel**        | Label with hover icon display     |
| **IndicatorLabel**    | Status indicator with colored LED |

### 🔧 Miscellaneous Widgets (6)

| Widget             | Description                               |
| ------------------ | ----------------------------------------- |
| **CircularTimer**  | Animated circular timer                   |
| **DraggableItem**  | Draggable list item component             |
| **DraggableList**  | List with draggable and reorderable items |
| **OptionSelector** | Option selector with animated selector    |
| **ToggleIcon**     | Toggleable icon (open/closed states)      |
| **ToggleSwitch**   | Modern toggle switch with animation       |

## 📦 Dependencies

- **PySide6>=6.0.0** – Qt for Python framework
- **typing_extensions>=4.0.0** – Extended typing support

## 🔧 Quick API Reference

```python
from ezqt_widgets import (
    # Button widgets
    DateButton, IconButton, LoaderButton,
    # Input widgets
    AutoCompleteInput, SearchInput, TabReplaceTextEdit,
    # Label widgets
    ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel,
    # Misc widgets
    CircularTimer, DraggableList, OptionSelector, ToggleIcon, ToggleSwitch,
)

# Button examples
date_btn = DateButton(placeholder="Select date")
icon_btn = IconButton(icon="path/to/icon.png", text="Click")
loader_btn = LoaderButton(loading_text="Loading...")

# Input examples
auto_input = AutoCompleteInput(completions=["A", "B", "C"])
search_input = SearchInput(max_history=20)

# Misc examples
timer = CircularTimer(duration=5000, loop=True)
switch = ToggleSwitch(checked=True)
selector = OptionSelector(options=["Small", "Medium", "Large"])
```

## 📄 License

MIT License – See [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: [https://github.com/neuraaak/ezqt-widgets](https://github.com/neuraaak/ezqt-widgets)
- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezqt-widgets/issues)
- **Documentation**: [neuraaak.github.io/ezqt_widgets](https://neuraaak.github.io/ezqt-widgets/)
- **PyPI**: [pypi.org/project/ezqt-widgets](https://pypi.org/project/ezqt-widgets/)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

**EzQt-Widgets** – Modern, typed, and beautiful Qt widgets for Python. 🎨
