from typing import OrderedDict,Dict,AnyStr

from requests import auth
import requests
from requests.auth import HTTPBasicAuth
from base64 import b64encode
import base64
import json
import uuid
from functools import wraps

#TODO: xcption
def authenticate(
    Clientid:AnyStr,
    Client_Secret:AnyStr,
) -> Dict:
    '''
        helps to authenicate and returns new headers to call for
        - input:
            - client_id:        
            - clinet_secret:
        - output:<hash map>
            {
                "requestId": ID,  
                "requestStatus": "RECEIVED"/"INPROGRESS"/"READY", 
                "requestSubmissionDate": date, 
                "reportType": "BUYBOX", 
                "reportVersion": "v1"
            }
        '''
    guid = uuid.uuid4().hex
    API_URL = "https://marketplace.walmartapis.com/v3/token"
    PAYLOAD = {"grant_type": "client_credentials"}
    credentials = f"{Clientid}:{Client_Secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "WM_QOS.CORRELATION_ID": f"{guid}",
        "WM_SVC.NAME": "WalmartMarketplace",
    }
    # headers
    # Make the POST request
    response = requests.post(url=API_URL, headers=headers, data=PAYLOAD)
    # print(response)
    val = response.json()
    # print(val)
    access_token = val["access_token"]
    return {
        "Authorization": f"Basic {encoded_credentials}",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "WM_QOS.CORRELATION_ID": f"{guid}",
        "WM_SVC.NAME": "WalmartMarketplace",
        "WM_SEC.ACCESS_TOKEN": f"{access_token}",
    }



def authenticator(client_id: str, client_secret: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            headers = authenticate(Clientid=client_id, Client_Secret=client_secret)
            return func(*args, **kwargs, header=headers)
        return wrapper
    return decorator

