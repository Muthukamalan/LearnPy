from typing import Optional

import typer
from typing_extensions import Annotated

__version__ = "0.1.0"

app = typer.Typer(no_args_is_help=True)  # by-default `--help` to get help not now 


def return_version():
    print(f"Good APP:: {__version__}")
    # 🥚 find me, As a callback I ran before main execute or after execute:: check main9.py
    raise typer.Exit(0)

@app.command()
def main(
    name: Annotated[str, typer.Argument()],
    version: Annotated[
        Optional[bool], typer.Option("--version",'-V', callback=return_version,is_eager=True)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()