# ///////////////////////////////////////////////////////////////
# CLI_MAIN - CLI Main Entry Point
# Project: ezqt_widgets
# ///////////////////////////////////////////////////////////////

"""
EzQt Widgets CLI - Main entry point.

Command-line interface for running examples and utilities.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import click
from rich.panel import Panel
from rich.text import Text

# Local imports
from .._version import __version__
from ._console import console
from .commands import demo_group, docs_command, info_command, version_command

# ///////////////////////////////////////////////////////////////
# CLI GROUP
# ///////////////////////////////////////////////////////////////


@click.group(
    name="ezqt-widgets",
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(
    __version__,
    "-v",
    "--version",
    prog_name="EzQt Widgets CLI",
    message="%(prog)s version %(version)s",
)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """EzQt Widgets CLI - Launch examples and utilities.

    A command-line interface for running EzQt Widgets examples
    and managing the development workflow.
    """
    if ctx.invoked_subcommand is None:
        _display_welcome()
        click.echo(ctx.get_help())


def _display_welcome() -> None:
    """Display a welcome message."""
    try:
        welcome_text = Text()
        welcome_text.append("EzQt Widgets CLI", style="bold bright_blue")
        welcome_text.append(" - Qt Widgets Toolkit", style="dim white")

        panel = Panel(
            welcome_text,
            title="[bold bright_blue]Welcome[/bold bright_blue]",
            border_style="bright_blue",
            padding=(1, 2),
        )
        console.print(panel)
    except (OSError, RuntimeError, ValueError):
        click.echo("EzQt Widgets CLI - Qt Widgets Toolkit")


# ///////////////////////////////////////////////////////////////
# COMMAND GROUPS
# ///////////////////////////////////////////////////////////////

# Register commands and groups
cli.add_command(demo_group)
cli.add_command(docs_command)
cli.add_command(info_command)
cli.add_command(version_command)


# ///////////////////////////////////////////////////////////////
# MAIN ENTRY POINT
# ///////////////////////////////////////////////////////////////


def main() -> None:
    """Main entry point for the CLI."""
    try:
        cli()
    except click.ClickException as e:
        e.show()
        raise SystemExit(e.exit_code) from e
    except KeyboardInterrupt as e:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        raise SystemExit(1) from e
    except (OSError, RuntimeError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1) from e


if __name__ == "__main__":
    main()
