# About the architecture

High-level overview of how `ezqt-widgets` is structured and why it was built that way.

## 🏗️ Module structure

`ezqt-widgets` is organised into four public widget sub-packages and a shared constants module:

```txt
ezqt_widgets/
├── widgets/
│   ├── button/   # DateButton, IconButton, LoaderButton, DatePickerDialog
│   ├── input/    # AutoCompleteInput, FilePickerInput, PasswordInput,
│   │             # SearchInput, SpinBoxInput, TabReplaceTextEdit
│   ├── label/    # ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel
│   ├── misc/     # CircularTimer, CollapsibleSection, DraggableList,
│   │             # NotificationBanner, OptionSelector, ThemeIcon,
│   │             # ToggleIcon, ToggleSwitch
│   └── shared/   # Animation constants, icon sizes, SVG bytes
├── types.py      # Public type aliases (IconSource, SizeType, etc.)
├── cli/          # Click-based CLI (demo, docs, info, version)
└── utils/        # Internal utilities (URL fetching)
```

All public symbols are re-exported from the top-level `ezqt_widgets` namespace:

```python
from ezqt_widgets import DateButton, ToggleSwitch, SearchInput
```

This flat re-export means consumers never need to know the internal sub-package layout.
The internal hierarchy exists for maintainability, not to create distinct namespaces.

## 🎨 Design reasoning

The library is built around five principles that informed every structural decision.

**Widget independence.**
Each widget is a self-contained unit with no runtime dependency on any other *domain* widget —
with one deliberate exception: `ThemeIcon`.

All widgets that expose an icon (`IconButton`, `ToggleIcon`, `LoaderButton`, `SearchInput`, …) use `ThemeIcon`
as their shared icon primitive. This is intentional: `ThemeIcon` acts as a synchronisation point with
[`ezqt-app`](https://github.com/Neuraaak/ezqt-app), a companion library that manages application-wide theming.
When `ezqt-app` switches theme, every icon rendered through `ThemeIcon` updates automatically, regardless of
which widget hosts it.

The independence guarantee therefore holds at the *domain-widget* level (a `ToggleSwitch` never imports a
`DateButton`), but `ThemeIcon` is a shared infrastructure widget, not a domain widget.
This distinction eliminates cascading breakage between functional widgets while still enabling coherent
icon theming across the whole widget set.

**Qt-native patterns.**
Widgets use `QProperty`, `Signal/Slot`, and `QPropertyAnimation` rather than custom event loops or timers.
Using Qt's own primitives means widgets compose naturally with any PySide6 application and respond correctly
to the Qt event model — pause, resume, and destroy behave as expected.

**Typed API.**
All public constructors and methods carry type annotations, and the package ships `py.typed`.
Type safety was prioritised because desktop GUI code tends to evolve slowly with infrequent test runs;
a type checker catches parameter mistakes that might otherwise surface only at runtime.

**QSS compatibility.**
Every widget exposes a `refreshStyle()` method and responds to `setStyleSheet()`.
Qt's style system is powerful but fragile: dynamic property changes require re-polishing to take effect.
The `refreshStyle()` contract makes this explicit and repeatable without each consumer needing to remember
to call `style().unpolish()` / `style().polish()`.

**Shared constants.**
Animation durations and icon sizes are centralised in `widgets.shared._defaults`.
Visual consistency across unrelated widgets (e.g. the loading spinner in `LoaderButton` and the
toggle animation in `ToggleSwitch`) depends on using the same timing values.
Centralisation prevents drift when tuning feel.

## 🔌 CLI architecture

The CLI layer is entirely separate from the widget layer.
It uses [Click](https://click.palletsprojects.com/) for command declaration and
[Rich](https://rich.readthedocs.io/) for formatted terminal output.

The entry point is registered in `pyproject.toml`:

```toml
[project.scripts]
ezqt-widgets = "ezqt_widgets.cli.main:cli"
```

The CLI exposes four commands: `demo` (a group with `run` and `list` subcommands), `docs`, `info`, and `version`.
The `demo` commands start the example scripts under `examples/` in a subprocess,
keeping the CLI layer decoupled from the widget code at runtime.

## ⚖️ Dependency choices

| Dependency          | Reason                                                                           |
| ------------------- | -------------------------------------------------------------------------------- |
| `PySide6`           | Official LGPL Qt binding for Python; preferred over PyQt for licence flexibility |
| `click`             | Declarative CLI; composable with groups and subcommands                          |
| `rich`              | Rich terminal output without extra configuration                                 |
| `PyYAML`            | Future-proof configuration loading                                               |
| `typing_extensions` | Backports newer typing constructs to Python 3.11                                 |

## 🔗 Relationship to the auto-generated architecture graph

The [Architecture](../architecture.md) page provides an import dependency graph generated by
[grimp](https://github.com/seddonym/grimp) at build time.
That graph reflects the actual import relationships in the source tree.
The narrative above explains the *intent* behind those relationships;
the graph shows whether the codebase honours that intent.
