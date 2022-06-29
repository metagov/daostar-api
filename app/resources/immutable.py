from flask import request
from flask_restful import Resource, abort
import json
from app.connectors import ipfs, pinata
from app.utils.schema import validate_schema
from app.connectors.aws import immutable, get_item, put_item

class ImmutableSchema(Resource):
    def get(self, cid):
        schema = ipfs.get_file(cid)
        return schema, 200

    def post(self):
        data = validate_schema()

        cid1 = ipfs.add_json(data)
        cid2 = pinata.add_json(data)

        return {'id': cid2}