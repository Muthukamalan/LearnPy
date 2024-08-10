# CLI Options (*not required)


'''
`note:` 
- best practice required mentioned as argument
- options are typer.Optional but if you really want you can change that too
    - skipping
    ```python
        debug:Annotated[bool,typer.Option(rich_help_panel='dev tools',show_default=True,default=...)],
    ```
    add this line after planet in greet fn
'''

from typing import Optional
import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def greet(
        planet: str,
        galaxy: Annotated[
                        str,
                        typer.Option(
                            "--galxy",'-g',                   # shorter_name
                            help="name of galaxy::",
                            rich_help_panel="Galaxies",
                        )
                ]="M64",  #Andromeda Galaxy
        
    )->None:
    print(f"Hello {planet},🌍 and how's your {galaxy} 📚")


@app.command()
def bye(planet:str,galaxy:Optional[str]="M64"):
    print(f"Hello {planet},🌍 and take care your {galaxy} 📚 too!")


if __name__=="__main__":
    app()


# $ python main6.py 
# $ python main6.py --help


