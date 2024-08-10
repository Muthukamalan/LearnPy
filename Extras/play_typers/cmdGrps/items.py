import typer

app = typer.Typer()


@app.command(help='utility to create product')
def create(item: str):
    print(f"Creating item: {item}")


@app.command("del",help='utility to del product')
def delete(item: str):
    print(f"Deleting item: {item}")


@app.command(help='utility to sell product')
def sell(item: str):
    print(f"Selling item: {item}")


if __name__ == "__main__":
    app()


'''
$ ls
. .. items.py 

$ python items.py sell cake
$ python items.py delete cake
$ python items.py create cake
'''