# Getting Started

This guide will help you get started with **EzQt Widgets** quickly and easily.

## Installation

### From PyPI (Recommended)

```bash
pip install ezqt-widgets
```

### From Source

```bash
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt_widgets
pip install .
```

### Development Installation

For contributors and developers:

```bash
pip install -e ".[dev]"
```

This installs EzQt Widgets in editable mode with all development dependencies (testing, linting, formatting tools).

---

## Requirements

- **Python** >= 3.10
- **PySide6** >= 6.7.3

---

## First Steps

### Basic Widget Usage

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])
switch = ToggleSwitch(checked=True)
switch.toggled.connect(lambda state: print(f"State: {state}"))
switch.show()
app.exec()
```

### Multiple Widgets Example

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from ezqt_widgets import DateButton, ToggleSwitch, AutoCompleteInput

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

# Create widgets
date_btn = DateButton(placeholder="Pick a date")
switch = ToggleSwitch(checked=False, width=60, height=28)
auto_input = AutoCompleteInput(completions=["Apple", "Banana", "Cherry"])

# Add to layout
layout.addWidget(date_btn)
layout.addWidget(switch)
layout.addWidget(auto_input)

window.setLayout(layout)
window.show()
app.exec()
```

---

## Imports

All widgets are accessible from the root package:

```python
# Direct imports (recommended)
from ezqt_widgets import DateButton, IconButton, LoaderButton
from ezqt_widgets import AutoCompleteInput, SearchInput, PasswordInput
from ezqt_widgets import ClickableTagLabel, IndicatorLabel
from ezqt_widgets import CircularTimer, DraggableList, ToggleSwitch
```

Or from submodules:

```python
# Module-specific imports
from ezqt_widgets.button import DateButton
from ezqt_widgets.input import SearchInput
from ezqt_widgets.label import IndicatorLabel
from ezqt_widgets.misc import ToggleSwitch
```

---

## Signal Connections

Each widget emits Qt signals to communicate state changes:

### Date Selection

```python
from ezqt_widgets import DateButton
from PySide6.QtCore import QDate

date_btn = DateButton(placeholder="Pick a date")
date_btn.dateChanged.connect(lambda date: print(f"Selected: {date.toString()}"))

# Programmatically set date
date_btn.setDate(QDate.currentDate())
```

### Toggle Switch

```python
from ezqt_widgets import ToggleSwitch

switch = ToggleSwitch(checked=False)
switch.toggled.connect(lambda checked: print(f"Switch is: {'ON' if checked else 'OFF'}"))

# Programmatically toggle
switch.setChecked(True)
```

### Status Indicator

```python
from ezqt_widgets import IndicatorLabel

indicator = IndicatorLabel(
    status_map={
        "online": {"text": "System Online", "state": "ok", "color": "#28a745"},
        "offline": {"text": "System Offline", "state": "error", "color": "#dc3545"},
        "loading": {"text": "Loading...", "state": "warning", "color": "#ffc107"},
    },
    initial_status="loading",
)
indicator.statusChanged.connect(lambda status: print(f"Status: {status}"))

# Update status
indicator.setStatus("online")
```

### Auto-Complete Input

```python
from ezqt_widgets import AutoCompleteInput

auto_input = AutoCompleteInput(
    completions=["Python", "JavaScript", "TypeScript", "Rust", "Go"]
)
auto_input.textChanged.connect(lambda text: print(f"Input: {text}"))
```

---

## QSS Styling

Widgets support styling via QSS (Qt Style Sheets):

### Basic Styling

```python
from ezqt_widgets import ToggleSwitch

switch = ToggleSwitch()
switch.setStyleSheet("""
    ToggleSwitch {
        background-color: #2d2d2d;
        border: 2px solid #444444;
        border-radius: 12px;
    }
""")
```

### Advanced Styling

```python
from ezqt_widgets import DateButton

date_btn = DateButton()
date_btn.setStyleSheet("""
    DateButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 14px;
    }
    DateButton:hover {
        background-color: #2980b9;
    }
    DateButton:pressed {
        background-color: #1c5f8a;
    }
""")
```

See the [QSS Style Guide](guides/style-guide.md) for per-widget styling examples.

---

## Advanced Features

### Custom Animation Configuration

Many widgets support animation customization:

```python
from ezqt_widgets import ToggleSwitch
from PySide6.QtCore import QEasingCurve

switch = ToggleSwitch(
    checked=False,
    width=80,
    height=36,
    animation_duration=300,  # milliseconds
    animation_curve=QEasingCurve.Type.OutCubic
)
```

### Working with Widget Properties

Access and modify widget properties dynamically:

```python
from ezqt_widgets import CircularTimer

timer = CircularTimer(duration=5000, loop=False)

# Access properties
print(f"Duration: {timer.duration}")
print(f"Is running: {timer.isRunning()}")

# Modify properties
timer.setDuration(10000)
timer.setLoopEnabled(True)

# Connect to finished signal
timer.finished.connect(lambda: print("Timer completed!"))

# Start the timer
timer.start()
```

### Multiple Widget Integration

Combine widgets for complex interfaces:

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from ezqt_widgets import SearchInput, DraggableList, ToggleSwitch, IndicatorLabel

app = QApplication([])
window = QWidget()
main_layout = QVBoxLayout()

# Header with search and toggle
header_layout = QHBoxLayout()
search = SearchInput(max_history=10)
theme_toggle = ToggleSwitch(checked=False)
header_layout.addWidget(QLabel("Search:"))
header_layout.addWidget(search)
header_layout.addWidget(QLabel("Dark Mode:"))
header_layout.addWidget(theme_toggle)

# Draggable list
items_list = DraggableList()
items_list.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

# Footer with status
status = IndicatorLabel(
    status_map={
        "ready": {"text": "Ready", "state": "ok", "color": "#28a745"}
    },
    initial_status="ready"
)

# Combine layouts
main_layout.addLayout(header_layout)
main_layout.addWidget(items_list)
main_layout.addWidget(status)

window.setLayout(main_layout)
window.show()
app.exec()
```

---

## Type Hints Support

EzQt Widgets provides full type hints for better IDE support:

```python
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDate
from ezqt_widgets import DateButton, ToggleSwitch, IndicatorLabel
from typing import Optional

app: QApplication = QApplication([])

# Type-annotated widgets
date_btn: DateButton = DateButton(placeholder="Select date")
switch: ToggleSwitch = ToggleSwitch(checked=True)
indicator: IndicatorLabel = IndicatorLabel(
    status_map={"ok": {"text": "OK", "state": "ok", "color": "#28a745"}},
    initial_status="ok"
)

# Type-safe signal connections
def handle_date_change(date: QDate) -> None:
    print(f"Date selected: {date.toString()}")

def handle_toggle(checked: bool) -> None:
    print(f"Toggle state: {checked}")

def handle_status_change(status: str) -> None:
    print(f"Status changed to: {status}")

date_btn.dateChanged.connect(handle_date_change)
switch.toggled.connect(handle_toggle)
indicator.statusChanged.connect(handle_status_change)
```

### IDE Benefits

With full type hints, you get:

- **Auto-completion** for widget methods and properties
- **Type checking** with mypy, pyright, or IDE built-in checkers
- **Inline documentation** from docstrings
- **Error detection** before runtime

---

## Explore with the CLI

EzQt Widgets includes a command-line interface for testing and exploration:

```bash
# Run all widget examples
ezqt run --all

# Run by category
ezqt run --buttons
ezqt run --inputs
ezqt run --labels
ezqt run --misc

# Run specific widget
ezqt run --widget ToggleSwitch
ezqt run --widget DateButton

# Show information
ezqt info
ezqt --version

# Run tests
ezqt test --unit
ezqt test --coverage
```

For more details, see the [CLI Reference](cli/index.md).

---

## Next Steps

Now that you've set up EzQt Widgets, explore these resources:

- **[API Reference](api/index.md)** – Detailed documentation for each widget with all methods, signals, and properties
- **[Examples](examples/index.md)** – Complete code examples organized by widget category
- **[QSS Style Guide](guides/style-guide.md)** – Learn how to customize widget appearance with Qt stylesheets
- **[User Guides](guides/index.md)** – In-depth tutorials and best practices
- **[Testing Guide](guides/testing.md)** – Learn about the test suite and how to run tests
- **[Development Guide](guides/development.md)** – Set up your development environment and contribute

---

## Troubleshooting

### Import Error

If you encounter import errors:

```python
# Make sure you're importing from 'ezqt_widgets', not 'ezqt-widgets'
from ezqt_widgets import ToggleSwitch  # Correct
# from ezqt-widgets import ToggleSwitch  # Wrong (hyphens not allowed in Python imports)
```

### PySide6 Installation Issues

If PySide6 installation fails:

```bash
# Try upgrading pip first
pip install --upgrade pip

# Then install PySide6
pip install PySide6>=6.7.3

# Or install with wheel file (corporate environments)
pip install path/to/PySide6-6.7.3-cp310-cp310-win_amd64.whl
```

### Version Compatibility

Check your installed version:

```python
import ezqt_widgets
print(ezqt_widgets.__version__)  # Should be 2.3.3 or higher
```

Or from command line:

```bash
ezqt --version
```

### Widget Not Displaying

If widgets don't appear:

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch()
switch.show()  # Don't forget to show the widget!

app.exec()  # Must call exec() to start event loop
```

### Signal Connection Issues

Ensure proper signal connection syntax:

```python
from ezqt_widgets import DateButton

date_btn = DateButton()

# Correct - use .connect()
date_btn.dateChanged.connect(lambda date: print(date))

# Wrong - missing .connect()
# date_btn.dateChanged(lambda date: print(date))  # This will fail
```

---

## Need Help?

- **Documentation**: [Full API Reference](api/index.md)
- **Examples**: [Code Examples](examples/index.md)
- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezqt-widgets/issues)
- **Repository**: [https://github.com/neuraaak/ezqt-widgets](https://github.com/neuraaak/ezqt-widgets)

---

**Ready to build amazing Qt applications!** 🚀
