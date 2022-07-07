from flask import Flask, Response
from flask_restful import Api
from flask_cors import CORS
from app.resources.mutable import MutableSchema, Members, Proposals, ActivityLog, Governance
from app.resources.immutable import ImmutableSchema
from app.resources.resolve import ResolveSchema

main = Flask('DAOstar API')
api = Api(main)
cors = CORS(main, origins=['http://127.0.0.1:5000', 'https://daostar.org'])

@main.errorhandler(404)
def resource_not_found(e):
    return {'message': '404: not found'}, 404

api.add_resource(MutableSchema, '/mutable', '/mutable/', '/mutable/<caip>')
# api.add_resource(Members, '/mutable/<caip>/members')
# api.add_resource(Proposals, '/mutable/<caip>/proposals')
# api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
# api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(ImmutableSchema, '/immutable', '/immutable/', '/immutable/<cid>')
api.add_resource(ResolveSchema, '/resolve/<caip>')