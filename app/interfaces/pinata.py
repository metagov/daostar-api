import requests
import json
from app.constants import Pinata

headers = {
    "pinata_api_key":        Pinata.API_KEY,
    "pinata_secret_api_key": Pinata.SECRET_API_KEY
}

def add_file(file_data):
    resp = requests.post(
        url = Pinata.BASE_URL + '/pinning/pinFileToIPFS',
        headers=headers,
        files = {'file': ('data.txt', file_data)}
    )

    if resp.ok:
        resp_data = resp.json()
        return resp_data['IpfsHash']
    else:
        return None

def add_json(json_data):
    # converts to dictionary to minified json
    text = json.dumps(json_data, separators=(',', ':'))
    return add_file(text)