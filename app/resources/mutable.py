from flask import request
from flask_restful import Resource, abort
from app.connectors.aws import mutable, get_item, put_item, update_item, delete_item
from app.utils.schema import validate_json, validate_schema, format_schema
from app.utils.caip import validate_caip

class MutableSchema(Resource):
    def get(self, caip):
        validate_caip(caip)
        item = mutable(get_item, caip)

        if item:
            return format_schema(item)
        else:
            abort(404, message=f'{caip} not found')

    def post(self, caip):
        validate_caip(caip)
        data = validate_schema()
        # don't overwrite existing schema
        if mutable(get_item, caip):
            abort(409, message=f'{caip} already exists')
            
        mutable(put_item, caip, data)
        return caip

    def put(self, caip):
        validate_caip(caip)
        data = validate_json()

        item = mutable(update_item, caip, data)
        return format_schema(item)

    def delete(self, caip):
        validate_caip(caip)
        mutable(delete_item, caip)

        return {'success': True}

class Members(Resource):
    def get(self, caip):
        response = mutable(
            get_item,
            Key = {'id': caip}
        )

        if 'Item' in response:
            return {'members': response['Item']['membersURI']}
        else:
            abort(404, message=f'{caip} does not exist')

class Proposals(Resource): ...

class ActivityLog(Resource): ...

class Governance(Resource): ...