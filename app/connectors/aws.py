import boto3
import os
from dotenv import load_dotenv

load_dotenv()

REGION_NAME = os.getenv('REGION_NAME')
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

db = boto3.resource(
    'dynamodb',
    region_name=REGION_NAME,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY)

mutable = db.Table('Mutable')