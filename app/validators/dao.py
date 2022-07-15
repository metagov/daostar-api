from marshmallow import Schema, fields, validate
from app.validators.fields import Caip10, Uri

class DaoSchema(Schema):
    _context       = fields.String(dump_only=True, default="http://www.daostar.org/schemas", data_key="@context")
    _type          = fields.String(dump_only=True, default="DAO", data_key="type")
    name           = fields.String(default=None)
    description    = fields.String(default=None)
    membersURI     = fields.String(default=None)
    proposalsURI   = fields.String(default=None)
    activityLogURI = fields.String(default=None)
    governanceURI  = fields.String(default=None)

    class Meta:
        ordered = True

class InputCaipWithDaoSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
    caip = Caip10(required=True)

class InputDaoSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
