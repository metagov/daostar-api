from marshmallow import Schema, fields, pre_dump, post_dump
from app.validators.fields import Caip10, Uri
from app.validators.base import BaseSchema

class DaoUriSchema(BaseSchema):
    name = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    description = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    membersURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    proposalsURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    issuersURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    activityLogURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    governanceURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    contractsRegistryURI = fields.String(skip_if=lambda x: x in [None, ""], required=False)
    managerAddress = fields.String(skip_if=lambda x: x in [None, ""], required=False)

    @post_dump
    def remove_empty_fields(self, data, many, **kwargs):
        return {key: value for key, value in data.items() if value not in [None, "", {}]}

class InputCaipWithDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
    caip = Caip10(required=True)

class InputDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
