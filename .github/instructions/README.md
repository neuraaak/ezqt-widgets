# Project Instructions & AI Orchestration

<rules>
- **AGENT DIRECTIVE:** Before any action, you MUST load `core/MANIFEST.md` and `languages/python/MANIFEST.md`.
- **PRECEDENCE:** Project-specific overrides in this README take precedence over all modular UIAs.
- **DECISION:** Adhere to the "Watchguard" architectural choice documented below.
</rules>

## Project Identity

- **Name:** `ezqt-widgets`
- **License:** MIT
- **Core Stack:** Python 3.11+, PySide6 >= 6.7.3, uv, Ruff, Hatchling (PEP 517), pytest
- **Environment:** Production-first, Windows 11 dev, corporate network (proxy-aware)

## Architectural Decision (Watchguard)

> **Decision:** Simple Layered Architecture
> **Rationale:** (Reference `core/core-decision-framework.instructions.md`)
>
> - [x] No non-trivial domain logic — this is a UI widget library.
> - [x] Single entry point: `src/ezqt_widgets/`.
> - [x] Non-volatile infrastructure — PySide6 is pinned and not subject to swap.

Hexagonal Architecture does NOT apply here. There are no ports, adapters, or domain isolation layers. Widgets are organized by functional family, not by technical pattern.

## Instruction Index (Modular UIAs)

| Category   | Manifest Path                    | Description                                       |
| :--------- | :------------------------------- | :------------------------------------------------ |
| **Core**   | `./core/MANIFEST.md`             | Reasoning, Git, Security, Ops, and Collaboration. |
| **Python** | `./languages/python/MANIFEST.md` | uv, Ruff, Hatchling, 3.11+ Standards.             |

## Architecture Overview

```text
src/ezqt_widgets/
├── __init__.py          # Top-level re-exports; __all__ mandatory
├── _version.py          # Single source of truth for version
├── types.py             # Shared type aliases and Protocols
├── widgets/
│   ├── button/          # DateButton, IconButton, LoaderButton
│   ├── input/           # AutoCompleteInput, PasswordInput, SearchInput, TabReplaceTextEdit
│   ├── label/           # ClickableTagLabel, FramedLabel, HoverLabel, IndicatorLabel
│   ├── misc/            # CircularTimer, DraggableList, OptionSelector, ThemeIcon, ToggleSwitch, ...
│   └── shared/          # Cross-widget utilities (internal)
├── utils/               # network_utils.py (proxy-aware helpers)
└── cli/                 # Click CLI entry point

tests/unit/              # Mirrors src/ezqt_widgets/ structure exactly
```

**Core principles:**

1. One file = one widget (exception: `DraggableItem` cohabits with `DraggableList`).
2. Widgets are grouped by functional family (`button/`, `input/`, `label/`, `misc/`), not by technical pattern.
3. All public symbols are re-exported via `__init__.py`; top-level import `from ezqt_widgets import ToggleSwitch` must always work.
4. `__all__` is mandatory in every `__init__.py`.
5. Test structure mirrors `src/` exactly: `tests/unit/test_<family>/test_<widget>.py`.

## Project-Specific Overrides

These rules differ from the global UIAs and take precedence within this project.

**Naming conventions (Qt-style, diverges from pure Python snake_case):**

- Public methods use **camelCase** — `setValue()`, `clearDate()`, `setChecked()` — for PySide6 API consistency.
- Python properties use **snake_case** — standard Python convention maintained.
- Qt signals use **camelCase** — inherits C++ Qt naming.
- Private/internal methods use **snake_case** with leading underscore: `_build_layout()`.

**Test naming pattern:**

```python
class TestToggleSwitch:
    def test_toggle_switch_creation_default(self, qt_application) -> None: ...
    def test_toggle_switch_set_checked(self, qt_application) -> None: ...
```

Pattern: `test_<widget>_<behaviour_under_test>`.

**Versioning:**

- Version is defined exclusively in `pyproject.toml` via Hatchling dynamic versioning from `_version.py`. No other file should hardcode the version string.

**Formatting:**

- `ruff format` replaces Black. Never invoke `black` directly.

**Corporate network constraint:**

- No direct network requests without proxy configuration. Prefer local `.whl` files over live PyPI installs where possible.

## Forbidden Patterns

The following patterns are banned and must never appear in committed code:

| Pattern                                  | Replacement                                     |
| :--------------------------------------- | :---------------------------------------------- |
| `print()`                                | `logging`                                       |
| `os.path.*`                              | `pathlib.Path`                                  |
| `Union[X, Y]`                            | `X \| Y`                                        |
| `from typing import List/Dict/Tuple/...` | Native generics: `list[...]`, `dict[...]`       |
| Mutable global variables                 | Module-level constants or injected dependencies |
| Commented-out code in commits            | Delete it or open a tracked issue               |

## Quick Execution Commands

```bash
# Daily workflow
make check        # format + lint + test (full gate)
make test         # unit tests only
make test-cov     # tests with coverage report
make lint         # ruff check only
make format       # ruff format only
make clean        # remove __pycache__, .egg-info, build/, dist/

# Dependency management
uv sync           # install/update all dependencies from lockfile
uv add <pkg>      # add a new dependency
```
