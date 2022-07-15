from flask import request
from flask_restful import Resource, abort
from app.interfaces.aws import mutable, get_item, put_item, update_item, delete_item
from app.utils import validate_json, load_schema, dump_schema, validate_caip
from app.constants import Web
from app.validators import DaoSchema, InputCaipWithDaoSchema, InputDaoSchema

class CreateMutableSchema(Resource):
    def post(self):
        schema = load_schema(InputCaipWithDaoSchema, validate_json())
        caip = schema['caip']
        data = schema['data']

        # don't overwrite existing schema
        if mutable(get_item, caip): abort(409, message=f'Endpoint for {caip} already exists.')

        mutable(put_item, caip, data)

        return {
            'url': Web.host + '/mutable/' + caip
        }

class InteractMutableSchema(Resource):
    def get(self, caip):
        validate_caip(caip)
        item = mutable(get_item, caip)

        if not item: abort(404, message=f'Endpoint for {caip} not found.')
        return dump_schema(DaoSchema, item)

    def put(self, caip):
        validate_caip(caip)
        schema = load_schema(InputDaoSchema, validate_json())
        data = schema['data']

        item = mutable(update_item, caip, data)
        return dump_schema(DaoSchema, item)

    def delete(self, caip):
        validate_caip(caip)
        mutable(delete_item, caip)

        return None, 204

class Members(Resource): ...

class Proposals(Resource): ...

class ActivityLog(Resource): ...

class Governance(Resource): ...