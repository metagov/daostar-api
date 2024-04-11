from dotenv import load_dotenv
import os, json
from pathlib import Path

load_dotenv()


class Web:
    host              = 'https://api.daostar.org'
    cors_origins      = ['https://daostar.org', 'https://netlify.app', 'https://127.0.0.1:5501', 'http://localhost:8000']
    valid_schemes     = {'http', 'https', 'ipfs'}

class AWS:
    REGION_NAME       = 'us-east-2'
    ACCESS_KEY_ID     = os.getenv('AWS_ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    MUTABLE_TABLE     = 'Mutable'
    IMMUTABLE_TABLE   = 'Immutable'
    PARTITION_KEY     = 'id'

class IPFS:
    BASE_URL          = 'http://localhost:5001'

class Pinata:
    BASE_URL          = 'https://api.pinata.cloud'
    API_KEY           = os.getenv('PINATA_API_KEY')
    SECRET_API_KEY    = os.getenv('PINATA_SECRET_API_KEY')

class Alchemy:
    MAINNET_BASE_URL = 'https://eth-mainnet.g.alchemy.com/v2/'
    RINKEBY_BASE_URL = 'https://eth-rinkeby.alchemyapi.io/v2/'
    MAINNET_API_KEY  = os.getenv('ALCHEMY_MAINNET_API_KEY')
    RINKEBY_API_KEY  = os.getenv('ALCHEMY_RINKEBY_API_KEY')

class CAIP10:
    valid_chain_ids = {
        'eip155': [ # Ethereum
            '1',    # Mainnet
            '3',    # Ropsten
            '4',    # Rinkeby
            '5',    # Goerli
            '42',   # Kovan
            '56',   # Binance Smart Chain
            '100',  # Gnosis Chain
            '137'   # Polygon
        ]
    }

class SchemaFormat:
    context = 'https://www.daostar.org/schemas'
    type    = 'DAO'

class EIP4824:
    ABI = json.load(open(Path(__file__).parent.absolute() / 'abi.json', 'r'))
