# Input widgets

Text input widgets with auto-completion, password management, search history, tab sanitization, file selection, and numeric spin input.

---

## AutoCompleteInput

A `QLineEdit` subclass with a built-in `QCompleter` powered by a configurable list of string suggestions.

::: ezqt_widgets.widgets.input.auto_complete_input.AutoCompleteInput
options:
members_order: source

---

## FilePickerInput

A composite `QWidget` combining a `QLineEdit` and a folder icon button that opens a `QFileDialog` for file or directory selection.

::: ezqt_widgets.widgets.input.file_picker_input.FilePickerInput
options:
members_order: source

---

## PasswordInput

A `QWidget` containing a `QLineEdit` in password mode with an optional strength bar and a visibility-toggle icon.

::: ezqt_widgets.widgets.input.password_input.PasswordInput
options:
members_order: source

---

## SearchInput

A `QLineEdit` subclass that maintains a submission history navigable with the Up/Down arrow keys.

::: ezqt_widgets.widgets.input.search_input.SearchInput
options:
members_order: source

---

## SpinBoxInput

A custom numeric spin box `QWidget` with decrement and increment buttons flanking a central `QLineEdit`.

::: ezqt_widgets.widgets.input.spin_box_input.SpinBoxInput
options:
members_order: source

---

## TabReplaceTextEdit

A `QPlainTextEdit` subclass that replaces tab characters with a configurable string on paste.

::: ezqt_widgets.widgets.input.tab_replace_textedit.TabReplaceTextEdit
options:
members_order: source

---

## AutoCompleteInput

A `QLineEdit` subclass with a built-in `QCompleter` powered by a configurable list of string suggestions.

**Constructor parameters:**

| Parameter         | Type                        | Default                                     | Description                                   |
| ----------------- | --------------------------- | ------------------------------------------- | --------------------------------------------- |
| `parent`          | `QWidget \| None`           | `None`                                      | Parent widget                                 |
| `suggestions`     | `list[str] \| None`         | `None`                                      | Initial list of completion candidates         |
| `case_sensitive`  | `bool`                      | `False`                                     | Whether completion matching is case-sensitive |
| `filter_mode`     | `Qt.MatchFlag`              | `Qt.MatchFlag.MatchContains`                | How typed text is matched against suggestions |
| `completion_mode` | `QCompleter.CompletionMode` | `QCompleter.CompletionMode.PopupCompletion` | How completions are presented                 |

**Properties:**

| Property          | Type                        | Description                                                          |
| ----------------- | --------------------------- | -------------------------------------------------------------------- |
| `suggestions`     | `list[str]`                 | Gets or sets the full list of completion candidates (returns a copy) |
| `case_sensitive`  | `bool`                      | Gets or sets case-sensitivity of matching                            |
| `filter_mode`     | `Qt.MatchFlag`              | Gets or sets the filter mode                                         |
| `completion_mode` | `QCompleter.CompletionMode` | Gets or sets the completion mode                                     |

**Methods:**

| Method               | Signature                   | Description                                   |
| -------------------- | --------------------------- | --------------------------------------------- |
| `addSuggestion()`    | `(suggestion: str) -> None` | Adds a candidate if it is not already present |
| `removeSuggestion()` | `(suggestion: str) -> None` | Removes a candidate if it exists              |
| `clearSuggestions()` | `() -> None`                | Removes all candidates                        |
| `refreshStyle()`     | `() -> None`                | Re-applies the QSS stylesheet                 |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import AutoCompleteInput

app = QApplication([])

inp = AutoCompleteInput(
    suggestions=["Python", "PySide6", "Qt", "PyQt6"],
    case_sensitive=False,
)
inp.addSuggestion("Rust")
inp.show()

app.exec()
```

::: ezqt_widgets.widgets.input.auto_complete_input.AutoCompleteInput

---

## PasswordInput

A `QWidget` containing a `QLineEdit` in password mode, an optional colored strength bar, and a visibility-toggle icon.

**Signals:**

| Signal            | Signature | Emitted when                                                       |
| ----------------- | --------- | ------------------------------------------------------------------ |
| `strengthChanged` | `(int)`   | The password text changes; value is the new strength score (0–100) |
| `iconClicked`     | `()`      | The visibility-toggle icon is clicked                              |

**Constructor parameters:**

| Parameter             | Type                              | Default         | Description                                              |
| --------------------- | --------------------------------- | --------------- | -------------------------------------------------------- |
| `parent`              | `QWidget \| None`                 | `None`          | Parent widget                                            |
| `show_strength`       | `bool`                            | `True`          | Whether to display the strength progress bar             |
| `strength_bar_height` | `int`                             | `3`             | Height of the strength bar in pixels                     |
| `show_icon`           | `QIcon \| QPixmap \| str \| None` | icons8 URL      | Icon displayed when the password is hidden (eye-open)    |
| `hide_icon`           | `QIcon \| QPixmap \| str \| None` | icons8 URL      | Icon displayed when the password is visible (eye-closed) |
| `icon_size`           | `QSize \| tuple[int, int]`        | `QSize(16, 16)` | Size of the toggle icon                                  |

**Properties:**

| Property              | Type            | Description                                          |
| --------------------- | --------------- | ---------------------------------------------------- |
| `password`            | `str`           | Gets or sets the raw password text                   |
| `show_strength`       | `bool`          | Gets or sets strength bar visibility                 |
| `strength_bar_height` | `int`           | Gets or sets the bar height in pixels (minimum 1)    |
| `show_icon`           | `QIcon \| None` | Gets or sets the icon shown when password is hidden  |
| `hide_icon`           | `QIcon \| None` | Gets or sets the icon shown when password is visible |
| `icon_size`           | `QSize`         | Gets or sets the toggle icon size                    |

**Methods:**

| Method             | Signature             | Description                                         |
| ------------------ | --------------------- | --------------------------------------------------- |
| `togglePassword()` | `() -> None`          | Switches the echo mode and updates the toggle icon  |
| `updateStrength()` | `(text: str) -> None` | Recalculates the strength score and updates the bar |
| `refreshStyle()`   | `() -> None`          | Triggers a repaint                                  |

**Strength score:**

The score ranges from 0 to 100. Each criterion adds points:

| Criterion                  | Points |
| -------------------------- | ------ |
| Length >= 8                | +25    |
| Contains uppercase letter  | +15    |
| Contains lowercase letter  | +15    |
| Contains digit             | +20    |
| Contains special character | +25    |

Bar color by score: 0–29 red, 30–59 orange, 60–79 green, 80–100 dark green.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import PasswordInput

app = QApplication([])

field = PasswordInput(show_strength=True, strength_bar_height=4)
field.strengthChanged.connect(lambda score: print(f"Strength: {score}/100"))
field.show()

app.exec()
```

::: ezqt_widgets.widgets.input.password_input.PasswordInput

---

## SearchInput

A `QLineEdit` subclass that maintains a submission history navigable with the Up/Down arrow keys and emits `searchSubmitted` when the user presses Enter.

**Signals:**

| Signal            | Signature | Emitted when                                                     |
| ----------------- | --------- | ---------------------------------------------------------------- |
| `searchSubmitted` | `(str)`   | The user presses Enter/Return; the text is also added to history |

**Constructor parameters:**

| Parameter       | Type                              | Default  | Description                                |
| --------------- | --------------------------------- | -------- | ------------------------------------------ |
| `parent`        | `QWidget \| None`                 | `None`   | Parent widget                              |
| `max_history`   | `int`                             | `20`     | Maximum number of history entries to keep  |
| `search_icon`   | `QIcon \| QPixmap \| str \| None` | `None`   | Optional icon displayed in the field       |
| `icon_position` | `str`                             | `"left"` | Icon position: `"left"` or `"right"`       |
| `clear_button`  | `bool`                            | `True`   | Whether to show Qt's built-in clear button |

**Properties:**

| Property        | Type            | Description                                            |
| --------------- | --------------- | ------------------------------------------------------ |
| `search_icon`   | `QIcon \| None` | Gets or sets the search icon                           |
| `icon_position` | `str`           | Gets or sets the icon position (`"left"` or `"right"`) |
| `clear_button`  | `bool`          | Gets or sets clear button visibility                   |
| `max_history`   | `int`           | Gets or sets the history size limit                    |

**Methods:**

| Method           | Signature                           | Description                                                                |
| ---------------- | ----------------------------------- | -------------------------------------------------------------------------- |
| `addToHistory()` | `(text: str) -> None`               | Adds a term to the front of history; ignores empty/whitespace-only strings |
| `getHistory()`   | `() -> list[str]`                   | Returns a copy of the current history list                                 |
| `clearHistory()` | `() -> None`                        | Empties the history and resets the navigation index                        |
| `setHistory()`   | `(history_list: list[str]) -> None` | Replaces history with the provided list, trimmed to `max_history`          |
| `refreshStyle()` | `() -> None`                        | Re-applies the QSS stylesheet                                              |

**Keyboard navigation:**

| Key                | Effect                                                               |
| ------------------ | -------------------------------------------------------------------- |
| `Enter` / `Return` | Submits current text, adds to history, emits `searchSubmitted`       |
| `Up`               | Navigates backward through history                                   |
| `Down`             | Navigates forward through history; restores current input at the end |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import SearchInput

app = QApplication([])

search = SearchInput(max_history=10, clear_button=True)
search.setPlaceholderText("Type and press Enter...")
search.searchSubmitted.connect(lambda q: print(f"Search: {q}"))
search.show()

app.exec()
```

::: ezqt_widgets.widgets.input.search_input.SearchInput

---

## TabReplaceTextEdit

A `QPlainTextEdit` subclass that intercepts paste events and replaces tab characters with a configurable string. Useful for pasting tabular or CSV data.

**Constructor parameters:**

| Parameter             | Type              | Default | Description                                         |
| --------------------- | ----------------- | ------- | --------------------------------------------------- |
| `parent`              | `QWidget \| None` | `None`  | Parent widget                                       |
| `tab_replacement`     | `str`             | `"\n"`  | String substituted for each `\t` character          |
| `sanitize_on_paste`   | `bool`            | `True`  | Whether to sanitize text on paste                   |
| `remove_empty_lines`  | `bool`            | `True`  | Whether to discard empty lines during sanitization  |
| `preserve_whitespace` | `bool`            | `False` | If `True`, keeps lines that contain only whitespace |

**Properties:**

| Property              | Type   | Description                                          |
| --------------------- | ------ | ---------------------------------------------------- |
| `tab_replacement`     | `str`  | Gets or sets the tab replacement string              |
| `sanitize_on_paste`   | `bool` | Gets or sets whether sanitization is active on paste |
| `remove_empty_lines`  | `bool` | Gets or sets whether empty lines are removed         |
| `preserve_whitespace` | `bool` | Gets or sets whitespace-only line preservation       |

**Methods:**

| Method           | Signature            | Description                                                                 |
| ---------------- | -------------------- | --------------------------------------------------------------------------- |
| `sanitizeText()` | `(text: str) -> str` | Applies tab replacement and optional empty-line removal; returns the result |
| `refreshStyle()` | `() -> None`         | Re-applies the QSS stylesheet                                               |

**Behavior notes:**

- Pressing the Tab key inserts `tab_replacement` at the cursor (no focus change).
- Paste events (Ctrl+V) are intercepted when `sanitize_on_paste` is `True` and route through `sanitizeText()` before insertion.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import TabReplaceTextEdit

app = QApplication([])

# Pasting "col1\tcol2\n\ncol3\tcol4" produces "col1;col2\ncol3;col4"
editor = TabReplaceTextEdit(
    tab_replacement=";",
    remove_empty_lines=True,
)
editor.show()

app.exec()
```

::: ezqt_widgets.widgets.input.tab_replace_textedit.TabReplaceTextEdit

---

## FilePickerInput

A composite `QWidget` combining a `QLineEdit` and a folder icon button that opens a `QFileDialog` for file or directory selection. Supports theme-aware icon rendering via `ThemeIcon`.

**Signals:**

| Signal         | Signature | Emitted when                                          |
| -------------- | --------- | ----------------------------------------------------- |
| `fileSelected` | `(str)`   | A path is chosen via the dialog                       |
| `pathChanged`  | `(str)`   | The text in the `QLineEdit` changes (every keystroke) |

**Constructor parameters:**

| Parameter      | Type                    | Default              | Description                                           |
| -------------- | ----------------------- | -------------------- | ----------------------------------------------------- |
| `parent`       | `QWidget \| None`       | `None`               | Parent widget                                         |
| `placeholder`  | `str`                   | `"Select a file..."` | Placeholder text for the `QLineEdit`                  |
| `mode`         | `"file" \| "directory"` | `"file"`             | Whether the dialog selects a file or a directory      |
| `filter`       | `str`                   | `""`                 | File filter string, e.g. `"Images (*.png *.jpg)"`     |
| `dialog_title` | `str`                   | `""`                 | Window title for the `QFileDialog`; auto-set if empty |

**Properties:**

| Property           | Type                    | Description                                            |
| ------------------ | ----------------------- | ------------------------------------------------------ |
| `path`             | `str`                   | Gets or sets the current path shown in the `QLineEdit` |
| `mode`             | `"file" \| "directory"` | Gets or sets the selection mode                        |
| `placeholder_text` | `str`                   | Gets or sets the `QLineEdit` placeholder text          |
| `filter`           | `str`                   | Gets or sets the file dialog filter string             |
| `dialog_title`     | `str`                   | Gets or sets the file dialog window title              |

**Methods:**

| Method           | Signature              | Description                                                       |
| ---------------- | ---------------------- | ----------------------------------------------------------------- |
| `clear()`        | `() -> None`           | Clears the current path from the `QLineEdit`                      |
| `setTheme()`     | `(theme: str) -> None` | Updates the folder icon color; connect to a `themeChanged` signal |
| `refreshStyle()` | `() -> None`           | Re-applies the QSS stylesheet                                     |

**Behavior notes:**

- `fileSelected` is emitted only when the user picks a path via the dialog, not on manual text edits.
- `pathChanged` is emitted on every text change in the `QLineEdit`, including manual entry.
- When `mode` is `"directory"`, the dialog default title is `"Select Directory"`; when `"file"`, it is `"Select File"`. Setting `dialog_title` overrides both defaults.
- Passing an invalid value to `mode` (neither `"file"` nor `"directory"`) leaves the mode unchanged.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import FilePickerInput

app = QApplication([])

picker = FilePickerInput(
    placeholder="Choose a CSV file...",
    mode="file",
    filter="CSV files (*.csv)",
)
picker.fileSelected.connect(lambda p: print(f"Selected: {p}"))
picker.pathChanged.connect(lambda p: print(f"Path text: {p}"))
picker.show()

app.exec()
```

::: ezqt_widgets.widgets.input.file_picker_input.FilePickerInput

---

## SpinBoxInput

A fully custom numeric spin box `QWidget` with integrated decrement (−) and increment (+) `QToolButton` flanking a central `QLineEdit`. Supports mouse wheel input and real-time `QIntValidator` clamping.

**Signals:**

| Signal         | Signature | Emitted when              |
| -------------- | --------- | ------------------------- |
| `valueChanged` | `(int)`   | The integer value changes |

**Constructor parameters:**

| Parameter | Type              | Default | Description                                            |
| --------- | ----------------- | ------- | ------------------------------------------------------ |
| `parent`  | `QWidget \| None` | `None`  | Parent widget                                          |
| `value`   | `int`             | `0`     | Initial value; clamped between `minimum` and `maximum` |
| `minimum` | `int`             | `0`     | Minimum allowed value                                  |
| `maximum` | `int`             | `100`   | Maximum allowed value                                  |
| `step`    | `int`             | `1`     | Increment/decrement step size (minimum 1)              |
| `prefix`  | `str`             | `""`    | String prepended to the displayed value                |
| `suffix`  | `str`             | `""`    | String appended to the displayed value                 |

**Properties:**

| Property  | Type  | Description                                                             |
| --------- | ----- | ----------------------------------------------------------------------- |
| `value`   | `int` | Gets or sets the current value; clamped and emits `valueChanged`        |
| `minimum` | `int` | Gets or sets the minimum; updates the validator and re-clamps the value |
| `maximum` | `int` | Gets or sets the maximum; updates the validator and re-clamps the value |
| `step`    | `int` | Gets or sets the step size (minimum 1)                                  |
| `prefix`  | `str` | Gets or sets the display prefix; refreshes the `QLineEdit`              |
| `suffix`  | `str` | Gets or sets the display suffix; refreshes the `QLineEdit`              |

**Methods:**

| Method           | Signature              | Description                                                                                                  |
| ---------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `setValue()`     | `(value: int) -> None` | Sets the value, clamped between minimum and maximum; emits `valueChanged` only if the value actually changes |
| `stepUp()`       | `() -> None`           | Increments the value by step, clamped at maximum                                                             |
| `stepDown()`     | `() -> None`           | Decrements the value by step, clamped at minimum                                                             |
| `refreshStyle()` | `() -> None`           | Re-applies the QSS stylesheet                                                                                |

**Behavior notes:**

- Mouse wheel scrolling increments (`scroll up`) or decrements (`scroll down`) by step when the widget has focus.
- `valueChanged` is emitted only when the value actually changes, not on every display refresh.
- `prefix` and `suffix` are stripped before parsing the `QLineEdit` text.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import SpinBoxInput

app = QApplication([])

spin = SpinBoxInput(value=10, minimum=0, maximum=200, step=5, suffix=" px")
spin.valueChanged.connect(lambda v: print(f"Value: {v}"))
spin.show()

app.exec()
```

::: ezqt_widgets.widgets.input.spin_box_input.SpinBoxInput
