import typer
import random
from rich import print


app = typer.Typer()


# make chits
chits = list(range(1,10))
chits.extend( list(range(100,105)) )



@app.command(name="throw")
def throw_stones(*,material='cotton'):
    pick_one = random.choice(chits)
    
    if pick_one>100:
        print('not have enough material to hit!!')
        raise typer.Exit(code=-1)
    else:
        if material=='cotton':
            for _ in range(pick_one):
                print('I hit softly!!')
        else:
            for _ in range(pick_one):
                print('彼を死なせてください ⚰️')
            


if __name__=='__main__':
    app()


# python main4.py --material stone
# python main4.py 
# python main4.py --help
# if it's error  `$ echo $?`