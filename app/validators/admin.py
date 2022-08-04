from marshmallow import Schema, fields
from app.validators.fields import Caip10

class InputAdminSchema(Schema):
    caip = Caip10(required=True)

class AuthorizeAdminSchema(Schema):
    signature = fields.String(required=True)