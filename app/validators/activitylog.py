from marshmallow import Schema, fields
from app.validators.base import BaseSchema
from app.validators.proposals import ProposalSchema
from app.validators.members import MemberSchema

class ActivitySchema(Schema):
    type       = fields.String()
    id         = fields.String()
    proposal   = fields.Nested(ProposalSchema)
    member     = fields.Nested(MemberSchema)

class ActivityLogUriSchema(BaseSchema):
    name       = fields.String()
    activities = fields.List(fields.Nested(ActivitySchema))