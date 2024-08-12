
from typing import Optional,List,Dict,OrderedDict
import typer
from typing_extensions import Annotated
from datetime import datetime
from enum import Enum

app = typer.Typer()

"""
@app.command()
def main(name: str, age: int = 20, height_meters: float = 1.89, female: bool = True):
    '''
        by-default ,
        - name: required
        - age,height_meters,female: optional
    '''
    print(f"NAME is {name}, of type: {type(name)}")
    print(f"--age is {age}, of type: {type(age)}")
    print(f"--height-meters is {height_meters}, of type: {type(height_meters)}")
    print(f"--female is {female}, of type: {type(female)}")
"""


class NeuralNetwork(str,Enum):
    simple="neuron"
    conv  ="convolution"
    lstm  ="lstm"
    all   ="transformers" 


class WMReqmode(str,Enum):
    send=1
    status=2
    download=3


print(NeuralNetwork.all)

@app.command()
def main(
        idx: Annotated[int, typer.Argument(min=0,max=1000)],
        mtime:Annotated[
                datetime,
                typer.Argument(
                    formats=[r"%Y-%m-%d", r"%Y-%m-%dT%H:%M:%S", r"%Y-%m-%d %H:%M:%S", r"%m/%d/%Y"]
                ),
            ]= datetime.now().strftime("%y-%m-%d"),
        age: Annotated[int,typer.Option('--age','-a',min=18,max=100,clamp=True)] = 20,
        verbose:Annotated[bool,typer.Option('--verbose','-V')]=False,
        force:Annotated[bool, typer.Option("--force/--no-force", "-f/-F")]=False,
        nn:Annotated[NeuralNetwork,typer.Option(case_sensitive=False)]= NeuralNetwork.all,
        mode:Annotated[WMReqmode,typer.Option('--mode','-M')] = WMReqmode.status
        
)->None:
    '''
        CLI useful for validation too

        $ python main10.py 1 --age 17
    '''
    print(f"idx::{idx} and age:: {age}")
    print(f"verbose:: {verbose}")
    print(f'force flag::{force}')
    print(f"mtime: {mtime}")
    print(f"using neural network:: {nn.value}")
    print(f"mode of call:: {mode.value}")

if __name__ == "__main__":
    app()