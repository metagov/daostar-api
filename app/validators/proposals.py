from marshmallow import Schema, fields
from app.validators.base import BaseSchema

class CallSchema(Schema):
    type        = fields.String()
    operation   = fields.String()
    _from       = fields.String()
    to          = fields.String()
    value       = fields.String()
    data        = fields.String()

class ProposalSchema(Schema):
    type        = fields.String()
    id          = fields.String()
    name        = fields.String()
    contentURI  = fields.String()
    status      = fields.String()
    calls       = fields.List(fields.Nested(CallSchema))

class ProposalsUriSchema(BaseSchema):
    name        = fields.String()
    proposals   = fields.List(fields.Nested(ProposalSchema))