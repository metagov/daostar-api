from dotenv import load_dotenv
import os

load_dotenv()

class AWS:
    REGION_NAME       = os.getenv('AWS_REGION_NAME')
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

class CAIP10:
    valid_chain_ids = {
        'eip155': [ # Ethereum
            '1',    # Mainnet
            '3',    # Ropsten
            '4',    # Rinkeby
            '5',    # Goerli
            '42'    # Kovan
        ]
    }