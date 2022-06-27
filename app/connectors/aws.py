import boto3
from app.constants import AWS

db = boto3.resource(
    'dynamodb',
    region_name           = AWS.REGION_NAME,
    aws_access_key_id     = AWS.ACCESS_KEY_ID,
    aws_secret_access_key = AWS.SECRET_ACCESS_KEY
)

mutable = db.Table('Mutable')