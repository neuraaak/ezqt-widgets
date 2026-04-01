# API reference

Navigation index for the `ezqt_widgets` public API.
Each entry below links to the detailed reference page for that widget group.

## 📦 Widget modules

| Module                                  | Classes                                                                                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Button](reference/button.md)           | `DateButton`, `DatePickerDialog`, `IconButton`, `LoaderButton`                                                                            |
| [Input](reference/input.md)             | `AutoCompleteInput`, `FilePickerInput`, `PasswordInput`, `SearchInput`, `SpinBoxInput`, `TabReplaceTextEdit`                              |
| [Label](reference/label.md)             | `ClickableTagLabel`, `FramedLabel`, `HoverLabel`, `IndicatorLabel`                                                                        |
| [Misc](reference/misc.md)               | `CircularTimer`, `CollapsibleSection`, `DraggableList`, `NotificationBanner`, `OptionSelector`, `ThemeIcon`, `ToggleIcon`, `ToggleSwitch` |
| [Shared constants](reference/shared.md) | `ANIMATION_DURATION_*`, `ICON_SIZE_*`, `SVG_*`                                                                                            |

## 🔤 Type aliases

All public type aliases are defined in `ezqt_widgets.types`:

| Type alias           | Accepted values                                         |
| -------------------- | ------------------------------------------------------- |
| `IconSource`         | `QIcon \| str \| None`                                  |
| `IconSourceExtended` | `QIcon \| QPixmap \| str \| bytes \| ThemeIcon \| None` |
| `SizeType`           | `QSize \| tuple[int, int]`                              |
| `ColorType`          | `QColor \| str`                                         |
| `WidgetParent`       | `QWidget \| None`                                       |
| `AnimationDuration`  | `int`                                                   |
| `EventCallback`      | `Callable[[], None]`                                    |
| `ValueCallback`      | `Callable[[Any], None]`                                 |

For the complete, auto-generated symbol listing (all public classes, methods, and
attributes), see the [full reference](reference/index.md) page.

!!! note
Only public symbols are documented here (private members prefixed with `_` are excluded).
For usage examples, see [Examples](../examples/index.md).
