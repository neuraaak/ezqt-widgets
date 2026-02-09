# User Guides

In-depth guides and tutorials for **EzQt Widgets** library.

## Overview

This section provides comprehensive guides for mastering EzQt Widgets features and best practices. Whether you're just getting started or looking to contribute to the project, you'll find detailed documentation here.

## Available Guides

| Guide                               | Description                                    | Level        |
| ----------------------------------- | ---------------------------------------------- | ------------ |
| [QSS Style Guide](style-guide.md)   | Visual customization with Qt stylesheets       | Beginner     |
| [Development Guide](development.md) | Development workflow and contribution guide    | Intermediate |
| [Testing Guide](testing.md)         | Test suite documentation and testing practices | Advanced     |

## Quick Links

### For Beginners

- [Getting Started](../getting-started.md) - Start here if you're new to EzQt Widgets
- [Basic Examples](../examples/index.md) - Simple usage examples for each widget
- [QSS Style Guide](style-guide.md) - Learn to customize widget appearance

### For Developers

- [Development Guide](development.md) - Set up your development environment
- [Testing Guide](testing.md) - Run tests and understand the test suite
- [API Reference](../api/index.md) - Complete API documentation

### For Advanced Users

- [API Reference](../api/index.md) - Detailed widget documentation
- [CLI Reference](../cli/index.md) - Command-line interface usage
- [GitHub Repository](https://github.com/neuraaak/ezqt_widgets) - Source code and issues

## Topics

### Core Concepts

- **Qt Signals & Slots** - Understanding widget communication through Qt's signal/slot mechanism
- **QPropertyAnimation** - Smooth animations with configurable easing curves
- **QSS Styling** - Customizing widget appearance with Qt stylesheets
- **Type Hints** - Using Python type annotations for better IDE support

### Widget Features

- **Button Widgets** - Date pickers, icon buttons, and loading buttons
- **Input Widgets** - Auto-complete, search, and password inputs
- **Label Widgets** - Clickable tags, hover labels, and status indicators
- **Misc Widgets** - Timers, drag-and-drop lists, toggles, and selectors

### Integration

- **Application Integration** - Integrating EzQt Widgets into your PySide6 applications
- **Custom Styling** - Creating custom themes and visual styles
- **Signal Management** - Connecting widgets with signals and slots
- **Layout Management** - Organizing widgets in layouts

### Best Practices

- **Performance** - Optimizing widget performance in large applications
- **Error Handling** - Robust error handling with Qt widgets
- **Testing** - Testing applications that use EzQt Widgets
- **Code Organization** - Structuring your Qt application code

## Development Workflow

### Setting Up

1. **Clone the repository**

   ```bash
   git clone https://github.com/neuraaak/ezqt_widgets.git
   cd ezqt_widgets
   ```

2. **Install in development mode**

   ```bash
   pip install -e ".[dev]"
   ```

3. **Install pre-commit hooks**

   ```bash
   pre-commit install
   ```

See the [Development Guide](development.md) for detailed setup instructions.

### Testing

Run the test suite to ensure everything works:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=ezqt_widgets

# Run specific test types
pytest tests/unit/
pytest tests/integration/

# Using the CLI
ezqt test --unit
ezqt test --coverage
```

See the [Testing Guide](testing.md) for more information.

### Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature/amazing-widget`)
3. **Make your changes** with tests
4. **Run tests and linting** (`pytest`, `ruff check`)
5. **Commit your changes** with conventional commits
6. **Push to your fork** (`git push origin feature/amazing-widget`)
7. **Open a Pull Request** on GitHub

See the [Development Guide](development.md) for contribution guidelines.

## Code Style

EzQt Widgets follows these coding standards:

- **PEP 8** - Python style guide
- **Type Hints** - Full type annotations for Python 3.10+
- **Docstrings** - Google-style docstrings for all public APIs
- **Testing** - Comprehensive test coverage (~75%)
- **Black** - Code formatting (88 character line length)
- **Ruff** - Linting and code quality

## Documentation

### Building Docs

Build the documentation locally:

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Build documentation
mkdocs build

# Serve locally
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Writing Docs

Documentation is written in Markdown and built with MkDocs Material:

- **Guides** - Located in `docs/guides/`
- **API Reference** - Auto-generated from docstrings with mkdocstrings
- **Examples** - Code examples in `docs/examples/`
- **CLI** - Command-line interface docs in `docs/cli/`

## See Also

- [Getting Started](../getting-started.md) - Quick start guide
- [API Reference](../api/index.md) - Complete API documentation
- [Examples](../examples/index.md) - Practical code examples
- [CLI Reference](../cli/index.md) - Command-line interface

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezqt_widgets/issues)
- **Discussions**: [GitHub Discussions](https://github.com/neuraaak/ezqt_widgets/discussions)
- **Repository**: [https://github.com/neuraaak/ezqt_widgets](https://github.com/neuraaak/ezqt_widgets)

---

**Happy coding with EzQt Widgets!** 🚀
