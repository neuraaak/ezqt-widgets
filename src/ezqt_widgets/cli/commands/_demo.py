# ///////////////////////////////////////////////////////////////
# CLI Demo Commands
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
CLI commands for running and listing demo examples.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import os
import runpy
import sys
from pathlib import Path

# Third-party imports
import click

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class ExampleRunner:
    """Handles running EzQt Widgets examples.

    Provides functionality to discover, list, and execute example files
    from the EzQt Widgets package.

    Args:
        verbose: Whether to enable verbose output (default: False).
    """

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(self, verbose: bool = False) -> None:
        """Initialize the example runner."""
        self.verbose: bool = verbose
        self.examples_dir: Path = self._find_examples_dir()

    # ------------------------------------------------
    # PRIVATE METHODS
    # ------------------------------------------------

    def _find_examples_dir(self) -> Path:
        """Find the examples directory relative to the package.

        Returns:
            Path to the examples directory.

        Raises:
            FileNotFoundError: If the examples directory cannot be found.
        """
        # First priority: examples in the project root
        package_dir = Path(__file__).parent.parent.parent
        examples_dir = package_dir / "examples"

        if examples_dir.exists():
            return examples_dir

        # Second priority: examples inside the package (ezqt_widgets/examples/)
        package_examples = Path(__file__).parent.parent / "examples"
        if package_examples.exists():
            return package_examples

        # Fallback: try to find examples in the current directory
        current_examples = Path.cwd() / "examples"
        if current_examples.exists():
            return current_examples

        raise FileNotFoundError("Examples directory not found")

    def _execute_example(self, example_path: Path) -> bool:
        """Execute a specific example file.

        Args:
            example_path: Path to the example file to execute.

        Returns:
            True if execution was successful, False otherwise.
        """
        if self.verbose:
            click.echo(f"🚀 Running: {example_path.name}")

        try:
            # Change to the examples directory to ensure relative imports work
            original_cwd = Path.cwd()
            original_argv = sys.argv[:]
            original_sys_path = sys.path.copy()
            os.chdir(example_path.parent)
            sys.argv = [str(example_path)]
            example_dir = str(example_path.parent)
            if example_dir not in sys.path:
                sys.path.insert(0, example_dir)

            runpy.run_path(str(example_path), run_name="__main__")
            return True

        except SystemExit as exc:
            code = exc.code if isinstance(exc.code, int) else 1
            if code != 0:
                click.echo(f"❌ Error running {example_path.name}: exit {code}")
                return False
            return True
        except Exception as e:
            click.echo(f"❌ Exception running {example_path.name}: {e}")
            return False
        finally:
            os.chdir(original_cwd)
            sys.argv = original_argv
            sys.path = original_sys_path

    # ///////////////////////////////////////////////////////////////
    # PUBLIC METHODS
    # ///////////////////////////////////////////////////////////////

    def get_available_examples(self) -> list[Path]:
        """Get list of available example files.

        Returns:
            List of paths to available example files.
        """
        examples: list[Path] = []
        for pattern in ["_*.py", "run_all_examples.py"]:
            examples.extend(self.examples_dir.glob(pattern))
        return sorted(examples)

    def run_example(self, example_name: str) -> bool:
        """Run a specific example by name.

        Args:
            example_name: Name of the example to run (without .py extension).

        Returns:
            True if execution was successful, False otherwise.
        """
        normalized_name = example_name.removesuffix(".py")
        candidates = (
            [normalized_name, normalized_name.lstrip("_")]
            if normalized_name.startswith("_")
            else [normalized_name, f"_{normalized_name}"]
        )

        for candidate in candidates:
            example_path = self.examples_dir / f"{candidate}.py"
            if example_path.exists():
                return self._execute_example(example_path)

        click.echo(f"❌ Example not found: {example_name}")
        return False

    def run_all_examples(self, use_gui_launcher: bool = True) -> bool:
        """Run all examples or use the GUI launcher.

        Args:
            use_gui_launcher: Whether to use the GUI launcher if available
                (default: True).

        Returns:
            True if all examples ran successfully, False otherwise.
        """
        if use_gui_launcher:
            launcher_path = self.examples_dir / "run_all_examples.py"
            if launcher_path.exists():
                return self._execute_example(launcher_path)
            click.echo("⚠️  GUI launcher not found, running examples sequentially")
            use_gui_launcher = False

        # Run each example sequentially
        examples = [
            "_button",
            "_input",
            "_label",
            "_misc",
        ]
        success_count = 0

        for example in examples:
            click.echo(f"\n{'=' * 50}")
            click.echo(f"🚀 Running: {example}")
            click.echo(f"{'=' * 50}")

            if self.run_example(example):
                success_count += 1
            else:
                click.echo(f"❌ Failed to run: {example}")

        click.echo(f"\n✅ Successfully ran {success_count}/{len(examples)} examples")
        return success_count == len(examples)

    def list_examples(self) -> None:
        """List all available examples."""
        examples = self.get_available_examples()

        if not examples:
            click.echo("❌ No examples found")
            return

        click.echo("📋 Available examples:")
        click.echo("=" * 40)

        for example in examples:
            status = "✅" if example.exists() else "❌"
            click.echo(f"{status} {example.stem}")

        click.echo(f"\nTotal: {len(examples)} examples found")


# ///////////////////////////////////////////////////////////////
# PUBLIC FUNCTIONS
# ///////////////////////////////////////////////////////////////


def run_example_by_category(category: str, verbose: bool = False) -> bool:
    """Run examples by category.

    Args:
        category: Category name (buttons, inputs, labels, misc).
        verbose: Whether to enable verbose output (default: False).

    Returns:
        True if execution was successful, False otherwise.
    """
    runner = ExampleRunner(verbose)

    category_mapping = {
        "buttons": "_button",
        "inputs": "_input",
        "labels": "_label",
        "misc": "_misc",
    }

    if category not in category_mapping:
        click.echo(f"❌ Unknown category: {category}")
        click.echo(f"Available categories: {', '.join(category_mapping.keys())}")
        return False

    return runner.run_example(category_mapping[category])


def run_all_examples(use_gui: bool = True, verbose: bool = False) -> bool:
    """Run all examples.

    Args:
        use_gui: Whether to use the GUI launcher if available (default: True).
        verbose: Whether to enable verbose output (default: False).

    Returns:
        True if all examples ran successfully, False otherwise.
    """
    runner = ExampleRunner(verbose)
    return runner.run_all_examples(use_gui)


def list_available_examples() -> None:
    """List all available examples."""
    runner = ExampleRunner()
    runner.list_examples()


# ///////////////////////////////////////////////////////////////
# COMMANDS
# ///////////////////////////////////////////////////////////////


@click.group(name="demo", help="Run and list demo examples")
def demo_group() -> None:
    """Demo command group."""


@demo_group.command(name="run", help="Run widget examples")
@click.option(
    "--all", "-a", "run_all", is_flag=True, help="Run all examples with GUI launcher"
)
@click.option(
    "--buttons",
    "-b",
    is_flag=True,
    help="Run button examples (DateButton, IconButton, LoaderButton)",
)
@click.option(
    "--inputs",
    "-i",
    is_flag=True,
    help="Run input examples (AutoComplete, Password, Search, TabReplace)",
)
@click.option(
    "--labels",
    "-l",
    is_flag=True,
    help="Run label examples (ClickableTag, Framed, Hover, Indicator)",
)
@click.option(
    "--misc",
    "-m",
    is_flag=True,
    help="Run misc examples (CircularTimer, DraggableList, OptionSelector, ToggleIcon, ToggleSwitch)",
)
@click.option(
    "--verbose", "-v", is_flag=True, help="Verbose output with detailed information"
)
def run_command(
    run_all: bool,
    buttons: bool,
    inputs: bool,
    labels: bool,
    misc: bool,
    verbose: bool,
) -> None:
    """Run EzQt Widgets examples."""
    options_selected = any([run_all, buttons, inputs, labels, misc])

    if not options_selected:
        click.echo("❌ Please specify which examples to run.")
        click.echo("\n📋 Available options:")
        click.echo("  --all, -a        Run all examples with GUI launcher")
        click.echo("  --buttons, -b    Run button examples")
        click.echo("  --inputs, -i     Run input examples")
        click.echo("  --labels, -l     Run label examples")
        click.echo("  --misc, -m       Run misc examples")
        click.echo("\n💡 Example: ezqt run --buttons")
        return

    if verbose:
        click.echo("🔍 Verbose mode enabled")

    success = True

    if run_all:
        click.echo("🎯 Running all examples...")
        success = run_all_examples(use_gui=True, verbose=verbose)

    elif buttons:
        click.echo("🎛️  Running button examples...")
        success = run_example_by_category("buttons", verbose)

    elif inputs:
        click.echo("⌨️  Running input examples...")
        success = run_example_by_category("inputs", verbose)

    elif labels:
        click.echo("🏷️  Running label examples...")
        success = run_example_by_category("labels", verbose)

    elif misc:
        click.echo("🔧 Running misc examples...")
        success = run_example_by_category("misc", verbose)

    if success:
        click.echo("✅ Examples completed successfully!")
    else:
        click.echo("❌ Some examples failed to run.")
        raise SystemExit(1)


@demo_group.command(name="list", help="List available examples")
def list_command() -> None:
    """List available examples."""
    list_available_examples()
