# Examples

Runnable examples organized by widget category. Each script can be launched directly with Python or through the CLI.

---

## Running Examples

```bash
# Run all examples with the GUI launcher
ezqt-widgets run --all

# Run by category
ezqt-widgets run --buttons
ezqt-widgets run --inputs
ezqt-widgets run --labels
ezqt-widgets run --misc

# List available scripts
ezqt-widgets list
```

Or run a script directly:

```bash
python examples/button_example.py
python examples/input_example.py
python examples/label_example.py
python examples/misc_example.py
```

---

## Available Scripts

| Script                | Widgets demonstrated                                                             |
| --------------------- | -------------------------------------------------------------------------------- |
| `button_example.py`   | `DateButton`, `IconButton`, `LoaderButton`                                       |
| `input_example.py`    | `AutoCompleteInput`, `PasswordInput`, `SearchInput`, `TabReplaceTextEdit`        |
| `label_example.py`    | `ClickableTagLabel`, `FramedLabel`, `HoverLabel`, `IndicatorLabel`               |
| `misc_example.py`     | `CircularTimer`, `DraggableList`, `OptionSelector`, `ToggleIcon`, `ToggleSwitch` |
| `types_example.py`    | `IconSource`, `SizeType`, `ColorType` and other type aliases                     |
| `run_all_examples.py` | Launcher that starts all categories in sequence                                  |

---

## Button Examples

The `button_example.py` script demonstrates all three button widget types in a scrollable window:

- `DateButton` with date-change signal connected to a label
- `IconButton` with a QIcon, text, and click counter
- `LoaderButton` simulating a 2-second asynchronous operation

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import DateButton, IconButton, LoaderButton
from PySide6.QtCore import QTimer

app = QApplication([])

# Date picker with dd/MM/yyyy format
date_btn = DateButton(date_format="dd/MM/yyyy", placeholder="Pick a date")
date_btn.dateChanged.connect(lambda d: print(f"Date: {d.toString('dd/MM/yyyy')}"))

# Icon button — icon sourced from a URL
icon_btn = IconButton(
    icon="https://img.icons8.com/?size=100&id=8329&format=png&color=000000",
    text="Open",
    icon_size=(20, 20),
)

# Loader button with simulated async operation
loader_btn = LoaderButton(text="Submit", loading_text="Sending...", auto_reset=True)

def on_submit():
    loader_btn.startLoading()
    QTimer.singleShot(2000, lambda: loader_btn.stopLoading(success=True))

loader_btn.clicked.connect(on_submit)

date_btn.show()
icon_btn.show()
loader_btn.show()
app.exec()
```

---

## Input Examples

The `input_example.py` script demonstrates text input widgets:

- `AutoCompleteInput` with a fixed list of suggestions
- `PasswordInput` with a visible strength bar
- `SearchInput` with history navigation and Enter submission
- `TabReplaceTextEdit` that converts tabs to semicolons on paste

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import AutoCompleteInput, PasswordInput, SearchInput, TabReplaceTextEdit

app = QApplication([])

# Auto-complete with programming languages
lang_input = AutoCompleteInput(suggestions=["Python", "Rust", "Go", "TypeScript"])

# Password with strength bar
pwd_field = PasswordInput(show_strength=True)
pwd_field.strengthChanged.connect(lambda score: print(f"Strength: {score}/100"))

# Search with history
search = SearchInput(max_history=10)
search.searchSubmitted.connect(lambda q: print(f"Search: {q}"))

# Tab-to-semicolon replacement
editor = TabReplaceTextEdit(tab_replacement=";", remove_empty_lines=True)

lang_input.show()
pwd_field.show()
search.show()
editor.show()
app.exec()
```

---

## Label Examples

The `label_example.py` script demonstrates label widget types:

- `ClickableTagLabel` toggling state on click
- `FramedLabel` with centered text and custom styling
- `HoverLabel` showing an icon on mouse-over
- `IndicatorLabel` cycling through status states

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel

app = QApplication([])

# Tag that toggles between selected/unselected
tag = ClickableTagLabel(name="Python", enabled=False, status_color="#0078d4")
tag.stateChanged.connect(lambda on: print(f"Tag selected: {on}"))

# Framed label for section headers
header = FramedLabel(text="Section Header", min_height=30)

# Hover label with a removal icon
note = HoverLabel(
    text="Hover to reveal action",
    icon="https://img.icons8.com/?size=100&id=8329&format=png&color=000000",
    opacity=0.8,
)

# Status indicator cycling through states
status_map = {
    "idle":    {"text": "Idle",    "state": "none",  "color": "#808080"},
    "online":  {"text": "Online",  "state": "ok",    "color": "#4CAF50"},
    "offline": {"text": "Offline", "state": "error", "color": "#F44336"},
}
indicator = IndicatorLabel(status_map=status_map, initial_status="idle")
indicator.status = "online"

tag.show()
header.show()
note.show()
indicator.show()
app.exec()
```

---

## Misc Examples

The `misc_example.py` script demonstrates utility widgets:

- `CircularTimer` with a 10-second looping animation
- `DraggableList` with drag-and-drop reordering
- `OptionSelector` with four horizontal options
- `ToggleIcon` toggling between open and closed
- `ToggleSwitch` with an animated sliding circle

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import (
    CircularTimer,
    DraggableList,
    OptionSelector,
    ToggleIcon,
    ToggleSwitch,
)

app = QApplication([])

# 10-second looping arc timer
timer = CircularTimer(duration=10000, ring_color="#0078d4", loop=True)
timer.cycleCompleted.connect(lambda: print("cycle done"))
timer.startTimer()

# Reorderable task list
task_list = DraggableList(
    items=["design", "implement", "test", "deploy"],
    compact=False,
)
task_list.orderChanged.connect(lambda order: print(f"Order: {order}"))

# Horizontal option selector
period = OptionSelector(items=["Day", "Week", "Month"], default_id=0)
period.valueChanged.connect(lambda v: print(f"Period: {v}"))

# Toggle icon (default painted arrow)
arrow = ToggleIcon(initial_state="closed", icon_size=20)
arrow.stateChanged.connect(lambda s: print(f"Arrow: {s}"))

# Toggle switch
switch = ToggleSwitch(checked=False, width=50, height=24)
switch.toggled.connect(lambda on: print(f"Switch: {on}"))

timer.show()
task_list.show()
period.show()
arrow.show()
switch.show()
app.exec()
```
