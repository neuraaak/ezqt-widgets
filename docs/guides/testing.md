# How to run and write tests

Run the test suite and add tests for new behaviour in `ezqt-widgets`.

## 🔧 Prerequisites

- Development environment set up ([How to set up a dev environment](development.md))

## 🧪 Run the full test suite

```bash
uv run pytest
```

You should see a summary showing all tests passed.

## 📊 Run with coverage

```bash
uv run pytest --cov=src/ --cov-report=term-missing
```

## ✏️ Write a new test

1. Create a test file in `tests/` following the naming convention `test_<module>.py`.

2. Write your test using `pytest` conventions.

   ```python
   from PySide6.QtWidgets import QApplication
   from ezqt_widgets import IconButton

   def test_icon_button_default_text():
       app = QApplication.instance() or QApplication([])
       btn = IconButton(text="Hello")
       assert btn is not None
   ```

3. Run the test in isolation to verify it passes.

   ```bash
   uv run pytest tests/test_<module>.py -v
   ```

## ✅ Result

All tests pass and coverage remains above the configured threshold.
