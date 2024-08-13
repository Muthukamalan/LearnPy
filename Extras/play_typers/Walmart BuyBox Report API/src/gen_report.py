from typing import Dict
import requests
import json
import os 
from pathlib import Path

REQUEST_URL: str = r"https://marketplace.walmartapis.com/v3/reports/reportRequests?reportType=BUYBOX&requestStatus=READY&requestSubmissionStartDate=%7BdateStr%7D%22"
PARAMS: Dict = {"reportType": "BUYBOX", "reportVersion": "v1"}



def request_call(header)->bool:
    '''
        helps to call buybox report with version V1
    '''
    r = requests.post(url=REQUEST_URL, headers=header, params=PARAMS)
    report_hit = r.json()

    # Data to be written
    # Serializing json
    json_object = json.dumps(report_hit)
    # Writing to sample.json
    with open("./assets/report.json", "w") as outfile:
        outfile.write(json_object)
    return f"{report_hit.get('requestId')}"
