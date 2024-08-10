
'''
Like, in previous example,
git
|_ push
|    |_ remote_name  
|    |_ --tags, --all
|_ branch
|    |_ branch_name
|    |_ -v
|
'''

# TODO: learn @app.callback() works


import typer

app = typer.Typer()
state = {
    'verbose':False
}

@app.callback()
def main(verbose:bool=False):
    print('print callback')
    if verbose:
        state['verbose']=verbose

@app.callback()
def seed_():
    print('Override seed!!')
    

@app.command()
def create(usr_name:str):
    if state['verbose']:
        print(f"User create with id:{1} and name:{usr_name}")
    print('create operation done!')


@app.command()
def delete(usr_name:str):
    if state['verbose']:
        print(f"Delete create with id:{100} and name:{usr_name}")
    print('delete opeartion done!')



if __name__=="__main__":
    app()