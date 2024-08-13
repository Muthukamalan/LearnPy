import os 
from dotenv import dotenv_values
from typing import Dict


from src.authenication import authenticator
from src.utils import file_format
from src.download_report import file_download
from src.gen_report import request_call
from src.status_check import status_check

assert os.path.isfile(os.path.join(os.path.dirname(__file__),'.env')), "set environmental file"
ENV:Dict = dotenv_values(os.path.join(os.path.dirname(__file__),'.env'))