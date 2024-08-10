from pathlib import Path 
from typing import Optional

import typer 
from typing_extensions import Annotated


app = typer.Typer()

@app.command()
def exec(config:Annotated[Optional[Path], typer.Option()]=None)->None:
    if config is None:
        print("no config file")
        raise typer.Abort()                        # Abort, Exit and assert [difference](https://www.geeksforgeeks.org/c-exit-abort-and-assert-functions/)
    if config.is_file():
        text = config.read_text()
        print(f'config file content:: {text}')
    if config.is_dir():
        print('config is a directory')
    elif not config.exists():
        print("config not exists")


if __name__=='__main__':
    app()


'''
abort:: abort() may not close files that are open. It may also not delete temporary files and may not flush the stream buffer.
exit::  exit() close the files, clear temp files, flush the stream buffer.
assert:: unit test /debug purpose/

'''