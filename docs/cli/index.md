# CLI -- Command-Line Interface

Documentation for the **ezqt** command-line interface.

---

## Installation

```bash
# Install in development mode
pip install -e ".[dev]"

# Verify installation
ezqt --version
```

---

## Commands

### `ezqt run` -- Run Examples

Launch interactive examples to explore widgets.

```bash
ezqt run [OPTIONS]
```

| Option      | Short | Description                                                                            |
| ----------- | ----- | -------------------------------------------------------------------------------------- |
| `--all`     | `-a`  | Run all examples with the GUI launcher                                                 |
| `--buttons` | `-b`  | Button examples (DateButton, IconButton, LoaderButton)                                 |
| `--inputs`  | `-i`  | Input examples (AutoComplete, Search, TabReplace)                                      |
| `--labels`  | `-l`  | Label examples (ClickableTag, Framed, Hover, Indicator)                                |
| `--misc`    | `-m`  | Misc examples (CircularTimer, DraggableList, OptionSelector, ToggleIcon, ToggleSwitch) |
| `--no-gui`  |       | Sequential mode without GUI launcher                                                   |
| `--verbose` | `-v`  | Verbose output                                                                         |

**Examples:**

```bash
ezqt run --all
ezqt run --buttons --verbose
ezqt run --all --no-gui
```

---

### `ezqt list` -- List Examples

Displays all available example files and their status.

```bash
ezqt list
```

**Output:**

```text
Available examples:
========================================
button_example
input_example
label_example
misc_example
run_all_examples

Total: 5 examples found
```

---

### `ezqt test` -- Run Tests

Executes the project test suite.

```bash
ezqt test [OPTIONS]
```

| Option       | Short | Description         |
| ------------ | ----- | ------------------- |
| `--unit`     | `-u`  | Unit tests          |
| `--coverage` | `-c`  | Tests with coverage |
| `--verbose`  | `-v`  | Verbose output      |

**Examples:**

```bash
ezqt test --unit
ezqt test --coverage
ezqt test --unit --coverage --verbose
```

---

### `ezqt info` -- Package Information

Displays information about the ezqt_widgets installation.

```bash
ezqt info
```

**Output:**

```text
EzQt Widgets Information
========================================
Version: 2.3.2
Location: /path/to/ezqt_widgets/__init__.py
PySide6: 6.9.1
Examples: 5 found
========================================
```

---

## Use Cases

### For Developers

```bash
# Quick test during development
ezqt run --buttons --verbose

# Tests before commit
ezqt test --coverage

# Check package status
ezqt info
```

### For Users

```bash
# Explore all widgets
ezqt run --all

# Focus on a widget type
ezqt run --inputs

# See what's available
ezqt list
```

---

## Environment Variables

| Variable            | Description                           |
| ------------------- | ------------------------------------- |
| `EZQT_VERBOSE`      | Enable verbose mode by default        |
| `EZQT_EXAMPLES_DIR` | Custom path to the examples directory |

---

## Troubleshooting

| Issue              | Solution                                                |
| ------------------ | ------------------------------------------------------- |
| Command not found  | Install in dev mode: `pip install -e ".[dev]"`          |
| Examples not found | Check that the `examples/` directory exists at the root |
| Import errors      | Check PySide6: `pip install PySide6`                    |

---

## Resources

- [API Reference](../api/index.md) -- Widget documentation
- [Examples](../examples/index.md) -- Example code
- [QSS Style Guide](../guides/style-guide.md) -- Visual customization
