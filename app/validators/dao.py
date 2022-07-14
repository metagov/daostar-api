from marshmallow import Schema, fields, validate
from app.validators.fields import Caip10, Uri

class DaoSchema(Schema):
    _context       = fields.String(dump_only=True, default="http://www.daostar.org/schemas", data_key="@context")
    _type          = fields.String(dump_only=True, default="DAO", data_key="type")
    name           = fields.String(required=True, validate=validate.Length(min=1))
    description    = fields.String(default=None)
    membersURI     = Uri(default=None)
    proposalsURI   = Uri(default=None)
    activityLogURI = Uri(default=None)
    governanceURI  = Uri(default=None)

    class Meta:
        ordered = True

class MutableDaoSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
    caip = Caip10(required=True)

class ImmutableDaoSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
