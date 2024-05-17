from marshmallow import Schema, fields, pre_dump, post_dump
from app.validators.fields import Caip10, Uri
from app.validators.base import BaseSchema

class DaoUriSchema(BaseSchema):
    name = fields.String(default=None)
    description = fields.String(default=None)
    membersURI = fields.String(default=None)
    proposalsURI = fields.String(default=None)
    issuersURI = fields.String(default=None)
    activityLogURI = fields.String(default=None)
    governanceURI = fields.String(default=None)
    contractsRegistryURI = fields.String(default=None)
    managerAddress = fields.String(default=None)

    # @post_dump
    # def remove_empty_fields(self, data, many, **kwargs):
    #     return {key: value for key, value in data.items() if value not in [None, "", {}]}

class InputCaipWithDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
    caip = Caip10(required=True)

class InputDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
