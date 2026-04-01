# CLI reference

One-line description of the top-level `ezqt-widgets` command.

The CLI is registered as the `ezqt-widgets` entry point in `pyproject.toml`:

```toml
[project.scripts]
ezqt-widgets = "ezqt_widgets.cli.main:cli"
```

## 💻 Usage

```bash
ezqt-widgets [OPTIONS] COMMAND [ARGS]...
```

## ⚙️ Global options

| Option      | Short | Description               |
| ----------- | ----- | ------------------------- |
| `--version` | `-v`  | Show the version and exit |
| `--help`    | `-h`  | Show help and exit        |

## 📋 Commands

| Command   | Description                                          |
| --------- | ---------------------------------------------------- |
| `demo`    | Run and list interactive widget demos                |
| `docs`    | Open the online documentation in the default browser |
| `info`    | Display package information                          |
| `version` | Display version information                          |

---

## 🖥️ `ezqt-widgets demo` — Widget demos

The `demo` command group exposes two subcommands: `run` and `list`.

### `demo run` — Run widget examples

```bash
ezqt-widgets demo run [OPTIONS]
```

| Option      | Short | Description                                                                                    |
| ----------- | ----- | ---------------------------------------------------------------------------------------------- |
| `--all`     | `-a`  | Run all examples with the GUI launcher                                                         |
| `--buttons` | `-b`  | Run button examples (`DateButton`, `IconButton`, `LoaderButton`)                               |
| `--inputs`  | `-i`  | Run input examples (`AutoCompleteInput`, `PasswordInput`, `SearchInput`, `TabReplaceTextEdit`) |
| `--labels`  | `-l`  | Run label examples (`ClickableTagLabel`, `FramedLabel`, `HoverLabel`, `IndicatorLabel`)        |
| `--misc`    | `-m`  | Run misc examples (`CircularTimer`, `DraggableList`, `OptionSelector`, `ToggleSwitch`)         |
| `--no-gui`  | —     | Run examples sequentially without the GUI launcher                                             |
| `--verbose` | `-v`  | Verbose output                                                                                 |

At least one category flag must be provided. Running `ezqt-widgets demo run` with no options prints usage information.

### `demo list` — List available examples

```bash
ezqt-widgets demo list
```

Displays all available example scripts and their status.

**Sample output:**

```text
📋 Available examples:
========================================
✅ _button
✅ _input
✅ _label
✅ _misc
✅ run_all_examples

Total: 5 examples found
```

---

## 📖 `ezqt-widgets docs` — Open documentation

Opens the online documentation website in the default browser.

```bash
ezqt-widgets docs
```

If a browser cannot be opened (e.g. in a headless environment), the documentation URL is printed to stdout instead.

---

## ℹ️ `ezqt-widgets info` — Package information

Displays information about the installed package.

```bash
ezqt-widgets info
```

**Sample output:**

```text
Package Information
==================================================

Version: 2.7.0
Author:  Neuraaak
URL:     https://github.com/neuraaak/ezqt-widgets
Path:    /path/to/site-packages/ezqt_widgets
Examples: 5 found
```

---

## 🔢 `ezqt-widgets version` — Version information

```bash
ezqt-widgets version [OPTIONS]
```

| Option   | Short | Description                      |
| -------- | ----- | -------------------------------- |
| `--full` | `-f`  | Display full version information |

---

## 🧪 Examples

```bash
# Show installed version
ezqt-widgets --version

# Run all demos at once
ezqt-widgets demo run --all

# Run only button demos with verbose output
ezqt-widgets demo run --buttons --verbose

# Run multiple categories
ezqt-widgets demo run --inputs --misc

# List available demos
ezqt-widgets demo list

# Open online docs
ezqt-widgets docs

# Show package info
ezqt-widgets info

# Show full version details
ezqt-widgets version --full
```

---

## Troubleshooting

| Issue                             | Solution                                                             |
| --------------------------------- | -------------------------------------------------------------------- |
| `ezqt-widgets: command not found` | Install with `pip install ezqt-widgets` or `pip install -e ".[dev]"` |
| Examples not found                | Ensure the `examples/` directory exists at the repository root       |
| `ImportError: PySide6`            | Install PySide6: `pip install "PySide6>=6.7.3"`                      |
