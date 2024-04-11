from marshmallow import Schema, fields, post_load
from app.validators.fields import Caip10, Uri
from app.validators.base import BaseSchema

# class BaseSchema(Schema):
#     @post_load
#     def remove_empty_fields(self, data, **kwargs):
#         """Remove keys with None values or empty strings."""
#         return {key: value for key, value in data.items() if value not in [None, "", 'null']}

class DaoUriSchema(BaseSchema):
    name           = fields.String(default=None)
    description    = fields.String(default=None)
    membersURI     = fields.String(default=None)
    proposalsURI   = fields.String(default=None)
    issuersURI     = fields.String(default=None)
    activityLogURI = fields.String(default=None)
    governanceURI  = fields.String(default=None)
    contractsRegistryURI = fields.String(default=None)
    managerAddress  = fields.String(default=None)

class InputCaipWithDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
    caip = Caip10(required=True)

class InputDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
