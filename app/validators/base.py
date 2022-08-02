from marshmallow import Schema, fields, EXCLUDE
from app.constants import SchemaFormat

class BaseSchema(Schema):
    _context = fields.String(dump_only=True, default=SchemaFormat.context, data_key="@context")
    _type    = fields.String(dump_only=True, default=SchemaFormat.type, data_key="type")

    class Meta:
        ordered = True
        unknown = EXCLUDE