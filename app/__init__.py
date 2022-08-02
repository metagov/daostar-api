from flask import Flask, Response
from flask_restful import Api
from flask_cors import CORS
from app.resources import (
    CreateMutableSchema,
    InteractMutableSchema,
    CreateImmutableSchema,
    ViewImmutableSchema,
    ResolveSchema
)
from app.constants import CAIP10

main = Flask('DAOstar API')
api = Api(main)
cors = CORS(main, origins=['https://daostar.org'])

@main.errorhandler(404)
def resource_not_found(e):
    return {'message': 'Resource not found.'}, 404

@main.route('/')
def landing_page():
    return {'message': 'API service for DAOstar, access via https://daostar.org/api or view documentation at https://daostar.org/api/docs'}, 200

@main.route('/chains')
def get_chains():
    return CAIP10.valid_chain_ids

api.add_resource(CreateMutableSchema, '/mutable', '/mutable/')
api.add_resource(InteractMutableSchema, '/mutable/<caip>')
# api.add_resource(Members, '/mutable/<caip>/members')
# api.add_resource(Proposals, '/mutable/<caip>/proposals')
# api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
# api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(CreateImmutableSchema, '/immutable', '/immutable/')
api.add_resource(ViewImmutableSchema, '/immutable/<cid>')
# api.add_resource(ResolveSchema, '/resolve/<caip>')