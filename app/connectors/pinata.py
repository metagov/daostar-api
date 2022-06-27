import requests
from app.constants import Pinata

url = "https://api.pinata.cloud/pinning/pinJSOnToIPFS"

headers = {
    "pinata_api_key":        Pinata.API_KEY,
    "pinata_secret_api_key": Pinata.SECRET_API_KEY
}

def pin_file(data, name=None):
    payload = {
        "pinataOptions": {
            "cidVersion": 1
        },
        "pinataContent": data
    }

    resp = requests.post(
        url=url,
        headers=headers,
        json=payload
    )

    return resp.json()