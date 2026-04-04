# How to style widgets with QSS

Apply custom Qt Style Sheet (QSS) rules to `ezqt-widgets` widgets.

## 🔧 Prerequisites

- `ezqt-widgets` installed:

    === "uv"

        ```bash
        uv add ezqt-widgets
        ```

    === "pip"

        ```bash
        pip install ezqt-widgets
        ```

- Basic familiarity with [Qt Style Sheets](https://doc.qt.io/qt-6/stylesheet.html)

## 📝 Steps

1. Apply a global stylesheet to the `QApplication` instance.

   ```python
   from PySide6.QtWidgets import QApplication
   from ezqt_widgets import SearchInput

   app = QApplication([])
   app.setStyleSheet("""
       SearchInput {
           background-color: #2d2d2d;
           border: 1px solid #444444;
           border-radius: 4px;
       }
       SearchInput:focus {
           border: 1px solid #0078d4;
       }
   """)

   widget = SearchInput()
   widget.show()
   app.exec()
   ```

2. Call `refreshStyle()` after changing a widget's stylesheet at runtime to force a re-paint.

   ```python
   widget.setStyleSheet("border: 2px solid #ff0000;")
   widget.refreshStyle()
   ```

## 🗂️ QSS selectors per widget category

| Widget class         | QSS selector         |
| -------------------- | -------------------- |
| `AutoCompleteInput`  | `AutoCompleteInput`  |
| `SearchInput`        | `SearchInput`        |
| `PasswordInput`      | `PasswordInput`      |
| `TabReplaceTextEdit` | `TabReplaceTextEdit` |
| `FilePickerInput`    | `FilePickerInput`    |
| `SpinBoxInput`       | `SpinBoxInput`       |
| `ClickableTagLabel`  | `ClickableTagLabel`  |
| `FramedLabel`        | `FramedLabel`        |
| `HoverLabel`         | `HoverLabel`         |
| `IndicatorLabel`     | `IndicatorLabel`     |
| `DateButton`         | `DateButton`         |
| `IconButton`         | `IconButton`         |
| `LoaderButton`       | `LoaderButton`       |
| `ToggleSwitch`       | `ToggleSwitch`       |

For complete per-widget CSS examples, see the [QSS Style Guide](style-guide.md).

## ✅ Result

Your widgets now render with the custom stylesheet applied.

## ➡️ Next steps

- [QSS Style Guide](style-guide.md)
- [API Reference](../api/index.md)
