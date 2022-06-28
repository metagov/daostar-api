import boto3
from app.constants import AWS

db = boto3.resource(
    'dynamodb',
    region_name           = AWS.REGION_NAME,
    aws_access_key_id     = AWS.ACCESS_KEY_ID,
    aws_secret_access_key = AWS.SECRET_ACCESS_KEY
)

table = db.Table('Mutable')

def get_item(key):
    response = table.get_item(
        Key = {AWS.PARTITION_KEY: key}
    )

    if 'Item' in response:
        return response['Item']
    else:
        return None

def put_item(key, item):
    if AWS.PARTITION_KEY not in item:
        item[AWS.PARTITION_KEY] = key

    response = table.put_item(
        Item = item
    )

def update_item(key):
    response = table.update_item(
        Key = {AWS.PARTITION_KEY: key},
        UpdateExpression=None,
        ExpressionAttributeValues=None
    )

def delete_item(key):
    response = table.delete_item(
        Key = {AWS.PARTITION_KEY: key},
    )