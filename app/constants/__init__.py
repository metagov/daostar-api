from dotenv import load_dotenv
import os

load_dotenv()

class Pinata:
    API_KEY           = os.getenv('PINATA_API_KEY'),
    SECRET_API_KEY    = os.getenv('PINATA_SECRET_API_KEY')

class AWS:
    REGION_NAME       = os.getenv('AWS_REGION_NAME')
    ACCESS_KEY_ID     = os.getenv('AWS_ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')