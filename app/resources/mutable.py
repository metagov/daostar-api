from flask import request
from flask_restful import Resource, abort
from app.connectors import aws

def validate_item(schema, item, required=False, limit=None, default=None):
    if item in schema:
        ...
    else:
        if required:
            abort(400, message="'name' is a required field")
        else:
            schema[item] = None

def validate_schema():
    schema = request.get_json(force=True, silent=True)
    if not schema: abort(400, message='Could not understand request')

    validate_item(schema, 'name', required=True)
    validate_item(schema, 'description')
    validate_item(schema, 'membersURI')
    validate_item(schema, 'proposalsURI')
    validate_item(schema, 'activityLogURI')
    validate_item(schema, 'governanceURI')

    return schema

def order_schema(data):
    key_order = ['name', 'description', 'membersURI', 'proposalsURI', 'activityLogURI', 'governanceURI']
    ordered_schema = {}
    for k in key_order:
        ordered_schema[k] = data[k]
    return ordered_schema

class MutableSchema(Resource):
    def get(self, caip):
        response = aws.mutable.get_item(
            Key = {'id': caip}
        )

        if 'Item' in response:
            return order_schema(response['Item'])
        else:
            abort(404, message=f'{caip} does not exist')

    def post(self, caip):
        data = validate_schema()

        print(data)

        response = aws.mutable.put_item(
            Item = data | {'id': caip}
        )

        print(response)

        return caip

    def put(self, caip):
        exp = 'SET '
        schema = request.json
        update_schema = {}

        for k in schema.keys():
            exp += f'{k} = :{k}'
            update_schema[':' + k] = schema[k]

        print(schema)
        print(exp)


        aws.mutable.update_item(
            Key = {'id': caip},
            UpdateExpression=exp,
            ExpressionAttributeValues=update_schema
        )

    def delete(self, caip):
        aws.mutable.delete_item(
            Key = {'id': caip}
        )

        return {'success': True}

class Members(Resource):
    def get(self, caip):
        response = aws.mutable.get_item(
            Key = {'id': caip}
        )

        if 'Item' in response:
            return {'members': response['Item']['membersURI']}
        else:
            abort(404, message=f'{caip} does not exist')

class Proposals(Resource): ...

class ActivityLog(Resource): ...

class Governance(Resource): ...