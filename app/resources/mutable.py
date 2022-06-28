from flask import request
from flask_restful import Resource, abort
from app.connectors import aws
from app.utils.schema import format_schema, validate_schema

class MutableSchema(Resource):
    def get(self, caip):
        item = aws.get_item(caip)

        if item:
            return format_schema(item)
        else:
            abort(404, message=f'{caip} not found')

    def post(self, caip):
        data = validate_schema()
        # don't overwrite existing schema
        if aws.get_item(caip):
            abort(409, message=f'{caip} already exists')
            
        aws.put_item(caip, data)
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
        aws.delete_item(caip)

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