# Development Guide

Complete guide for setting up the development environment, using tools
and contributing to the **ezqt_widgets** project.

---

## Prerequisites

- **Python**: 3.10 or higher
- **PySide6**: 6.x
- **Git**: for version control

## Quick Setup

```bash
# Install in development mode
pip install -e ".[dev]"

# Or with Make
make install-dev
```

---

## Development Tools

### Code Formatting

#### VSCode (recommended)

The project includes a VSCode configuration that enables:

- **Auto-format on save** with Ruff
- **Automatic import sorting** with Ruff
- **Real-time linting** with Ruff
- **Test discovery** with pytest

#### Recommended VSCode Extensions

- `ms-python.python` -- Full Python support
- `charliermarsh.ruff` -- Ruff formatter and linter
- `ms-python.mypy-type-checker` -- Type checking

### Development Commands

#### With Make

```bash
make help           # Display help
make format         # Format code (Black + isort)
make lint           # Check code quality
make fix            # Auto-fix issues
make test           # Run tests
make test-cov       # Tests with coverage
make clean          # Clean temporary files
```

#### Native Python Scripts

```bash
# Linting and formatting
python .scripts/dev/lint.py              # Check quality
python .scripts/dev/lint.py --fix        # Auto-fix

# Tests
python tests/run_tests.py --type unit    # Unit tests
python tests/run_tests.py --coverage     # With coverage
python tests/run_tests.py --fast         # Fast tests
```

---

## Code Standards

### Ruff Configuration

- **Line length**: 88 characters
- **Python versions**: 3.10, 3.11, 3.12
- **Format on save**: enabled

### Type Hints

- **Required** for all public functions and methods
- **Style**: native types (`list`, `dict`) with `from __future__ import annotations`

### Docstrings

- **Format**: Google-style
- **Language**: English
- **Required** for all public classes, methods and functions

### Section Markers

```python
# ///////////////////////////////////////////////////////////////
# SECTION NAME
# ///////////////////////////////////////////////////////////////
```

---

## Pre-commit Hooks

### Installation

```bash
pip install pre-commit
pre-commit install
```

### Automatic Checks

Hooks run before each commit:

- Formatting with Ruff
- Import sorting
- Linting with Ruff
- Type checking
- Cleanup (trailing whitespace, etc.)

---

## Tests

### Test Structure

```text
tests/
├── conftest.py                 # pytest configuration
├── run_tests.py                # Execution script
└── unit/                       # Unit tests
    ├── test_button/
    ├── test_input/
    ├── test_label/
    └── test_misc/
```

### Running Tests

```bash
# Fast tests
python tests/run_tests.py --type unit --fast

# Full tests with coverage
python tests/run_tests.py --coverage

# Specific tests
pytest tests/unit/test_button/ -v
```

---

## Built-in CLI

The project includes a CLI accessible via `ezqt`:

```bash
# Package information
ezqt info

# Run examples
ezqt run --all
ezqt run --buttons
ezqt run --inputs

# Tests from CLI
ezqt test --unit
ezqt test --coverage
```

---

## Recommended Workflow

### 1. Before Starting

```bash
pip install -e ".[dev]"
pre-commit install
```

### 2. During Development

- **VSCode** auto-formats on save
- **Or manually**: `make format`
- **Quick tests**: `make test`

### 3. Before Committing

```bash
# Full check
make check        # format + lint + test

# Or step by step
make format       # Format
make lint         # Check
make test         # Test
```

### 4. Pre-commit hooks run automatically

---

## Troubleshooting

### Common Issues

| Issue               | Solution                                            |
| ------------------- | --------------------------------------------------- |
| Ruff not formatting | Check: `ruff --version`                             |
| Tests failing       | Check PySide6: `python -c "import PySide6"`         |
| Pre-commit hooks    | Reinstall: `pre-commit clean && pre-commit install` |

---

## Project Structure

```text
ezqt_widgets/
├── ezqt_widgets/         # Source code
│   ├── button/           # Button widgets
│   ├── input/            # Input widgets
│   ├── label/            # Label widgets
│   ├── misc/             # Utility widgets
│   └── cli/              # CLI interface
├── examples/             # Usage examples
├── tests/                # Test suite
├── pyproject.toml        # Project configuration
└── Makefile              # Make commands
```

---

## Resources

- [API Reference](../api/index.md) -- Complete widget documentation
- [Examples](../examples/index.md) -- Usage examples
- [QSS Style Guide](style-guide.md) -- Visual customization
- [CLI](../cli/index.md) -- Command-line interface
