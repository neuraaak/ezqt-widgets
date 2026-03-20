# API Reference

Complete parameter-level documentation for all public classes in ezqt_widgets 2.6.0.

All classes are importable directly from the top-level package:

```python
from ezqt_widgets import ClassName
```

---

## Button

| Class | Base class | Description |
| --- | --- | --- |
| [`DateButton`](button.md#datebutton) | `QToolButton` | Button displaying a date; opens calendar on click |
| [`DatePickerDialog`](button.md#datepickerdialog) | `QDialog` | Modal calendar dialog |
| [`IconButton`](button.md#iconbutton) | `QToolButton` | Button with icon from any source and optional text |
| [`LoaderButton`](button.md#loaderbutton) | `QToolButton` | Button with animated spinner and state management |

## Input

| Class | Base class | Description |
| --- | --- | --- |
| [`AutoCompleteInput`](input.md#autocompleteinput) | `QLineEdit` | Text input with configurable auto-completion |
| [`PasswordInput`](input.md#passwordinput) | `QWidget` | Password field with strength bar and visibility toggle |
| [`SearchInput`](input.md#searchinput) | `QLineEdit` | Search field with keyboard-navigable history |
| [`TabReplaceTextEdit`](input.md#tabreplacetextedit) | `QPlainTextEdit` | Text editor that sanitizes pasted tabs |

## Label

| Class | Base class | Description |
| --- | --- | --- |
| [`ClickableTagLabel`](label.md#clickabletaglabel) | `QFrame` | Toggleable tag label with signals |
| [`FramedLabel`](label.md#framedlabel) | `QFrame` | QLabel inside a QFrame for advanced styling |
| [`HoverLabel`](label.md#hoverlabel) | `QLabel` | Label that shows a floating icon on hover |
| [`IndicatorLabel`](label.md#indicatorlabel) | `QFrame` | Status indicator with a colored LED |

## Misc

| Class | Base class | Description |
| --- | --- | --- |
| [`CircularTimer`](misc.md#circulartimer) | `QWidget` | Animated circular arc timer |
| [`DraggableItem`](misc.md#draggableitem) | `QFrame` | Single draggable item for DraggableList |
| [`DraggableList`](misc.md#draggablelist) | `QWidget` | Scrollable list with drag-and-drop reordering |
| [`OptionSelector`](misc.md#optionselector) | `QFrame` | Animated single-selection option bar |
| [`ThemeIcon`](misc.md#themeicon) | `QIcon` | Theme-aware icon that adapts color to dark/light mode |
| [`ToggleIcon`](misc.md#toggleicon) | `QLabel` | Label toggling between two icons |
| [`ToggleSwitch`](misc.md#toggleswitch) | `QWidget` | Animated toggle switch |

---

## Type Aliases

The following type aliases are exported from `ezqt_widgets.types` and re-exported at the top level:

| Alias | Resolves to |
| --- | --- |
| `IconSource` | `QIcon \| str \| None` |
| `IconSourceExtended` | `QIcon \| QPixmap \| str \| None` |
| `SizeType` | `QSize \| tuple[int, int]` |
| `ColorType` | `QColor \| str` |
| `WidgetParent` | `QWidget \| None` |
| `AnimationDuration` | `int` (milliseconds) |
| `EventCallback` | `Callable[[], None]` |
| `ValueCallback` | `Callable[[Any], None]` |
