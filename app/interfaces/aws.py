import boto3
from app.constants import AWS

db = boto3.resource(
    'dynamodb',
    region_name           = AWS.REGION_NAME,
    aws_access_key_id     = AWS.ACCESS_KEY_ID,
    aws_secret_access_key = AWS.SECRET_ACCESS_KEY
)

mutable_table = db.Table(AWS.MUTABLE_TABLE)
immutable_table = db.Table(AWS.IMMUTABLE_TABLE)
admin_table = db.Table(AWS.ADMIN_TABLE)

# wrappers for mutable and immutable tables, easier syntax for db operations
# ex: mutable(put_item, caip, data)
def mutable(func, *args, **kwargs):
    return func(mutable_table, AWS.DATA_PART_KEY, *args, **kwargs)

def immutable(func, *args, **kwargs):
    return func(immutable_table, AWS.DATA_PART_KEY, *args, **kwargs)

def admin(func, *args, **kwargs):
    return func(admin_table, AWS.ADMIN_PART_KEY, *args, **kwargs)

# retrieves an item from a table
def get_item(table, partition_key, key):
    response = table.get_item(
        Key = {partition_key: key}
    )

    return response.get('Item')

# queries an item by a secondary index
def query_item(table, partition_key, query_key, key):
    response = table.query(
        IndexName = "caip-index",
        ExpressionAttributeValues={
            ":v1": key
        },
        KeyConditionExpression=f"{query_key} = :v1"
    )
    return response

# inserts an item into a table
def put_item(table, partition_key, key, item):
    # if partition_key not in item:
    item[partition_key] = key

    response = table.put_item(
        Item = item
    )

# updates existing table item by replacing or adding key value pairs
def update_item(table, partition_key, key, item):
    expression = 'SET '
    attribute_values = {}
    attribute_names = {}

    # generates update expression, formatted as
    # SET value1 = :val1, value2 = :val2
    for c, k in enumerate(item.keys()):
        sub_exp = f'{k} = :{k}'
        # 'name' is a reserved keyword, so an alias must be used
        if k == 'name':
            sub_exp = '#N = :name'
            attribute_names = {'#N': 'name'}
        expression += sub_exp
        if c < len(item.keys()) -1: expression += ', '
        attribute_values[':' + k] = item[k]

    params = {
        'UpdateExpression': expression,
        'ExpressionAttributeNames': attribute_names,
        'ExpressionAttributeValues': attribute_values,
        'ReturnValues': 'ALL_NEW'
    }

    if not attribute_names: del params['ExpressionAttributeNames']

    response = table.update_item(
        Key = {partition_key: key},
        **params
    )

    return response.get('Attributes')

# removes an item from a table
def delete_item(table, partition_key, key):
    response = table.delete_item(
        Key = {partition_key: key},
    )