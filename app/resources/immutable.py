from flask import request
from flask_restful import Resource, abort
from app.connectors import ipfs, pinata
from app.utils.schema import validate_schema, format_schema
from app.connectors.aws import immutable, get_item, put_item
from app.constants import Web

class CreateImmutableSchema(Resource):
    def post(self):
        data = validate_schema()
        
        cid1 = ipfs.add_json(format_schema(data))
        cid2 = pinata.add_json(format_schema(data))
        immutable(put_item, cid1, data)

        return {
            'cid': cid1, 
            'url': Web.host + 'https://api.daostar.org/immutable/' + cid1
        }

class ViewImmutableSchema(Resource):
    def get(self, cid):
        schema = immutable(get_item, cid)
        return format_schema(schema)