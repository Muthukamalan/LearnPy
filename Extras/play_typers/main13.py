from typing import Tuple

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing_extensions import Annotated
import time 

def main(
        user: Annotated[Tuple[str, int, bool], typer.Option()] = (None, None, None),
        names: Annotated[
                    Tuple[str, str, str], typer.Option(help="Select 3 characters to play with")
                ] = ("Harry", "Hermione", "Ron")
)->None:
    username, coins, is_wizard = user
    if not username:
        print("No user provided")
        raise typer.Abort()
    print(f"The username {username} has {coins} coins")
    if is_wizard:
        print("And this user is a wizard!")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        time.sleep(2)
        for name in names[:2]:  print(f"Hello, {name}")
        progress.add_task(description="Preparing...", total=None)
        time.sleep(2)
        for name in names[2:]: print(f"Hello, {name}")
        print('*'*10)
    with typer.progressbar(names,length=100) as progress:
        for user in progress:
            typer.echo(user)


if __name__ == "__main__":
    typer.run(main)