from marshmallow import Schema, fields, validate, INCLUDE
from app.validators.fields import Caip10, Uri

class DaoSchema(Schema):
    context         = fields.String(data_key="@context", dump_default="http://www.daostar.org/schemas")
    type            = fields.String(dump_default="DAO")
    name            = fields.String(required=True)
    description     = fields.String()
    membersURI      = Uri()
    proposalsURI    = Uri()
    activityLogURI  = Uri()
    governanceURI   = Uri()

    class Meta:
        ordered = True
        unknown = INCLUDE

class MutableSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
    caip = Caip10(required=True)
