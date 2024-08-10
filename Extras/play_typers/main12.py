import typer
from typing import Optional
import random

# Command groups in single file


#
app = typer.Typer(no_args_is_help=True)

##
ppl  = typer.Typer(no_args_is_help=True)
pdt  = typer.Typer(no_args_is_help=True)
###
ethinics = typer.Typer(no_args_is_help=True)

ppl.add_typer(ethinics,name='ethinicity')

app.add_typer(ppl,name="people")
app.add_typer(pdt,name="product")


@pdt.command(help='utility to create product')
def create(item: str):
    print(f"Creating item: {item}")

@pdt.command("del",help='utility to del product')
def delete(item: str):
    print(f"Deleting item: {item}")


@ppl.command("create",help='utility to create user')
def create(user_name: str):
    print(f"Creating user: {user_name}")

@ppl.command("del",help='utility to del user')
def delete(user_name: str):
    print(f"Deleting user: {user_name}")



@ethinics.command(name="land")
def comes_from()->None:
    if random.choice([-1,1])>0:
        print("come from toto land!!")
    else:
        print("come from wano!!")


if __name__=='__main__':
    app()