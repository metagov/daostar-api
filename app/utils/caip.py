from web3 import Web3
from app.constants import CAIP10
from flask_restful import abort

def validate_caip(account_id):
    namespace, reference, account_address = account_id.split(':')

    if namespace not in CAIP10.valid_chain_ids:
        abort(400, message='Invalid namepace')
    if reference not in CAIP10.valid_chain_ids[namespace]:
        abort(400, message='Invalid namespace reference')
    if not Web3.isAddress(account_address):
        abort(400, message='Invalid address')