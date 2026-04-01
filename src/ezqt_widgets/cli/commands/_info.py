# ///////////////////////////////////////////////////////////////
# EZQT_WIDGETS - CLI Info Command
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
CLI command for displaying package information.

This module provides the info command for EzQt-Widgets.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

# Third-party imports
import click
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Local imports
import ezqt_widgets

from .._console import console
from ._demo import ExampleRunner

# ///////////////////////////////////////////////////////////////
# COMMANDS
# ///////////////////////////////////////////////////////////////


@click.command(name="info", help="Display package information")
def info_command() -> None:
    """
    Display package information.

    Show detailed information about the EzQt-Widgets package including
    version, location, and dependencies.
    """
    try:
        # Package info
        pkg_version = getattr(ezqt_widgets, "__version__", "unknown")
        author = getattr(ezqt_widgets, "__author__", "unknown")
        maintainer = getattr(ezqt_widgets, "__maintainer__", "unknown")
        description = getattr(ezqt_widgets, "__description__", "unknown")
        url = getattr(ezqt_widgets, "__url__", "unknown")

        try:
            package_path = (
                Path(ezqt_widgets.__file__).parent
                if hasattr(ezqt_widgets, "__file__")
                else None
            )
        except (AttributeError, TypeError, OSError):
            package_path = None
        try:
            runner = ExampleRunner()
            examples = runner.get_available_examples()
            example_count = len(examples)
        except FileNotFoundError:
            example_count = None

        # Build info text
        text = Text()
        text.append("Package Information\n", style="bold bright_blue")
        text.append("=" * 50 + "\n\n", style="dim")

        # Version
        text.append("Version: ", style="bold")
        text.append(f"{pkg_version}\n", style="white")

        # Author
        text.append("Author: ", style="bold")
        text.append(f"{author}\n", style="white")

        if maintainer != author:
            text.append("Maintainer: ", style="bold")
            text.append(f"{maintainer}\n", style="white")

        # Description
        text.append("\nDescription:\n", style="bold")
        text.append(f"  {description}\n", style="dim white")

        # URL
        text.append("\nURL: ", style="bold")
        text.append(f"{url}\n", style="cyan")

        # Package location
        if package_path:
            text.append("\nPackage Location: ", style="bold")
            text.append(f"{package_path}\n", style="dim white")

        # Examples
        if example_count is not None:
            text.append("\nExamples: ", style="bold")
            text.append(f"{example_count} found\n", style="white")
        else:
            text.append("\nExamples: ", style="bold")
            text.append("Not found\n", style="white")

        # Display panel
        panel = Panel(
            text,
            title="[bold bright_blue]EzQt-Widgets Information[/bold bright_blue]",
            border_style="bright_blue",
            padding=(1, 2),
        )
        console.print(panel)

        # Dependencies table
        try:
            import PySide6
            import rich

            try:
                click_version = version("click")
            except PackageNotFoundError:
                click_version = "unknown"

            deps_table = Table(
                title="Dependencies", show_header=True, header_style="bold blue"
            )
            deps_table.add_column("Package", style="cyan")
            deps_table.add_column("Version", style="green")

            deps_table.add_row("PySide6", getattr(PySide6, "__version__", "unknown"))
            deps_table.add_row("rich", getattr(rich, "__version__", "unknown"))
            deps_table.add_row("click", click_version)

            console.print("\n")
            console.print(deps_table)
        except (ImportError, OSError, RuntimeError, ValueError) as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

    except click.ClickException:
        raise
    except (OSError, RuntimeError, ValueError, TypeError, AttributeError) as e:
        raise click.ClickException(str(e)) from e
