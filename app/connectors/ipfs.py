import requests

base_url = "http://127.0.0.1:5001"

def add_file(file_data):
    resp = requests.post(
        url = base_url + "/api/v0/add",
        files = {"file": ("schema.json", file_data)}
    )

    if resp.ok:
        data = resp.json()
        return data['Hash']
    else:
        return False

def pin_file(hash):
    resp = requests.post(
        url = base_url + "/api/v0/pin/add",
        params = {"arg": hash}
    )

    print(resp.json())

def get_pins():
    resp = requests.post(
        url = base_url + "/api/v0/pin/ls"
    )

    if resp.ok:
        pins_dict = resp.json()
        return list(pins_dict['Keys'].keys())
    else:
        return None


def get_file(hash):
    resp = requests.post(
        url = base_url + "/api/v0/cat",
        params = {"arg": hash}
    )

    if resp.ok:
        data = resp.json()
        return data
    else:
        return False