from web3.auto import w3
from eth_account.messages import defunct_hash_message
from hexbytes import HexBytes

def validate_signature(signature_string, message):
    hash_message = defunct_hash_message(text=message)
    signature = HexBytes(signature_string)

    address = w3.eth.account.recoverHash(hash_message, signature=signature)
    return address