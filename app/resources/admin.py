import secrets
import eth_utils
from flask_restful import Resource, abort
from app.interfaces.aws import *
from app.utils import validate_json, load_schema, validate_signature
from app.validators import InputAdminSchema, AuthorizeAdminSchema

class CreateApiKey(Resource):
    def post(self):
        schema = load_schema(InputAdminSchema, validate_json())
        caip = schema['caip']

        api_key = secrets.token_urlsafe()

        admin(put_item, api_key, {'caip': caip, 'validated': False})

        return {
            'api_key': api_key
        }

class AuthorizeApiKey(Resource):
    def get(self, key):
        item = admin(get_item, key)
        
        if not item: abort(404, message=f'API key "{key}" not found.')
        return item

    def post(self, key):
        schema = load_schema(AuthorizeAdminSchema, validate_json())
        signature = schema['signature']

        if not len(signature): abort(400, message='Invalid signature.')
        
        try:
            wallet_address = validate_signature(signature, key)
        except eth_utils.exceptions.ValidationError:
            abort(400, message='Invalid signature.')

        auth = admin(update_item, key, {
            'wallet': wallet_address,
            'validated': True
        })

        mutable(update_item, auth['caip'], {
            'protected': True
        })

        return {
            'address': wallet_address
        }
    
    def delete(self, key):
        item = admin(get_item, key)
        if not item: abort(404, message=f'API key not found.')
        admin(delete_item, key)
        return {"message": "Successfully revoked API key."}
