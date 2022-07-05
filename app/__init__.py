from flask import Flask, Response
from flask_restful import Api
from flask_cors import CORS
from app.resources.mutable import MutableSchema, Members, Proposals, ActivityLog, Governance
from app.resources.immutable import ImmutableSchema
from app.resources.resolve import ResolveSchema

flask_app = Flask('DAOstar API')
api = Api(flask_app)
cors = CORS(flask_app, origins=["http://127.0.0.1:5500", "https://daostar.org"])

@flask_app.get('/')
async def query():
    return open('static/query.html', 'r').read()

@flask_app.get('/generate')
async def display_generator():
    return open('static/generator.html', 'r').read()

@flask_app.get('/dao')
async def contract():
    return open('static/contract.html', 'r').read()

@flask_app.get('/css/style.css')
async def get_css():
    return Response(
        response=open('static/style.css', 'r').read(),
        status=200,
        mimetype="text/css")
     

api.add_resource(MutableSchema, '/mutable', '/mutable/', '/mutable/<caip>')
# api.add_resource(Members, '/mutable/<caip>/members')
# api.add_resource(Proposals, '/mutable/<caip>/proposals')
# api.add_resource(ActivityLog, '/mutable/<caip>/activitylog')
# api.add_resource(Governance, '/mutable/<caip>/governance')
api.add_resource(ImmutableSchema, '/immutable', '/immutable/', '/immutable/<cid>')
api.add_resource(ResolveSchema, '/resolve/<caip>')