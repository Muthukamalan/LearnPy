import typer
from rich import print

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
    "socials":{
        'github':'https://github.com/muthukamalan',
        'blog':'https://muthukamalan.github.io/'
    }
}



if __name__=='__main__':
    print("[bold red]Alert![/bold red] [green]Profile[/green] overload! :boom:")
    print(data)