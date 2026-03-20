# Development Guide

Everything you need to set up the development environment, maintain code quality, and contribute a new widget to **ezqt-widgets**.

---

## Prerequisites

| Requirement | Version            |
| ----------- | ------------------ |
| Python      | >= 3.11            |
| PySide6     | >= 6.7.3, < 7.0.0  |
| Git         | any recent version |

---

## Environment Setup

```bash
# Clone the repository
git clone https://github.com/neuraaak/ezqt-widgets.git
cd ezqt-widgets

# Install in editable mode with all development extras
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

Or with Make:

```bash
make install-dev
make setup-hooks
```

Verify the CLI is available after installation:

```bash
ezqt-widgets info
```

---

## Project Structure

```text
ezqt_widgets/
├── src/
│   └── ezqt_widgets/
│       ├── __init__.py           # Public API — __all__ and re-exports
│       ├── version.py            # Single source of truth for __version__
│       ├── types.py              # Shared type aliases
│       ├── widgets/
│       │   ├── button/           # DateButton, IconButton, LoaderButton
│       │   ├── input/            # AutoCompleteInput, PasswordInput, SearchInput, TabReplaceTextEdit
│       │   ├── label/            # ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel
│       │   └── misc/             # CircularTimer, DraggableList, OptionSelector, ThemeIcon, ToggleIcon, ToggleSwitch
│       └── cli/
│           └── main.py           # Click entry point: ezqt-widgets
├── tests/
│   ├── conftest.py
│   ├── run_tests.py
│   └── unit/
│       ├── test_button/
│       ├── test_input/
│       ├── test_label/
│       └── test_misc/
├── examples/                     # Runnable example scripts
├── docs/                         # MkDocs documentation source
├── pyproject.toml
└── Makefile
```

---

## Make Commands

| Target             | What it does                                                |
| ------------------ | ----------------------------------------------------------- |
| `make help`        | List all available targets                                  |
| `make install`     | Install the package in editable mode                        |
| `make install-dev` | Install the package with all development extras             |
| `make format`      | Format source code with `ruff format`                       |
| `make fix`         | Alias for `make format`                                     |
| `make lint`        | Run `python lint.py` (Ruff + Bandit + import-linter)        |
| `make test`        | Run unit tests via `python tests/run_tests.py --type unit`  |
| `make test-cov`    | Run tests with HTML coverage report                         |
| `make test-fast`   | Run tests excluding slow-marked cases                       |
| `make check`       | Run `format` + `lint` + `test` in sequence                  |
| `make prepare`     | Run `format` + `lint` + `test-fast` — use before committing |
| `make setup-hooks` | Install pre-commit hooks                                    |
| `make pre-commit`  | Run all pre-commit hooks against every file                 |
| `make docs`        | Start the MkDocs dev server with live reload                |
| `make docs-build`  | Build the static site (`mkdocs build --strict`)             |
| `make docs-deploy` | Deploy to GitHub Pages (`mkdocs gh-deploy --force`)         |
| `make clean`       | Remove `__pycache__`, `*.pyc`, `dist/`, `htmlcov/`, etc.    |

---

## Code Standards

### File Structure

Every widget module follows this internal section order:

```python
# ///////////////////////////////////////////////////////////////
# SECTION NAME
# ///////////////////////////////////////////////////////////////
```

Mandatory sections, in order:

1. Module docstring
2. `from __future__ import annotations`
3. Standard library imports
4. Third-party imports (PySide6)
5. Local imports
6. `__all__` declaration
7. Class definition

### Naming Conventions

| Element        | Convention      | Example          |
| -------------- | --------------- | ---------------- |
| Module file    | `snake_case.py` | `date_button.py` |
| Class          | `PascalCase`    | `DateButton`     |
| Public method  | `camelCase`     | `startLoading()` |
| Private method | `_snake_case`   | `_apply_style()` |
| Signal         | `camelCase`     | `dateChanged`    |
| Qt Property    | `snake_case`    | `date_format`    |

### Type Hints

All public methods and constructors require type hints. Use the shared type aliases from `ezqt_widgets.types` where applicable:

```python
from ezqt_widgets.types import IconSource, SizeType, WidgetParent
```

Use native generics (`list[str]`, `dict[str, str]`) with `from __future__ import annotations` rather than `typing.List` or `typing.Dict`.

### Docstrings

Google-style docstrings are required for all public classes and methods. Mandatory sections for non-trivial methods:

```python
def setStatus(self, status: str) -> None:
    """Set the current status and update the display.

    Args:
        status: Key from the ``status_map`` passed at construction.

    Raises:
        ValueError: If ``status`` is not a key in ``status_map``.
    """
```

Rules:

- First line: one complete sentence ending with a period
- `Args`: document every non-obvious parameter
- `Returns`: always document non-trivial return values
- `Raises`: document only exceptions the caller is expected to handle
- Internal helper methods: one-line docstring is sufficient

---

## Adding a New Widget

Follow this checklist in order. Every step is required before a PR can be merged.

### 1. Choose the right category

| Category  | When to use                                                               |
| --------- | ------------------------------------------------------------------------- |
| `button/` | Inherits from `QAbstractButton`, `QToolButton`, or `QPushButton`          |
| `input/`  | Inherits from `QLineEdit`, `QPlainTextEdit`, or a composite input wrapper |
| `label/`  | Inherits from `QLabel` or `QFrame` used as a display element              |
| `misc/`   | Everything else — timers, selectors, icons, toggles                       |

### 2. Create the module file

Create `src/ezqt_widgets/widgets/<category>/<widget_name>.py`.

Minimal required content:

```python
# ///////////////////////////////////////////////////////////////
# <WIDGET NAME>
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
<WidgetClass> — one-sentence description.
"""

from __future__ import annotations

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Property

from ezqt_widgets.types import WidgetParent

__all__ = ["<WidgetClass>"]


class <WidgetClass>(QWidget):
    """<One-sentence description ending with a period>.

    Args:
        parent: Parent widget.
    """

    # Signals
    # Properties
    # Constructor
    # Public methods
    # Private methods
    # Qt event overrides
```

### 3. Register in the category `__init__.py`

Add the import and `__all__` entry to `src/ezqt_widgets/widgets/<category>/__init__.py`:

```python
from .<widget_name> import <WidgetClass>

__all__ = [
    ...,
    "<WidgetClass>",
]
```

### 4. Register in the top-level `__init__.py`

Add the class to `src/ezqt_widgets/__init__.py`:

```python
from .widgets.<category> import <WidgetClass>

__all__ = [
    ...,
    "<WidgetClass>",
]
```

### 5. Write unit tests

Create `tests/unit/test_<category>/test_<widget_name>.py`. Required test cases:

- Constructor with default parameters
- Constructor with all explicit parameters
- Each public method (happy path)
- Each signal emission
- Each error condition (wrong type, out-of-range value, etc.)

Test name convention: `test_should_<expected_behavior>_when_<condition>`.

### 6. Write an example script

Add or extend `examples/<category>_example.py` with a self-contained, runnable demonstration of the widget. The script must not rely on implicit state.

### 7. Document the widget

Add the widget to `docs/api/<category>.md`:

- Signal table
- Constructor parameter table
- Property table
- Method table
- Self-contained code example
- `:::` mkdocstrings directive

Add the class name to `docs/api/index.md`.

### 8. Run the full quality check

```bash
make check
```

All steps must pass: format, lint, and test with coverage above the 60% threshold.

---

## Quality Workflow

### Formatting

Ruff handles both formatting and import sorting:

```bash
# Format all source and test files
make format

# Equivalent direct command
ruff format src/ezqt_widgets tests
```

### Linting

```bash
# Run the full lint suite (Ruff lint + Bandit security + import-linter)
make lint

# Auto-fix safe issues
make fix
```

Ruff is configured in `pyproject.toml` with the following active rule sets: `E`, `W`, `F` (pyflakes), `I` (import order), `B` (bugbear), `C4`, `UP`, `S` (bandit), `T20`, `ARG`, `PIE`, `SIM`.

### Security scanning

Bandit is invoked by `python lint.py`. It scans `src/ezqt_widgets/` and excludes `tests/`, `docs/`, and `examples/`. Skipped rules: `B101` (assert), `B601`.

### Type checking

Two type checkers are configured:

```bash
# ty (fast, minimal)
ty check src/

# pyright (comprehensive)
pyright src/ezqt_widgets
```

Both are invoked by `python lint.py`. Target version for both is Python 3.11.

### Import contracts

`import-linter` enforces the layer dependency flow:

```text
ezqt_widgets.cli → ezqt_widgets.widgets → ezqt_widgets.utils
```

Upper layers may import from lower layers, but not the reverse.

### Pre-commit hooks

Hooks run automatically before each commit. To run them manually:

```bash
make pre-commit
```

Hooks include: Ruff format, Ruff lint, type checking, and standard file hygiene (trailing whitespace, end-of-file newline).

---

## Testing

### Running Tests

```bash
# Unit tests only
make test

# Unit tests with HTML coverage report
make test-cov

# Fast subset (excludes slow-marked tests)
make test-fast

# Target a single category
pytest tests/unit/test_button/ -v

# Run via the CLI
ezqt-widgets test --unit
ezqt-widgets test --coverage
```

### Coverage Threshold

Pytest is configured to fail if coverage drops below **60%**. The HTML report is written to `htmlcov/`. The following modules are excluded from coverage measurement: `cli/main.py` and `cli/runner.py` (not unit-testable without a running Qt application).

### Test Markers

| Marker        | Description                             |
| ------------- | --------------------------------------- |
| `unit`        | Standard unit test (default)            |
| `slow`        | Long-running test; excluded by `--fast` |
| `integration` | Requires running Qt event loop          |
| `robustness`  | Edge cases and error conditions         |
| `cli`         | Tests for CLI commands                  |

---

## Troubleshooting

| Issue                             | Solution                                                                           |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| `ezqt-widgets: command not found` | Run `pip install -e ".[dev]"` from the repo root                                   |
| `ImportError: PySide6`            | Run `pip install "PySide6>=6.7.3"`                                                 |
| `ruff: command not found`         | Ruff is installed via `.[dev]`; verify with `ruff --version`                       |
| Pre-commit hooks not running      | Run `pre-commit install` or `make setup-hooks`                                     |
| Tests fail at import              | Ensure the package is installed with `pip install -e .` so `src/` is on `sys.path` |
| Coverage below 60%                | Add missing test cases; run `make test-cov` to see the HTML report in `htmlcov/`   |

---

## Resources

- [API Reference](../api/index.md) — Complete widget documentation
- [Examples](../examples/index.md) — Runnable usage examples
- [CLI Reference](../cli/index.md) — `ezqt-widgets` command reference
