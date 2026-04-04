# How to set up a development environment

Set up a local environment to contribute to `ezqt-widgets`.

## 🔧 Prerequisites

- Python >= 3.11 ([python.org](https://www.python.org/downloads/))
- [uv](https://docs.astral.sh/uv/) installed (`pip install uv`)
- [git](https://git-scm.com/) installed

## 📝 Steps

1. Clone the repository.

   ```bash
   git clone https://github.com/neuraaak/ezqt-widgets.git
   cd ezqt-widgets
   ```

2. Create a virtual environment and install all dependencies.

    === "uv"

        ```bash
        uv sync --extra dev
        ```

    === "pip"

        ```bash
        pip install -e ".[dev]"
        ```

   You should see all packages resolved and installed from the lockfile.

3. Install pre-commit hooks.

   ```bash
   uv run pre-commit install
   ```

   You should see `pre-commit installed at .git/hooks/pre-commit`.

## ✅ Result

You now have a working development environment. Run `uv run pytest` to verify the test suite passes.

## ➡️ Next steps

- [How to run and write tests](testing.md)
- [API Reference](../api/index.md)
