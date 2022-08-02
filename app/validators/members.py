from marshmallow import Schema, fields
from app.validators.base import BaseSchema

class MemberSchema(Schema):
    type    = fields.String(default="EthereumAddress")
    id      = fields.String()

class MembersUriSchema(BaseSchema):
    name    = fields.String(default=None)
    members = fields.List(fields.Nested(MemberSchema))