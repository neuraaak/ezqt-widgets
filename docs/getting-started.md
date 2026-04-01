# Getting started with EzQt Widgets

By the end of this tutorial you will have `ezqt-widgets` installed and have run your first interactive widget.

## 🔧 Prerequisites

- Python >= 3.11 ([python.org](https://www.python.org/downloads/))
- Internet access to install from PyPI

## Step 1 — Install EzQt Widgets

```bash
pip install ezqt-widgets
```

You should see a line confirming the package was installed successfully. Verify:

```bash
python -c "import ezqt_widgets; print(ezqt_widgets.__version__)"
```

## Step 2 — Create your first widget

Create a file `hello.py` and run it:

```python
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from ezqt_widgets import IconButton, ToggleSwitch

app = QApplication([])

window = QWidget()
layout = QVBoxLayout(window)

btn = IconButton(text="Click me")
btn.clicked.connect(lambda: print("Button clicked!"))

switch = ToggleSwitch(checked=False)
switch.toggled.connect(lambda state: print(f"Toggle: {state}"))

layout.addWidget(btn)
layout.addWidget(switch)

window.setWindowTitle("EzQt Widgets — Hello World")
window.show()

app.exec()
```

You should see a window with an `IconButton` and a `ToggleSwitch`.

## Step 3 — Run the interactive demos

The CLI ships interactive demos for all widget categories.

```bash
# Run all demos with the GUI launcher
ezqt-widgets demo run --all

# Or run a single category
ezqt-widgets demo run --buttons
ezqt-widgets demo run --inputs
ezqt-widgets demo run --labels
ezqt-widgets demo run --misc
```

You should see a demo window showcasing each widget category.

## ✅ What you built

You installed `ezqt-widgets` from PyPI, created a minimal window combining an `IconButton` and a `ToggleSwitch`, and launched the built-in interactive demos.

## ➡️ Next steps

- [How to style widgets with QSS](guides/configuration.md)
- [API Reference](api/index.md)
- [Contributing — set up a dev environment](guides/development.md)
