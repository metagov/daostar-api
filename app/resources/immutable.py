from flask import request
from flask_restful import Resource, abort
from requests.exceptions import ConnectionError
from app.interfaces import ipfs, pinata
from app.utils import validate_json, load_schema, dump_schema
from app.interfaces.aws import immutable, get_item, put_item
from app.constants import Web
from app.validators import DaoUriSchema, InputDaoSchema

class CreateImmutableSchema(Resource):
    def post(self):
        schema = load_schema(InputDaoSchema, validate_json())
        data = schema['data']

        output = dump_schema(DaoUriSchema, data)
        
        try:
            # adds file to local node, pinata, and database
            cid1 = ipfs.add_json(output)
            cid2 = pinata.add_json(output)
            immutable(put_item, cid1, data)
        except ConnectionError:
            abort(500, message="Internal connection to IPFS network failed.")

        return {
            'cid': cid1, 
            'url': Web.host + '/immutable/' + cid1
        }

class ViewImmutableSchema(Resource):
    def get(self, cid):
        item = immutable(get_item, cid)

        if not item: abort(404, message=f'Endpoint for {cid} not found.')
        return dump_schema(DaoUriSchema, item)