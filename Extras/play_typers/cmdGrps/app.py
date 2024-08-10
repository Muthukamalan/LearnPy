import typer
from typing import Optional


import items
import users

app = typer.Typer(no_args_is_help=True)
app.add_typer(users.app,name='ppl')
app.add_typer(items.app,name='things')



if __name__=='__main__':
    app()