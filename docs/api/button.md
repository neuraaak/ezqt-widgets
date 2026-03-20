# Button Widgets

Specialized button widgets for date selection, icon display, and loading state management.

---

## DateButton

A `QToolButton` that displays the currently selected date and opens a calendar dialog when clicked.

**Signals:**

| Signal         | Signature | Emitted when                                                                        |
| -------------- | --------- | ----------------------------------------------------------------------------------- |
| `dateChanged`  | `(QDate)` | The date property changes, whether from user interaction or programmatic assignment |
| `dateSelected` | `(QDate)` | The user confirms a date in the calendar dialog                                     |

**Constructor parameters:**

| Parameter            | Type                       | Default           | Description                                         |
| -------------------- | -------------------------- | ----------------- | --------------------------------------------------- |
| `parent`             | `QWidget \| None`          | `None`            | Parent widget                                       |
| `date`               | `QDate \| str \| None`     | `None`            | Initial date; `None` defaults to today              |
| `date_format`        | `str`                      | `"dd/MM/yyyy"`    | Qt date format string used for display and parsing  |
| `placeholder`        | `str`                      | `"Select a date"` | Text shown when no valid date is set                |
| `show_calendar_icon` | `bool`                     | `True`            | Whether to show the calendar icon inside the button |
| `icon_size`          | `QSize \| tuple[int, int]` | `QSize(16, 16)`   | Size of the calendar icon                           |
| `min_width`          | `int \| None`              | `None`            | Minimum width; auto-calculated if `None`            |
| `min_height`         | `int \| None`              | `None`            | Minimum height; auto-calculated if `None`           |

**Properties:**

| Property             | Type          | Description                                                     |
| -------------------- | ------------- | --------------------------------------------------------------- |
| `date`               | `QDate`       | Gets or sets the selected date; setting to `None` clears it     |
| `date_string`        | `str`         | Gets or sets the date as a formatted string using `date_format` |
| `date_format`        | `str`         | Gets or sets the display/parse format                           |
| `placeholder`        | `str`         | Gets or sets the placeholder text                               |
| `show_calendar_icon` | `bool`        | Gets or sets calendar icon visibility                           |
| `icon_size`          | `QSize`       | Gets or sets the calendar icon size                             |
| `min_width`          | `int \| None` | Gets or sets the minimum width                                  |
| `min_height`         | `int \| None` | Gets or sets the minimum height                                 |

**Methods:**

| Method           | Returns | Description                                           |
| ---------------- | ------- | ----------------------------------------------------- |
| `clearDate()`    | `None`  | Sets the date to an invalid QDate (shows placeholder) |
| `setToday()`     | `None`  | Sets the date to today's date                         |
| `openCalendar()` | `None`  | Opens the `DatePickerDialog` programmatically         |
| `refreshStyle()` | `None`  | Re-applies the QSS stylesheet after dynamic changes   |

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import DateButton

app = QApplication([])

btn = DateButton(
    date_format="dd/MM/yyyy",
    placeholder="Pick a date",
    show_calendar_icon=True,
)
btn.dateChanged.connect(lambda d: print(d.toString("dd/MM/yyyy")))
btn.setToday()
btn.show()

app.exec()
```

::: ezqt_widgets.widgets.button.date_button.DateButton

---

## DatePickerDialog

A `QDialog` containing a `QCalendarWidget` for date selection. Used internally by `DateButton` but also available as a standalone dialog.

**Constructor parameters:**

| Parameter      | Type              | Default | Description                       |
| -------------- | ----------------- | ------- | --------------------------------- |
| `parent`       | `QWidget \| None` | `None`  | Parent widget                     |
| `current_date` | `QDate \| None`   | `None`  | Date pre-selected in the calendar |

**Methods:**

| Method           | Returns         | Description                                                             |
| ---------------- | --------------- | ----------------------------------------------------------------------- |
| `selectedDate()` | `QDate \| None` | Returns the date clicked in the calendar, or `None` if none was clicked |

**Example:**

```python
from PySide6.QtCore import QDate
from ezqt_widgets import DatePickerDialog

dialog = DatePickerDialog(current_date=QDate.currentDate())
if dialog.exec():
    date = dialog.selectedDate()
    if date:
        print(date.toString("dd/MM/yyyy"))
```

::: ezqt_widgets.widgets.button.date_button.DatePickerDialog

---

## IconButton

A `QToolButton` that displays an icon from any supported source (file path, URL, SVG, `QIcon`, or `QPixmap`) with an optional text label.

**Signals:**

| Signal        | Signature | Emitted when           |
| ------------- | --------- | ---------------------- |
| `iconChanged` | `(QIcon)` | The icon is updated    |
| `textChanged` | `(str)`   | The text label changes |

**Constructor parameters:**

| Parameter      | Type                              | Default         | Description                                      |
| -------------- | --------------------------------- | --------------- | ------------------------------------------------ |
| `parent`       | `QWidget \| None`                 | `None`          | Parent widget                                    |
| `icon`         | `QIcon \| QPixmap \| str \| None` | `None`          | Icon source; supports local paths, URLs, and SVG |
| `text`         | `str`                             | `""`            | Button label text                                |
| `icon_size`    | `QSize \| tuple[int, int]`        | `QSize(20, 20)` | Icon display size                                |
| `text_visible` | `bool`                            | `True`          | Whether the text label is initially visible      |
| `spacing`      | `int`                             | `10`            | Pixels between the icon and the text             |
| `min_width`    | `int \| None`                     | `None`          | Minimum width; auto-calculated if `None`         |
| `min_height`   | `int \| None`                     | `None`          | Minimum height; auto-calculated if `None`        |

**Properties:**

| Property       | Type            | Description                                     |
| -------------- | --------------- | ----------------------------------------------- |
| `icon`         | `QIcon \| None` | Gets or sets the button icon                    |
| `text`         | `str`           | Gets or sets the button text                    |
| `icon_size`    | `QSize`         | Gets or sets the icon size                      |
| `text_visible` | `bool`          | Gets or sets text label visibility              |
| `spacing`      | `int`           | Gets or sets the icon-to-text spacing in pixels |
| `min_width`    | `int \| None`   | Gets or sets minimum width                      |
| `min_height`   | `int \| None`   | Gets or sets minimum height                     |

**Methods:**

| Method                   | Signature                              | Description                                                            |
| ------------------------ | -------------------------------------- | ---------------------------------------------------------------------- |
| `clearIcon()`            | `() -> None`                           | Removes the current icon and emits `iconChanged` with an empty `QIcon` |
| `clearText()`            | `() -> None`                           | Sets the text to an empty string                                       |
| `toggleTextVisibility()` | `() -> None`                           | Inverts `text_visible`                                                 |
| `setIconColor()`         | `(color: str, opacity: float) -> None` | Applies a color overlay to the current icon pixmap                     |
| `refreshStyle()`         | `() -> None`                           | Re-applies the QSS stylesheet after dynamic changes                    |

!!! note "URL icons"
When `icon` is an HTTP or HTTPS URL, the fetch is asynchronous. The icon
appears after the network response completes; no blocking occurs.

**Example:**

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import IconButton

app = QApplication([])

btn = IconButton(
    icon="https://img.icons8.com/?size=100&id=8329&format=png&color=000000",
    text="Open file",
    icon_size=(24, 24),
    text_visible=True,
)
btn.iconChanged.connect(lambda icon: print("icon updated"))
btn.show()

app.exec()
```

::: ezqt_widgets.widgets.button.icon_button.IconButton

---

## LoaderButton

A `QToolButton` that transitions between a normal state, an animated loading state, a success state, and an error state.

**Signals:**

| Signal            | Signature | Emitted when                                                            |
| ----------------- | --------- | ----------------------------------------------------------------------- |
| `loadingStarted`  | `()`      | `startLoading()` is called                                              |
| `loadingFinished` | `()`      | `stopLoading(success=True)` completes                                   |
| `loadingFailed`   | `(str)`   | `stopLoading(success=False)` completes; the string is the error message |

**Constructor parameters:**

| Parameter              | Type                              | Default        | Description                                               |
| ---------------------- | --------------------------------- | -------------- | --------------------------------------------------------- |
| `parent`               | `QWidget \| None`                 | `None`         | Parent widget                                             |
| `text`                 | `str`                             | `""`           | Label in the normal state                                 |
| `icon`                 | `QIcon \| QPixmap \| str \| None` | `None`         | Icon in the normal state                                  |
| `loading_text`         | `str`                             | `"Loading..."` | Label shown during loading                                |
| `loading_icon`         | `QIcon \| QPixmap \| str \| None` | `None`         | Icon during loading; auto-generated spinner if `None`     |
| `success_icon`         | `QIcon \| QPixmap \| str \| None` | `None`         | Icon shown on success; auto-generated checkmark if `None` |
| `error_icon`           | `QIcon \| QPixmap \| str \| None` | `None`         | Icon shown on error; auto-generated X if `None`           |
| `animation_speed`      | `int`                             | `100`          | Spinner frame interval in milliseconds                    |
| `auto_reset`           | `bool`                            | `True`         | Whether to return to the normal state after success/error |
| `success_display_time` | `int`                             | `1000`         | Milliseconds to show the success state before auto-reset  |
| `error_display_time`   | `int`                             | `2000`         | Milliseconds to show the error state before auto-reset    |
| `min_width`            | `int \| None`                     | `None`         | Minimum width; auto-calculated if `None`                  |
| `min_height`           | `int \| None`                     | `None`         | Minimum height; auto-calculated if `None`                 |

**Properties:**

| Property               | Type            | Description                                             |
| ---------------------- | --------------- | ------------------------------------------------------- |
| `text`                 | `str`           | Normal-state label                                      |
| `icon`                 | `QIcon \| None` | Normal-state icon                                       |
| `loading_text`         | `str`           | Text shown during loading                               |
| `loading_icon`         | `QIcon \| None` | Icon shown during loading                               |
| `success_icon`         | `QIcon \| None` | Icon shown on success                                   |
| `error_icon`           | `QIcon \| None` | Icon shown on error                                     |
| `is_loading`           | `bool`          | Read-only; `True` while loading animation is active     |
| `animation_speed`      | `int`           | Spinner frame interval in milliseconds                  |
| `auto_reset`           | `bool`          | Whether to auto-return to normal state after completion |
| `success_display_time` | `int`           | Milliseconds the success state is displayed             |
| `error_display_time`   | `int`           | Milliseconds the error state is displayed               |
| `min_width`            | `int \| None`   | Minimum width                                           |
| `min_height`           | `int \| None`   | Minimum height                                          |

**Methods:**

| Method           | Signature                                     | Description                                                          |
| ---------------- | --------------------------------------------- | -------------------------------------------------------------------- |
| `startLoading()` | `() -> None`                                  | Enters the loading state; disables the button and starts the spinner |
| `stopLoading()`  | `(success: bool, error_message: str) -> None` | Exits the loading state; shows success or error UI                   |
| `refreshStyle()` | `() -> None`                                  | Re-applies the QSS stylesheet after dynamic changes                  |

!!! note "Calling stopLoading while not loading"
`stopLoading()` is a no-op if `is_loading` is `False`.

**Example:**

```python
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from ezqt_widgets import LoaderButton

app = QApplication([])

btn = LoaderButton(
    text="Submit",
    loading_text="Sending...",
    auto_reset=True,
    success_display_time=1500,
)
btn.loadingFinished.connect(lambda: print("done"))

def simulate_request():
    btn.startLoading()
    QTimer.singleShot(2000, lambda: btn.stopLoading(success=True))

btn.clicked.connect(simulate_request)
btn.show()

app.exec()
```

::: ezqt_widgets.widgets.button.loader_button.LoaderButton
