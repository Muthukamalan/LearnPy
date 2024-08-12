
'''
In Analogy,
- git `command/CLI-APP`
- pull `sub-command` 
    - it's having own arguments and options
    - --set-upstream orign main `optionals`
- push `sub-command`

note: It's common to call 'CLI-APP' as / 'sub-command' as 'command';
'''
import typer
from typing_extensions import Annotated

app = typer.Typer(help='CLI 🖥️ Appliation </>',no_args_is_help=True,rich_markup_mode='rich')


@app.command(help='create user',epilog="Made ❤️ with muthu")
def create(username: str):
    print(f"Creating user: {username}")


@app.command(help='**Delete** a user') #[bold red]Delete[/bold red] a user with [italic]USERNAME[/italic].
def delete(
    username: str,
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete the user?",)
    ],
):
    '''
    python main8.py delete muthu --force  #passing flag means force=True
    '''
    if force:
        print(f"Deleting user: {username}")
    else:
        print("Operation cancelled")


@app.command(help='delete-all users',deprecated=True,)
def delete_all(
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete ALL users?",help='forcelly?')
    ],
):
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


@app.command(help='init DB',deprecated=False)
def init():
    print("Initializing user database")


if __name__ == "__main__":
    app()
