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
from app.constants import CAIP10, Web
from app.resources.daodao import fetch_juno_daos, fetch_osmosis_daos, fetch_stargaze_daos

main = Flask('DAOstar API')
api = Api(main)
cors = CORS(main, origins=Web.cors_origins)

@main.errorhandler(404)
def resource_not_found(e):
    return {'message': 'Resource not found.'}, 404

@main.route('/')
def landing_page():
    return {'message': 'API service for DAOstar, access via https://daostar.org/api or view documentation at https://daostar.org/api/docs'}, 200

@main.route('/chains')
def get_chains():
    return CAIP10.valid_chain_ids
# New routes to fetch DAODAO DAO's securly
@main.route('/fetch_juno_daos', methods=['GET'])
def get_juno_daos():
    return fetch_juno_daos()

@main.route('/fetch_osmosis_daos', methods=['GET'])
def get_osmosis_daos():
    return fetch_osmosis_daos()

@main.route('/fetch_stargaze_daos', methods=['GET'])
def get_stargaze_daos():
    return fetch_stargaze_daos()


api.add_resource(CreateMutableSchema, '/mutable', '/mutable/')
api.add_resource(InteractMutableSchema, '/mutable/<caip>')
# api.add_resource(Members, '/mutable/<caip>/members')
# api.add_resource(Proposals, '/mutable/<caip>/proposals')
# api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
# api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(CreateImmutableSchema, '/immutable', '/immutable/')
api.add_resource(ViewImmutableSchema, '/immutable/<cid>')
# api.add_resource(ResolveSchema, '/resolve/<caip>')