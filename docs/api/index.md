# API Reference

Overview of the **ezqt_widgets** API.

All widgets can be imported directly from the package:

```python
from ezqt_widgets import ToggleSwitch, DateButton, AutoCompleteInput
```

---

## Modules

| Module              | Widgets                                                                                           | Description                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Button](button.md) | `DateButton`, `DatePickerDialog`, `IconButton`, `LoaderButton`                                    | Specialized buttons with calendar, icons and loading animations |
| [Input](input.md)   | `AutoCompleteInput`, `PasswordInput`, `SearchInput`, `TabReplaceTextEdit`                         | Input fields with auto-completion, search and advanced editing  |
| [Label](label.md)   | `ClickableTagLabel`, `FramedLabel`, `HoverLabel`, `IndicatorLabel`                                | Interactive labels with tags, hover effects and LED indicators  |
| [Misc](misc.md)     | `CircularTimer`, `DraggableList`, `DraggableItem`, `OptionSelector`, `ToggleIcon`, `ToggleSwitch` | Utility widgets: timers, drag & drop, toggles                   |

---

## Quick Install

```bash
pip install ezqt-widgets
```

## Minimal Example

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import ToggleSwitch

app = QApplication([])

switch = ToggleSwitch(checked=True)
switch.toggled.connect(lambda state: print(f"Switch: {state}"))
switch.show()

app.exec()
```
