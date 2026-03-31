# Getting Started

This page covers installation and your first working widget in under five minutes.

---

## Installation

=== "uv"

```bash
uv add ezqt-widgets
```

=== "pip"

```bash
pip install ezqt-widgets
```

=== "Development mode"

```bash
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt-widgets
uv sync --all-extras
```

!!! note "Corporate / offline environments"
If direct PyPI access is unavailable, download the wheel file from
[PyPI](https://pypi.org/project/ezqt-widgets/#files) and install it locally:

```bash
pip install ezqt_widgets-2.6.5-py3-none-any.whl
```

PySide6 must also be available as a wheel. Place both wheels in the same directory
and run `pip install` with `--no-index --find-links ./wheels/`.

---

## Requirements

| Dependency | Minimum version |
| ---------- | --------------- |
| Python     | 3.11            |
| PySide6    | 6.7.3           |

The library raises `RuntimeError` at import time if the Python version is below 3.11.

---

## First Example

The example below creates a toggle switch, connects its signal, and starts the Qt event loop.

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=False, width=50, height=24)
switch.toggled.connect(lambda state: print(f"On: {state}"))
switch.show()

app.exec()
```

Run it and click the switch. The console prints `On: True` or `On: False` on each toggle.

---

## Imports

All public widgets are available directly from the top-level package:

```python
from ezqt_widgets import (
    # Button
    DateButton,
    DatePickerDialog,
    IconButton,
    LoaderButton,
    # Input
    AutoCompleteInput,
    FilePickerInput,
    PasswordInput,
    SearchInput,
    SpinBoxInput,
    TabReplaceTextEdit,
    # Label
    ClickableTagLabel,
    FramedLabel,
    HoverLabel,
    IndicatorLabel,
    # Misc
    CircularTimer,
    CollapsibleSection,
    DraggableItem,
    DraggableList,
    NotificationBanner,
    NotificationLevel,
    OptionSelector,
    ThemeIcon,
    ToggleIcon,
    ToggleSwitch,
)
```

Submodule imports are also valid:

```python
from ezqt_widgets.widgets.button import DateButton
from ezqt_widgets.widgets.input import SearchInput
from ezqt_widgets.widgets.label import IndicatorLabel
from ezqt_widgets.widgets.misc import ToggleSwitch
```

---

## A More Complete Example

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from ezqt_widgets import DateButton, ToggleSwitch, AutoCompleteInput

app = QApplication([])
window = QWidget()
layout = QVBoxLayout(window)

# Date picker button — displays today's date by default
date_btn = DateButton(placeholder="Pick a date")
date_btn.dateChanged.connect(lambda d: print(f"Date: {d.toString('dd/MM/yyyy')}"))

# Toggle switch — starts unchecked
switch = ToggleSwitch(checked=False, width=60, height=28)
switch.toggled.connect(lambda on: print(f"Switch: {'on' if on else 'off'}"))

# Auto-complete input with preset suggestions
language_input = AutoCompleteInput(suggestions=["Python", "Rust", "Go", "TypeScript"])

layout.addWidget(date_btn)
layout.addWidget(switch)
layout.addWidget(language_input)

window.setWindowTitle("EzQt Widgets — Quick Start")
window.show()
app.exec()
```

---

## Notification Banner Example

The example below shows how to overlay a `NotificationBanner` on a parent window and trigger it from a button click.

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from ezqt_widgets import NotificationBanner, NotificationLevel

app = QApplication([])

window = QWidget()
window.resize(600, 300)
layout = QVBoxLayout(window)

banner = NotificationBanner(parent=window)
banner.dismissed.connect(lambda: print("Banner dismissed"))

btn = QPushButton("Save configuration")
btn.clicked.connect(
    lambda: banner.showNotification(
        "Configuration saved.",
        NotificationLevel.SUCCESS,
        duration=3000,
    )
)

layout.addWidget(btn)
window.setWindowTitle("EzQt Widgets — Notification Banner")
window.show()
app.exec()
```

Click the button to show a green success banner that auto-dismisses after 3 seconds. Pass `duration=0` to require manual dismissal.

---

## Explore with the CLI

After installation the `ezqt-widgets` command is available:

```bash
# Show installed version
ezqt-widgets --version

# List available example files
ezqt-widgets list

# Run all examples with the GUI launcher
ezqt-widgets run --all

# Run examples by category
ezqt-widgets run --buttons
ezqt-widgets run --inputs
ezqt-widgets run --labels
ezqt-widgets run --misc
```

See [CLI Reference](cli/index.md) for the full command reference.

---

## Next Steps

- [API Reference](api/index.md) — parameter-level documentation for every widget
- [Examples](examples/index.md) — runnable code organized by category
- [Development Guide](guides/development.md) — set up a contributor environment
