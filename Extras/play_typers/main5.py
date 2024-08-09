# CLI Arguments
## CLI arguments are **required**
## CLI options are optional


from typing import Optional
import typer
from typing_extensions import Annotated
# note::  support for Annotated starts from '0.9.0' otherwise get error and prefer to use `Annotated` instead 'Argument::OLD_VERSION'


'''
def main(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)
'''

app = typer.Typer()

@app.command()
def greet(
        planet: Annotated[
                    Optional[str], 
                    typer.Argument(
                        help="enter your loved ❤️ planet name:: ",
                        show_default=True,
                        metavar="[PLANET 🌎]",
                        rich_help_panel="Arguments"
                    )]="Earth"
    )->None:
    '''
        we explicitly mentioning `planet` is a argument (required)
        - but by default="Earth"
    '''
    if planet is not None: print(f"Hello {planet} 🌍")
    else: print("hello")


@app.command()
def bye(planet:Optional[str]="Earth"):
    '''
        It take it as Optional (not required for function to execute.)
        - but we need and by default making as "Earth"
    '''
    if planet is None: print(f"bye,")
    else: print(f"bye, {planet}!! 🪐")



#TODO: arguments with env variables

if __name__=="__main__":
    app()


#  Annotated allows us to pass additional metadata that can be used by Typer

# $ python main5.py greet --help                                                                                                             
#  Usage: main5.py greet [OPTIONS] [PLANET 🌎]                                                                                                                                                                                 
#  DOCSTRING
# ╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────╮
# │   planet      [PLANET 🌎]  enter your loved ❤️ planet name:: [default: Earth]                                 │
# ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# ╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────╮
# │ --help          Show this message and exit.                                                               │
# ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯



# $ python main5.py bye --help                                                                                                            
#  Usage: main5.py bye [OPTIONS]                                                                                                                                                             
#  DOCSTRING
# ╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────╮
# │ --planet        TEXT  [default: Earth]                                                                    │
# │ --help                Show this message and exit.                                                         │
# ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯



