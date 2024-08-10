import typer
from typing_extensions import Annotated

import random
ethics = typer.Typer(help='tells where he comes from')


@ethics.command(name="land")
def comes_from()->None:
    if random.choice([-1,1])>0:
        print("come from toto land!!")
    else:
        print("come from wano!!")



if __name__=='__main__':
    ethics()