import os
import json
import requests
from pathlib import Path
from typing import Tuple

def status_check(header:dict)->Tuple[str,bool]:
    pathway:str = os.path.join(Path.cwd(),'assets','report.json')
    assert os.path.isfile(pathway),"json artifact not found!!"

    with open(pathway, "r") as openfile:
        json_object:dict = json.load(openfile)
    request_id = json_object.get("requestId")

    # request_id = ''
    url_status = f"https://marketplace.walmartapis.com/v3/reports/reportRequests/{request_id}"
    res = requests.get(url=url_status, headers=header)
    
    res_json = res.json()
    print(res_json)

    if res.status_code==200 and res_json.get('requestStatus','OTHERS')=='READY':
        json_object['requestStatus']='READY'
        with open(pathway, "w") as openfile:
            json.dump(json_object, openfile, indent=4)
        return (request_id,True)
    
    return (request_id,False)
    
