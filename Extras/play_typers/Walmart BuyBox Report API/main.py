import os 
from typing import OrderedDict,List,Optional
from datetime import date,timedelta
import logging
from rich import print
import typer
from typer import Typer
from typing_extensions import Annotated
from pathlib import Path

from src import (
    authenticator,
    request_call,
    file_download,
    status_check,
    ENV as CONFIG
)


TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
DATE:str  = TODAY.strftime(r"%m_%d_%Y")

PROJECT_PATH:str = os.path.dirname(__file__)

# make_dirs
os.makedirs( os.path.join(PROJECT_PATH,'logfile'), exist_ok= True )
os.makedirs( os.path.join(PROJECT_PATH,"reports"), exist_ok=True )
os.makedirs( os.path.join(PROJECT_PATH,'assets'),  exist_ok=True )

# logging
logging.basicConfig( filename= os.path.join(os.getcwd(), 'logfile', f'logs.log'), format='%(asctime)s %(message)s', filemode='a' )
logger = logging.getLogger()
logger.setLevel(logging.INFO) #<< mode


app = typer.Typer(help='CLI-APP 🖥️</> for Walmart BuyBox',no_args_is_help=True)

@app.command("request",help='buybox-report requested to walmart')
def _():
    r_call = authenticator(client_id=CONFIG.get('CLIENT_ID',None), client_secret=CONFIG.get('CLIENT_SECRET',None))(request_call)
    try:
        report_id = r_call()
        logger.info(msg=f'request sent 📨 with report id:: {report_id}')
    except Exception as e:
        ...


@app.command('status',help="check status for requested report")
def _():
    s_call = authenticator(client_id=CONFIG.get('CLIENT_ID',None), client_secret=CONFIG.get('CLIENT_SECRET',None))(status_check) 
    report_id,current_status = s_call()
    logger.info(msg=f'status 📤 check for report id : {report_id} and download availability {current_status}')


@app.command('download',help="send a download report")
def _():
    d_call = authenticator(client_id=CONFIG.get('CLIENT_ID',None), client_secret=CONFIG.get('CLIENT_SECRET',None))(file_download) 
    report_id, is_downloaded = d_call(today=TODAY)
    logger.info(msg=f"download request for {report_id} is {'DONE ☑️' if is_downloaded else 'Not Yet Downloaded ⏳'}")




if __name__=='__main__':
    app()