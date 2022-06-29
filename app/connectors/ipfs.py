import requests
import json
from app.constants import IPFS

def add_file(file_data):
    resp = requests.post(
        url = IPFS.BASE_URL + "/api/v0/add",
        files = {"file": ("data.txt", file_data)}
    )

    if resp.ok:
        resp_data = resp.json()
        return resp_data['Hash']
    else:
        return None

def add_json(json_data):
    # converts to dictionary to minified json
    text = json.dumps(json_data, separators=(',', ':'))
    return add_file(text)

def pin_file(hash):
    resp = requests.post(
        url = IPFS.BASE_URL + "/api/v0/pin/add",
        params = {"arg": hash}
    )

def get_pins():
    resp = requests.post(
        url = IPFS.BASE_URL + "/api/v0/pin/ls"
    )

    if resp.ok:
        pins_dict = resp.json()
        return list(pins_dict['Keys'].keys())
    else:
        return None


def get_file(hash, timeout):
    resp = requests.post(
        url = IPFS.BASE_URL + "/api/v0/cat",
        params = {"arg": hash},
        timeout=timeout
    )

    if resp.ok:
        data = resp.json()
        return data
    else:
        return False