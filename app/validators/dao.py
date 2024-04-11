from marshmallow import Schema, fields, pre_dump
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

    @pre_dump
    def remove_empty_fields(self, data, **kwargs):
        """Remove fields with None or empty string values before dumping."""
        data_dict = data.__dict__.copy()
        for key in list(data_dict.keys()):  # list() to avoid RuntimeError due to change in dict size
            if data_dict[key] in [None, ""]:
                del data_dict[key]
        return data_dict

class InputCaipWithDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
    caip = Caip10(required=True)

class InputDaoSchema(Schema):
    data = fields.Nested(DaoUriSchema, required=True)
