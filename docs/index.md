# EzQt Widgets

[![PyPI version](https://img.shields.io/pypi/v/ezqt-widgets?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezqt-widgets?style=flat&logo=python&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![PyPI status](https://img.shields.io/pypi/status/ezqt-widgets?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezqt-widgets/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat&logo=github&logoColor=white)](https://github.com/neuraaak/ezqt-widgets/blob/main/LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/neuraaak/ezqt-widgets/publish-pypi.yml?style=flat&label=publish&logo=githubactions&logoColor=white)](https://github.com/neuraaak/ezqt-widgets/actions/workflows/publish-pypi.yml)
[![Docs](https://img.shields.io/badge/docs-Github%20Pages-blue?style=flat&logo=materialformkdocs&logoColor=white)](https://neuraaak.github.io/ezqt-widgets/)
[![uv](https://img.shields.io/badge/package%20manager-uv-DE5FE9?style=flat&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![linter](https://img.shields.io/badge/linter-ruff-orange?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![type checker](https://img.shields.io/badge/type%20checker-ty-orange?style=flat&logo=astral&logoColor=white)](https://github.com/astral-sh/ty)

**EzQt Widgets** — A collection of custom and reusable Qt widgets for PySide6. Provides advanced, styled graphical components to accelerate the development of modern desktop interfaces.

## 🚀 Quick start

Install from PyPI and run your first widget in under five minutes.

=== "uv"

    ```bash
    uv add ezqt-widgets
    ```

=== "pip"

    ```bash
    pip install ezqt-widgets
    ```

```python
from PySide6.QtWidgets import QApplication
from ezqt_widgets import IconButton, ToggleSwitch

app = QApplication([])

btn = IconButton(text="Hello EzQt")
btn.show()

app.exec()
```

## ✨ Key features

- **Button widgets** — date picker, icon buttons with URL/local/SVG support, loading state buttons
- **Input widgets** — auto-complete, password field with strength bar, search with history, tab-sanitized text editor, file picker, spin box
- **Label widgets** — clickable tag labels, framed labels, hover-icon labels, LED status indicators
- **Misc widgets** — animated circular timer, drag-and-drop list, option selector, theme-aware icon, toggle icon, modern toggle switch, notification banner, collapsible section
- Fully typed public API (`py.typed` compliant)
- PySide6 ≥ 6.7.3 compatible

## 📚 Documentation

| Section                               | Description                                                      |
| ------------------------------------- | ---------------------------------------------------------------- |
| [Getting Started](getting-started.md) | Install, first steps, and quickstart in under 5 minutes          |
| [User Guides](guides/index.md)        | Task-oriented guides for configuration, development, and testing |
| [Concepts](concepts/index.md)         | Design rationale and architectural background                    |
| [API Reference](api/index.md)         | Complete class and method reference generated from source        |
| [CLI Reference](cli/index.md)         | Command-line interface usage and options                         |
| [Examples](examples/index.md)         | Runnable end-to-end examples by widget category                  |
| [Architecture](architecture.md)       | Layer dependency graph generated from the source tree            |
| [Coverage](coverage.md)               | Test coverage report                                             |
| [Changelog](changelog.md)             | Version history and release notes                                |

## 📋 Requirements

- Python >= 3.11
- PySide6 >= 6.7.3

## ⚖️ License

[MIT](https://github.com/neuraaak/ezqt-widgets/blob/main/LICENSE)
