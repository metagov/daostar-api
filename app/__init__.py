from flask import Flask
from flask_restful import Api
from app.resources.mutable import MutableSchema, Members, Proposals, ActivityLog
from app.resources.immutable import ImmutableSchema
from app.resources.resolve import Resolve

flask_app = Flask('DAOstar API')
api = Api(flask_app)

api.add_resource(MutableSchema, '/mutable', '/mutable/', '/mutable/<caip>')
api.add_resource(ImmutableSchema, '/immutable', '/immutable/', '/immutable/<cid>')
api.add_resource(Resolve, '/resolve/<caip>')
