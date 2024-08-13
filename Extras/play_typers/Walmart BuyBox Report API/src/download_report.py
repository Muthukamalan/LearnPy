import os 
import requests
import json 
import pandas as  pd 
from pathlib import Path
from src.utils import file_format


#TODO: xcption
def file_download(header,*,today):
    '''
        help to download file from url.
    '''
    URL_DOWNLOAD:str = r"https://marketplace.walmartapis.com/v3/reports/downloadReport"
    DOWNLOAD_PATH:str= os.path.join(os.getcwd(), 'reports', f'{today}')
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    with open(os.path.join(Path.cwd(),'assets','report.json'),'r') as f:
        status = json.load(f)
    request_id = status['requestId']
    
    params = {"requestId": request_id}
    report = requests.get(url=URL_DOWNLOAD, headers=header, params=params)
    download_url = report.json()
    link = download_url['downloadURL']

    df = pd.read_csv(link, compression='zip')

    file_names = os.path.join(Path.cwd(), 'reports', f'{today}', f'buybox.csv')
    df.drop_duplicates().dropna(axis=0).astype({
        'Sku': 'string',
        'Item ID': 'int64',
        'Product Name': 'string',
        'Product Category': 'string',
        'Seller Item Price': 'float64',
        'Seller Ship Price': 'float64',
        'IsSellerBuyBoxWinner': 'string',
        'Buybox Item Price': 'float64',
        'Buybox Ship Price': 'float64'
    }).to_csv(file_names, index=False, lineterminator="\n")
    
    if len(os.listdir(DOWNLOAD_PATH))==1:
        return (request_id,True)
    
    return (request_id,False)