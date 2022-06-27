from flask import Flask
from flask_restful import Api
from app.resources.mutable import MutableSchema, Members, Proposals, ActivityLog, Governance
from app.resources.immutable import ImmutableSchema
from app.resources.resolve import ResolveSchema

flask_app = Flask('DAOstar API')
api = Api(flask_app)

api.add_resource(MutableSchema, '/mutable', '/mutable/', '/mutable/<caip>')
api.add_resource(Members, '/mutable/<caip>/members')
api.add_resource(Proposals, '/mutable/<caip>/proposals')
api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(ImmutableSchema, '/immutable', '/immutable/', '/immutable/<cid>')
api.add_resource(ResolveSchema, '/resolve/<caip>')