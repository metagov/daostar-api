from marshmallow import Schema, fields, validate, INCLUDE
from app.validators import Caip10

class DaoSchema(Schema):
    name            = fields.String(required=True)
    description     = fields.String()
    membersURI      = fields.Url(schemes={'ipfs'})
    proposalsURI    = fields.Url(schemes=('ipfs'))
    activityLogURI  = fields.Url(schemes={'ipfs'})
    governanceURI   = fields.Url(schemes={'ipfs'})

    class Meta:
        ordered = True
        unknown = INCLUDE

class MutableSchema(Schema):
    data = fields.Nested(DaoSchema, required=True)
    caip = Caip10(required=True)