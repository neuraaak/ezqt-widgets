# CLI Reference

Documentation for the `ezqt-widgets` command-line interface.

The CLI is registered as the `ezqt-widgets` entry point in `pyproject.toml`:

```toml
[project.scripts]
ezqt-widgets = "ezqt_widgets.cli.main:cli"
```

---

## Installation

```bash
# Standard installation
pip install ezqt-widgets

# Development installation (includes all dev extras)
pip install -e ".[dev]"

# Verify the command is available
ezqt-widgets --version
```

---

## Commands

### `ezqt-widgets run` — Run examples

Launch interactive examples to explore widget functionality.

```bash
ezqt-widgets run [OPTIONS]
```

| Option      | Short | Description                                                                                |
| ----------- | ----- | ------------------------------------------------------------------------------------------ |
| `--all`     | `-a`  | Run all examples with the GUI launcher                                                     |
| `--buttons` | `-b`  | Run button examples (DateButton, IconButton, LoaderButton)                                 |
| `--inputs`  | `-i`  | Run input examples (AutoCompleteInput, PasswordInput, SearchInput, TabReplaceTextEdit)     |
| `--labels`  | `-l`  | Run label examples (ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel)            |
| `--misc`    | `-m`  | Run misc examples (CircularTimer, DraggableList, OptionSelector, ToggleIcon, ToggleSwitch) |
| `--no-gui`  | —     | Run examples sequentially without the GUI launcher                                         |
| `--verbose` | `-v`  | Verbose output                                                                             |

At least one category flag must be provided. Running `ezqt-widgets run` with no options prints usage information.

**Examples:**

```bash
ezqt-widgets run --all
ezqt-widgets run --buttons --verbose
ezqt-widgets run --all --no-gui
ezqt-widgets run --inputs --misc
```

---

### `ezqt-widgets list` — List available examples

Displays all available example files and their status.

```bash
ezqt-widgets list
```

**Sample output:**

```text
Available examples:
========================================
button_example
input_example
label_example
misc_example
run_all_examples
types_example

Total: 6 examples found
```

---

### `ezqt-widgets test` — Run the test suite

Executes the project test suite via pytest.

```bash
ezqt-widgets test [OPTIONS]
```

| Option       | Short | Description                         |
| ------------ | ----- | ----------------------------------- |
| `--unit`     | `-u`  | Run unit tests (`tests/unit/`)      |
| `--coverage` | `-c`  | Run tests with HTML coverage report |
| `--verbose`  | `-v`  | Verbose pytest output               |

When no option is given, `--unit` is assumed.

**Examples:**

```bash
ezqt-widgets test --unit
ezqt-widgets test --coverage
ezqt-widgets test --unit --verbose
```

---

### `ezqt-widgets docs` — Documentation utilities

Serves the built documentation locally.

```bash
ezqt-widgets docs [OPTIONS]
```

| Option    | Short | Default | Description                           |
| --------- | ----- | ------- | ------------------------------------- |
| `--serve` | `-s`  | —       | Serve the `docs/` directory over HTTP |
| `--port`  | `-p`  | `8000`  | Port for the local HTTP server        |

!!! note
`ezqt-widgets docs --serve` uses Python's built-in `http.server` to serve the
static `docs/` directory, not the MkDocs development server. For live-reload
during documentation development, use `mkdocs serve` directly.

**Examples:**

```bash
ezqt-widgets docs --serve
ezqt-widgets docs --serve --port 8080
```

---

### `ezqt-widgets info` — Package information

Displays information about the installed package.

```bash
ezqt-widgets info
```

**Sample output:**

```text
EzQt Widgets Information
========================================
Version: 2.6.0
Location: /path/to/site-packages/ezqt_widgets/__init__.py
PySide6: 6.7.3
Examples: 6 found
========================================
```

---

## Common Workflows

### Exploring widgets

```bash
# See what is available
ezqt-widgets list

# Try everything at once
ezqt-widgets run --all

# Focus on a specific category
ezqt-widgets run --buttons
ezqt-widgets run --inputs
```

### Development workflow

```bash
# Run tests before committing
ezqt-widgets test --unit

# Check coverage
ezqt-widgets test --coverage

# Verify the package is correctly installed
ezqt-widgets info
```

---

## Troubleshooting

| Issue                             | Solution                                                             |
| --------------------------------- | -------------------------------------------------------------------- |
| `ezqt-widgets: command not found` | Install with `pip install ezqt-widgets` or `pip install -e ".[dev]"` |
| Examples not found                | Ensure the `examples/` directory exists at the repository root       |
| `ImportError: PySide6`            | Install PySide6: `pip install "PySide6>=6.7.3"`                      |
| Tests not found                   | Run from the repository root; pytest expects the `tests/` directory  |
