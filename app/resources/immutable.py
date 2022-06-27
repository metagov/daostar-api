from flask import request
from flask_restful import Resource, abort
import json
from app.connectors import ipfs

class ImmutableSchema(Resource):
    def get(self, cid):
        schema = ipfs.get_file(cid)
        return schema, 200

    def post(self):
        parser = schema_parser.copy()
        params = parser.parse_args()

        cid = ipfs.add_file(json.dumps(params, indent=2))

        return {'cid': cid}, 200