# Test Documentation

Comprehensive documentation for the **ezqt_widgets** test suite.
The test suite ensures reliability, robustness, and correctness of all widgets through unit tests.

---

## Test Structure

### Directory Organization

```text
tests/
├── conftest.py                    # Pytest configuration and fixtures
├── run_tests.py                   # Test runner script
└── unit/                          # Unit tests
    ├── test_button/               # Button widget tests
    │   ├── test_date_button.py
    │   ├── test_icon_button.py
    │   └── test_loader_button.py
    ├── test_input/                # Input widget tests
    │   ├── test_auto_complete_input.py
    │   ├── test_search_input.py
    │   └── test_tab_replace_textedit.py
    ├── test_label/                # Label widget tests
    │   ├── test_clickable_tag_label.py
    │   ├── test_framed_label.py
    │   ├── test_hover_label.py
    │   └── test_indicator_label.py
    └── test_misc/                 # Misc widget tests
        ├── test_circular_timer.py
        ├── test_draggable_list.py
        ├── test_option_selector.py
        ├── test_toggle_icon.py
        └── test_toggle_switch.py
```

### Test Statistics

| Category  | Widgets | Tests    | Coverage |
| --------- | ------- | -------- | -------- |
| Button    | 3       | ~59      | ~85%     |
| Input     | 3       | ~62      | ~85%     |
| Label     | 4       | ~40      | ~80%     |
| Misc      | 5       | ~50      | ~80%     |
| **Total** | **15**  | **~211** | **~80%** |

---

## Button Tests

### DateButton

**File:** `test_button/test_date_button.py` -- 20 tests

- Utility functions (`format_date`, `parse_date`, `get_calendar_icon`)
- `DatePickerDialog` class
- Creation with default and custom parameters
- Properties (date, format, show_calendar_icon, min_width, min_height)
- Signals (`dateChanged`, `dateSelected`)
- Methods (`clear_date`, `set_today`, `open_calendar`)
- Date handling (QDate, string, custom format)
- Mouse events and display

### IconButton

**File:** `test_button/test_icon_button.py` -- 17 tests

- Utility functions (`colorize_pixmap`, `load_icon_from_source`)
- Creation with default and custom parameters
- Properties (icon, text, icon_size, icon_color, min_width, min_height)
- Icon handling (QIcon, file, SVG, URL)
- Signals (`iconChanged`, `textChanged`)
- Methods (`clear_icon`, `clear_text`, `toggle_text_visibility`)
- Pixmap colorization and opacity

### LoaderButton

**File:** `test_button/test_loader_button.py` -- 22 tests

- Utility functions (`create_spinner_pixmap`, `create_loading_icon`)
- Creation with default and custom parameters
- Properties (loading, success, error, animation_speed, show_duration)
- Signals (`loadingStarted`, `loadingFinished`, `loadingFailed`)
- Loading states (loading, success, error)
- Animations and timers
- State transitions

---

## Input Tests

### AutoCompleteInput

**File:** `test_input/test_auto_complete_input.py` -- 17 tests

- Creation with default and custom parameters
- Properties (suggestions, case_sensitive, filter_mode, completion_mode)
- Suggestion handling (add, remove, clear)
- Integration with QCompleter
- Case sensitivity
- Filtering modes (MatchContains, MatchStartsWith, MatchEndsWith)
- Completion modes (PopupCompletion, InlineCompletion)

### SearchInput

**File:** `test_input/test_search_input.py` -- 20 tests

- Creation with default and custom parameters
- Properties (search_icon, icon_position, clear_button, max_history)
- History handling (add, clear, set, trim)
- Icon and position handling
- Text and placeholder handling
- Signals (searchSubmitted)

### TabReplaceTextEdit

**File:** `test_input/test_tab_replace_textedit.py` -- 25 tests

- Creation with default and custom parameters
- Properties (tab_replacement, sanitize_on_paste, remove_empty_lines)
- `sanitize_text` method with different cases
- Custom tab replacement
- Preservation of whitespace
- Special characters and Unicode

---

## Label Tests

### ClickableTagLabel

**File:** `test_label/test_clickable_tag_label.py`

- Creation with default and custom parameters
- Properties (name, enabled, status_color, min_width, min_height)
- Signals (clicked, toggle_keyword, stateChanged)
- State handling (enabled/disabled)

### FramedLabel

**File:** `test_label/test_framed_label.py`

- Creation with default and custom parameters
- Properties (text, alignment, min_width, min_height)
- Signal (textChanged)
- Text alignment

### HoverLabel

**File:** `test_label/test_hover_label.py`

- Creation with default and custom parameters
- Properties (opacity, hover_icon, icon_size, icon_color, icon_padding)
- Signal (hoverIconClicked)
- Hover icon handling

### IndicatorLabel

**File:** `test_label/test_indicator_label.py`

- Creation with default and custom parameters
- Properties (status, status_map)
- Signal (statusChanged)
- Customizable status map

---

## Misc Tests

### CircularTimer

**File:** `test_misc/test_circular_timer.py`

- Creation with default and custom parameters
- Properties (duration, ring_color, node_color, ring_width_mode, loop)
- Signals (timerReset, clicked, cycleCompleted)
- Timer control methods

### DraggableList

**File:** `test_misc/test_draggable_list.py`

- Creation with default and custom parameters
- Properties (items, compact, min_width, icon_color)
- Signals (itemMoved, itemRemoved, itemAdded, itemClicked, orderChanged)
- Methods (add_item, remove_item, clear_items, move_item)

### OptionSelector

**File:** `test_misc/test_option_selector.py`

- Creation with default and custom parameters
- Properties (options, current_value, current_value_id)
- Signals (valueChanged, valueIdChanged)

### ToggleIcon

**File:** `test_misc/test_toggle_icon.py`

- Creation with default and custom parameters
- Properties (opened_icon, closed_icon, state, icon_size, icon_color)
- Signals (stateChanged, clicked)

### ToggleSwitch

**File:** `test_misc/test_toggle_switch.py`

- Creation with default and custom parameters
- Properties (checked, width, height, animation)
- Signal (toggled)

---

## Running Tests

### Using pytest

```bash
# All tests
pytest tests/

# Specific directory
pytest tests/unit/test_button/
pytest tests/unit/test_input/
pytest tests/unit/test_label/
pytest tests/unit/test_misc/

# Specific file
pytest tests/unit/test_button/test_icon_button.py

# With coverage
pytest --cov=ezqt_widgets --cov-report=html tests/

# Verbose mode
pytest tests/ -v
```

### Using run_tests.py

```bash
# Unit tests
python tests/run_tests.py --type unit

# With coverage
python tests/run_tests.py --coverage

# Verbose mode
python tests/run_tests.py --verbose

# Fast mode (exclude slow tests)
python tests/run_tests.py --fast
```

### Coverage Reports

```bash
# Terminal report
pytest --cov=ezqt_widgets --cov-report=term-missing tests/

# HTML report
pytest --cov=ezqt_widgets --cov-report=html:htmlcov tests/
# Open htmlcov/index.html in browser
```

---

## Test Configuration

### `conftest.py` -- Shared Fixtures

**Location:** `tests/conftest.py`

**Available Fixtures:**

| Fixture             | Scope    | Description                         |
| ------------------- | -------- | ----------------------------------- |
| `qt_application`    | session  | QApplication instance for all tests |
| `qt_widget_cleanup` | function | Widget cleanup after each test      |
| `wait_for_signal`   | function | Helper to wait for Qt signals       |
| `mock_icon_path`    | function | Temporary icon file for testing     |
| `mock_svg_path`     | function | Temporary SVG file for testing      |

### Test Markers

Custom pytest markers for test categorization:

- `@pytest.mark.unit` -- Unit tests (default)
- `@pytest.mark.slow` -- Slow tests (exclude with `-m "not slow"`)

**Usage:**

```bash
# Run only unit tests
pytest -m unit

# Run all except slow tests
pytest -m "not slow"
```

---

## Best Practices

### 1. Test Isolation

Each test is independent. The `qt_widget_cleanup` fixture ensures proper cleanup:

```python
def test_widget_creation(qt_widget_cleanup):
    widget = SomeWidget()
    assert widget is not None
```

### 2. Use Fixtures

Use shared fixtures from `conftest.py`:

```python
def test_widget_with_icon(qt_widget_cleanup, mock_icon_path):
    widget = IconButton(icon=mock_icon_path)
    assert widget.icon is not None
```

### 3. Use Appropriate Markers

```python
@pytest.mark.unit
def test_something(qt_widget_cleanup):
    pass

@pytest.mark.slow
def test_slow_operation(qt_widget_cleanup):
    pass
```

### 4. Signal Testing

```python
def test_signal_emission(qt_widget_cleanup, wait_for_signal):
    widget = Widget()
    assert wait_for_signal(widget.someSignal)
```

### 5. Coverage Goals

Aim for >80% code coverage.

---

## Known Issues

### OptionSelector Test

- **Test**: `test_option_selector_selected_option_property`
- **Issue**: Fixed by using property access (`selected_option.text`) instead of method call
- **Status**: Resolved

### DateButton Dialog Blocking

- **Test**: `test_date_button_mouse_press_event`
- **Issue**: Dialog was opening and blocking tests
- **Fix**: Mocked `DatePickerDialog` to avoid blocking
- **Status**: Resolved

### Common Issues

| Issue                        | Solution                            |
| ---------------------------- | ----------------------------------- |
| QApplication already created | Use `qt_application` fixture        |
| Random test failures         | Use `wait_for_signal` or add delays |
| Memory leaks                 | Use `qt_widget_cleanup` fixture     |

---

## Resources

- [API Reference](../api/index.md) -- Complete widget documentation
- [Examples](../examples/index.md) -- Usage examples
- [Development Guide](development.md) -- Setup and tools
