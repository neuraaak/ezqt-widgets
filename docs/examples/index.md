# Examples

Usage examples and demonstrations for the **ezqt_widgets** library.

---

## Available Example Scripts

| Script                | Description                   | Widgets                                                                |
| --------------------- | ----------------------------- | ---------------------------------------------------------------------- |
| `run_all_examples.py` | GUI launcher for all examples | All                                                                    |
| `button_example.py`   | Button examples               | DateButton, IconButton, LoaderButton                                   |
| `input_example.py`    | Input examples                | AutoCompleteInput, SearchInput, TabReplaceTextEdit                     |
| `label_example.py`    | Label examples                | ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel             |
| `misc_example.py`     | Miscellaneous examples        | CircularTimer, DraggableList, OptionSelector, ToggleIcon, ToggleSwitch |

---

## Running Examples

### With Python

```bash
# Full GUI launcher
python examples/run_all_examples.py

# By category
python examples/button_example.py
python examples/input_example.py
python examples/label_example.py
python examples/misc_example.py
```

### With the CLI

```bash
# All examples with GUI
ezqt run --all

# By category
ezqt run --buttons
ezqt run --inputs
ezqt run --labels
ezqt run --misc

# Sequential mode (without GUI)
ezqt run --all --no-gui
```

---

## Code Examples

### Button Widgets

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import DateButton, IconButton, LoaderButton

app = QApplication([])

# Date button
date_btn = DateButton(placeholder="Pick a date")
date_btn.dateChanged.connect(lambda date: print(f"Date: {date}"))
date_btn.show()

# Icon button
icon_btn = IconButton(icon="path/to/icon.png", text="Click")
icon_btn.clicked.connect(lambda: print("Clicked"))
icon_btn.show()

# Loader button
loader_btn = LoaderButton(text="Load", loading_text="Loading...")
loader_btn.loadingStarted.connect(lambda: print("Loading..."))
loader_btn.show()

app.exec()
```

### Input Widgets

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import AutoCompleteInput, SearchInput, TabReplaceTextEdit

app = QApplication([])

# Auto-completion
auto_input = AutoCompleteInput(completions=["Apple", "Banana", "Cherry"])
auto_input.textChanged.connect(lambda text: print(f"Text: {text}"))
auto_input.show()

# Search
search_input = SearchInput()
search_input.searchSubmitted.connect(lambda query: print(f"Search: {query}"))
search_input.show()

# Text editor with tab replacement
text_edit = TabReplaceTextEdit()
text_edit.setPlainText("Type here...")
text_edit.show()

app.exec()
```

### Label Widgets

```python
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ezqt_widgets import ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel

app = QApplication([])

# Clickable tag
tag = ClickableTagLabel(name="Python", enabled=True)
tag.clicked.connect(lambda: print("Tag clicked"))
tag.show()

# Framed label
framed = FramedLabel(text="Framed label", alignment=Qt.AlignmentFlag.AlignCenter)
framed.show()

# Hover label
hover = HoverLabel(text="Hover me", hover_icon="path/to/icon.png")
hover.hoverIconClicked.connect(lambda: print("Icon clicked"))
hover.show()

# Status indicator
indicator = IndicatorLabel(
    status_map={
        "online": {"text": "Online", "state": "ok", "color": "#28a745"},
        "offline": {"text": "Offline", "state": "error", "color": "#dc3545"},
    },
    initial_status="online",
)
indicator.statusChanged.connect(lambda status: print(f"Status: {status}"))
indicator.show()

app.exec()
```

### Miscellaneous Widgets

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

# Circular timer
timer = CircularTimer(duration=5000, loop=True)
timer.cycleCompleted.connect(lambda: print("Cycle completed"))
timer.startTimer()
timer.show()

# Drag & drop list
draggable = DraggableList(items=["Item 1", "Item 2", "Item 3"])
draggable.itemMoved.connect(
    lambda item_id, old_pos, new_pos: print(f"Moved: {item_id}")
)
draggable.show()

# Option selector
selector = OptionSelector(options=["A", "B", "C"])
selector.valueChanged.connect(lambda value: print(f"Selected: {value}"))
selector.show()

# Toggle switch
switch = ToggleSwitch(checked=True)
switch.toggled.connect(lambda checked: print(f"Switch: {checked}"))
switch.show()

app.exec()
```

---

## Advanced Example: Dashboard

```python
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
)
from ezqt_widgets import CircularTimer, DraggableList, ToggleSwitch, IndicatorLabel


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - ezqt_widgets")
        self.setGeometry(100, 100, 1000, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Control panel
        control_panel = QWidget()
        control_layout = QVBoxLayout(control_panel)

        self.session_timer = CircularTimer(
            duration=3600000, ring_color="#007bff", loop=True
        )
        control_layout.addWidget(QLabel("Session time:"))
        control_layout.addWidget(self.session_timer)

        self.service_status = IndicatorLabel(
            status_map={
                "running": {"text": "Active", "state": "ok", "color": "#28a745"},
                "stopped": {"text": "Stopped", "state": "error", "color": "#dc3545"},
            },
            initial_status="running",
        )
        control_layout.addWidget(QLabel("Service status:"))
        control_layout.addWidget(self.service_status)

        self.auto_save = ToggleSwitch(checked=True)
        control_layout.addWidget(QLabel("Auto-save:"))
        control_layout.addWidget(self.auto_save)

        layout.addWidget(control_panel)

        # Task panel
        task_panel = QWidget()
        task_layout = QVBoxLayout(task_panel)

        self.task_list = DraggableList(
            items=["Analyze data", "Generate report", "Send notifications"],
            compact=True,
            icon_color="#28a745",
            max_height=300,
        )
        task_layout.addWidget(QLabel("Tasks:"))
        task_layout.addWidget(self.task_list)

        layout.addWidget(task_panel)
        self.session_timer.startTimer()


if __name__ == "__main__":
    app = QApplication([])
    dashboard = Dashboard()
    dashboard.show()
    app.exec()
```

---

## Resources

- [API Reference](../api/index.md) -- Detailed documentation
- [QSS Style Guide](../guides/style-guide.md) -- Visual customization
- [CLI](../cli/index.md) -- Run examples from the terminal
