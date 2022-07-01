from flask_restful import Resource, abort
from app.utils.caip import validate_caip
from web3 import Web3, HTTPProvider
from app.connectors.ipfs import get_file
from app.constants import Alchemy, EIP4824
from urllib.parse import urlparse
import requests

class ResolveSchema(Resource):
    def get(self, caip):
        namespace, reference, account_address = validate_caip(caip)

        if reference == '1':
            url = Alchemy.MAINNET_BASE_URL + Alchemy.MAINNET_API_KEY
        elif reference == '4':
            url = Alchemy.RINKEBY_BASE_URL + Alchemy.RINKEBY_API_KEY
        else:
            abort(400, message="Unsupported chain")
        
        web3 = Web3(HTTPProvider(url))

        contract = web3.eth.contract(address=account_address, abi=EIP4824.ABI)

        URI = contract.functions.daoURI().call()
        o = urlparse(URI)

        if o.scheme == 'ipfs':
            return get_file(o.netloc)

        elif o.scheme == 'http':
            return requests.get(URI)