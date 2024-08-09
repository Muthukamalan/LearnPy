import typer 
from typing import Optional

app = typer.Typer()

@app.command(name="rup")
def request_generator(req_name:str)->None:
    '''
        It's me `request_generator` docstring.
        `$ python main2.py rup --help`to see me again
    '''
    print(f"your request `{req_name}` sent successfully!")

@app.command(name="rdown")
def request_download(id:int,*,format:Optional[str]='csv')->None:
    if format=='csv':
        print(f"your request processed with ID:{id} and formated by csv")
    else:
        print(f"your request processed with ID:{id} and formated by {format}")


if __name__=='__main__':
    app()


# @app.command is not found >> RuntimeError: Could not get a command for this Typer instance
# python main2.py --help
# python main2.py rup marksheet
# python main2.py rdown 20                            # *INT required
# python main2.py rdown 100 --format json             # **format  flags options




# CLI Option
# -- prepended to the name

# In LINUX,
# ls --time `atime|ctime|mtime|birth` ~/GitHub
# `ls` >>  command-app or CLI app
# `--time` >> flag  can use options from `atime|ctime|mtime|birth`   (order not neccessary)
# `~/GitHub` folder path



# A CLI argument is required
# A CLI option is optional
## python main2.py rdown 100 --format json   >> `100 argument` && `json option`

## the main and most important difference is that:
# - CLI options start with `--` and don't depend on the order
# - CLI arguments depend on the sequence order