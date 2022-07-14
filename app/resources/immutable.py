from flask import request
from flask_restful import Resource, abort
from app.interfaces import ipfs, pinata
from app.utils import validate_json, load_schema, dump_schema
from app.interfaces.aws import immutable, get_item, put_item
from app.constants import Web
from app.validators import DaoSchema, ImmutableDaoSchema

class CreateImmutableSchema(Resource):
    def post(self):
        schema = load_schema(ImmutableDaoSchema, validate_json())
        data = schema['data']

        output = dump_schema(DaoSchema, data)

        cid1 = ipfs.add_json(output)
        cid2 = pinata.add_json(output)
        immutable(put_item, cid1, data)

        return {
            'cid': cid1, 
            'url': Web.host + 'https://api.daostar.org/immutable/' + cid1
        }

class ViewImmutableSchema(Resource):
    def get(self, cid):
        item = immutable(get_item, cid)
        return dump_schema(DaoSchema, item)