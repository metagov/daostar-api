from flask import request
from flask_restful import Resource, abort
from app.connectors import ipfs, pinata
from app.utils.schema import validate_schema, format_schema
from app.connectors.aws import immutable, get_item, put_item

class ImmutableSchema(Resource):
    def get(self, cid):
        schema = immutable(get_item, cid)
        return format_schema(schema)

    def post(self):
        data = validate_schema()

        cid1 = ipfs.add_json(format_schema(data))
        cid2 = pinata.add_json(format_schema(data))
        immutable(put_item, cid2, data)

        return {'id': cid2}