from flask import request
from flask_restful import abort

def validate_item(schema, item, required=False, limit=None, default=None):
    if item in schema:
        ...
    else:
        if required:
            abort(400, message="'name' is a required field")
        else:
            schema[item] = None

def validate_json():
    data = request.get_json(force=True, silent=True)
    if not data: abort(400, message='Could not understand request')
    return data

def validate_schema(schema):
    if not type(schema) == dict: abort(400, message='data field should be of type dict')
    validate_item(schema, 'name', required=True)
    validate_item(schema, 'description')
    validate_item(schema, 'membersURI')
    validate_item(schema, 'proposalsURI')
    validate_item(schema, 'activityLogURI')
    validate_item(schema, 'governanceURI')

    return schema

def format_schema(data):
    key_order = ['name', 'description', 'membersURI', 'proposalsURI', 'activityLogURI', 'governanceURI']
    formatted_schema = {
        '@context': 'https://daostar.org/schemas',
        'type': 'DAO'
    }
    for k in key_order:
        formatted_schema[k] = data[k]
        
    return formatted_schema