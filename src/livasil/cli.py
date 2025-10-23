from typing import Optional
import typer
from rich import print
from . import __version__

app = typer.Typer(no_args_is_help=True, add_completion=False, help="LivAsil Requirements Agent CLI")

@app.command()
def version():
    print(f"[bold green]livasil[/] v{__version__}")

@app.command()
def hello(name: Optional[str] = typer.Argument(None)):
    who = name or "world"
    print(f"hello, [cyan]{who}[/]!")

if __name__ == "__main__":
    app()
