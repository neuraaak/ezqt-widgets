# Getting Started

## Installation

### From PyPI

```bash
pip install ezqt-widgets
```

### From Source

```bash
git clone https://github.com/neuraaak/ezqt_widgets.git
cd ezqt_widgets
pip install -e .
```

### Development Mode

```bash
pip install -e ".[dev]"
```

---

## Requirements

- **Python** >= 3.10
- **PySide6** >= 6.7.3

---

## First Widget in 5 Lines

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])
switch = ToggleSwitch(checked=True)
switch.toggled.connect(lambda state: print(f"State: {state}"))
switch.show()
app.exec()
```

---

## Imports

All widgets are accessible from the root package:

```python
# Direct imports
from ezqt_widgets import DateButton, IconButton, LoaderButton
from ezqt_widgets import AutoCompleteInput, SearchInput
from ezqt_widgets import ClickableTagLabel, IndicatorLabel
from ezqt_widgets import CircularTimer, DraggableList, ToggleSwitch
```

Or from submodules:

```python
from ezqt_widgets.button import DateButton
from ezqt_widgets.misc import ToggleSwitch
```

---

## Signal Connections

Each widget emits Qt signals to communicate state changes:

```python
from ezqt_widgets import DateButton, ToggleSwitch, IndicatorLabel

# Date button
date_btn = DateButton(placeholder="Pick a date")
date_btn.dateChanged.connect(lambda date: print(f"Date: {date}"))

# Toggle switch
switch = ToggleSwitch()
switch.toggled.connect(lambda checked: print(f"Active: {checked}"))

# Status indicator
indicator = IndicatorLabel(
    status_map={
        "ok": {"text": "Online", "state": "ok", "color": "#28a745"},
        "error": {"text": "Offline", "state": "error", "color": "#dc3545"},
    },
    initial_status="ok",
)
indicator.statusChanged.connect(lambda status: print(f"Status: {status}"))
```

---

## QSS Styling

Widgets support styling via QSS (Qt Style Sheets):

```python
switch = ToggleSwitch()
switch.setStyleSheet("""
    ToggleSwitch {
        background-color: #2d2d2d;
        border: 2px solid #444444;
        border-radius: 12px;
    }
""")
```

See the [QSS Style Guide](guides/style-guide.md) for per-widget examples.

---

## Explore with the CLI

```bash
# Run all examples
ezqt run --all

# Run by category
ezqt run --buttons
ezqt run --inputs
ezqt run --labels
ezqt run --misc
```

---

## Next Steps

- [API Reference](api/index.md) - Detailed documentation for each widget
- [Examples](examples/index.md) - Complete code examples by category
- [QSS Style Guide](guides/style-guide.md) - Visual customization
