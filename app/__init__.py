from flask import Flask, Response
from flask_restful import Api
from flask_cors import CORS
from app.resources.mutable import CreateMutableSchema, InteractMutableSchema
from app.resources.immutable import CreateImmutableSchema, ViewImmutableSchema
from app.resources.resolve import ResolveSchema

main = Flask('DAOstar API')
api = Api(main)
cors = CORS(main, origins=['http://localho.st:5000', 'https://daostar.org'])

@main.errorhandler(404)
def resource_not_found(e):
    return {'message': '404: not found'}, 404

@main.route('/')
def landing_page():
    return {'message': 'API service for DAOstar, access via https://daostar.org/query'}, 200

api.add_resource(CreateMutableSchema, '/mutable', '/mutable/')
api.add_resource(InteractMutableSchema, '/mutable/<caip>')
# api.add_resource(Members, '/mutable/<caip>/members')
# api.add_resource(Proposals, '/mutable/<caip>/proposals')
# api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
# api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(CreateImmutableSchema, '/immutable', '/immutable/')
api.add_resource(ViewImmutableSchema, '/immutable/<cid>')
api.add_resource(ResolveSchema, '/resolve/<caip>')