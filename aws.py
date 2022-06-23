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

# response = table.put_item(
#     Item = {
#         'id': 'eip155:4:0x000000000000000000000000000000000000dead',
#         'chain_id': 'eip155:4',
#         'account_address': '0x000000000000000000000000000000000000dead',
#         'name': 'Null Address',
#         'description': 'Commonly used vanity address to burn tokens.',
#         'membersURI': 'https://discord.com',
#         'proposalsURI': 'https://drive.google.com',
#         'activityLogURI': '',
#         'governanceURI': 'Anarchy.'
#     }
# )

# print(response)

# response = table.get_item(
#     Key = {'id': 'eip155:4:0x000000000000000000000000000000000000dead'}
# )

# print(response)

# response = table.update_item(
#     Key = {'id': 'eip155:4:0x000000000000000000000000000000000000dead'},
#     UpdateExpression='',
#     ExpressionAttributeValues={

#     }
# )