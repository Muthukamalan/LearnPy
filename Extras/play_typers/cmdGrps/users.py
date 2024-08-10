import typer


import ethinicity

app = typer.Typer()


app.add_typer(ethinicity.ethics,name="ethinic")

@app.command("create",help='utility to create user')
def create(user_name: str):
    print(f"Creating user: {user_name}")


@app.command("del",help='utility to del user')
def delete(user_name: str):
    print(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()



'''
$ ls
. .. users.py 

$ python users.py create muthu
$ python users.py delete kakashi
'''