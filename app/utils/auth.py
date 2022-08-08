from flask import request
from flask_restful import abort
from web3.auto import w3
from eth_account.messages import defunct_hash_message
from hexbytes import HexBytes
from app.constants import Auth
from app.interfaces.aws import *

def validate_signature(signature_string, message):
    hash_message = defunct_hash_message(text=message)
    signature = HexBytes(signature_string)

    address = w3.eth.account.recoverHash(hash_message, signature=signature)
    return address

def authorize(caip):
    item = mutable(get_item, caip)
    if 'protected' not in item: return
    if not item['protected']: return

    api_key = request.headers.get(Auth.API_KEY_HEADER)
    if not api_key: abort(401, message=f"Authorization required, request should include '{Auth.API_KEY_HEADER}' header.")

    # retrieving authorization data from Admin db table
    auth = admin(get_item, api_key)
    if not auth: abort(403, message="Authorization failed, invalid API key.")
    if auth['caip'] != caip: abort(403, message="Authorization failed, invalid API key.")
