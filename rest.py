from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import ipfs
import json
import aws
import pdb

app = Flask(__name__)
api = Api(app)

schema_parser = reqparse.RequestParser()
schema_parser.add_argument("name", required=True)
schema_parser.add_argument("description")
schema_parser.add_argument("membersURI")
schema_parser.add_argument("proposalsURI")
schema_parser.add_argument("activityLogURI")
schema_parser.add_argument("governanceURI")

class Immutable(Resource):
    def get(self, cid):
        schema = ipfs.get_file(cid)
        return schema, 200

    def post(self):
        parser = schema_parser.copy()
        params = parser.parse_args()

        cid = ipfs.add_file(json.dumps(params, indent=2))

        return {"cid": cid}, 200

class Mutable(Resource):
    def get(self, caip):
        return aws.mutable.get_item(
            Key = {'id': caip}
        )['Item']

    def post(self, caip):
        parser = schema_parser.copy()
        params = parser.parse_args()

        aws.mutable.put_item(
            Item = params | {'id': caip}
        )

        return caip

    def put(self, caip):
        exp = "SET "
        schema = request.json
        update_schema = {}

        for k in schema.keys():
            exp += f"{k} = :{k}"
            update_schema[":" + k] = schema[k]

        print(schema)
        print(exp)


        aws.mutable.update_item(
            Key = {'id': caip},
            UpdateExpression=exp,
            ExpressionAttributeValues=update_schema
        )

    def delete(self, caip):
        aws.mutable.delete_item(
            Key = {'id': caip}
        )

class Members(Resource):
    pass

class Proposals(Resource):
    pass

class ActivityLog(Resource):
    pass

class Resolve(Resource):
    def get(self, caip):
        pass

api.add_resource(Immutable, "/immutable", "/immutable/", "/immutable/<cid>")
api.add_resource(Mutable, "/mutable", "/mutable/", "/mutable/<caip>")
api.add_resource(Resolve, "/resolve/<caip>")

app.run()
