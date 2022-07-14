from flask import request
from flask_restful import Resource, abort
from app.interfaces.aws import mutable, get_item, put_item, update_item, delete_item
from app.utils import validate_json, load_schema, dump_schema, validate_caip
from app.constants import Web
from app.validators import DaoSchema, MutableDaoSchema

class CreateMutableSchema(Resource):
    def post(self):
        schema = load_schema(MutableDaoSchema, validate_json())
        caip = schema['caip']
        data = schema['data']

        # don't overwrite existing schema
        if mutable(get_item, caip): abort(409, message=f'{caip} already exists')
            
        mutable(put_item, caip, data)

        return {
            'url': Web.host + '/mutable/' + caip
        }

class InteractMutableSchema(Resource):
    def get(self, caip):
        validate_caip(caip)
        item = mutable(get_item, caip)

        if not item: abort(404, message=f'{caip} not found')
        return dump_schema(DaoSchema, item)

    def put(self, caip):
        validate_caip(caip)
        data = validate_json()

        item = mutable(update_item, caip, data)
        return dump_schema(DaoSchema, item)

    def delete(self, caip):
        validate_caip(caip)
        mutable(delete_item, caip)

        return None, 204

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