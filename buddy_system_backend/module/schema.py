"""Training schema."""
from marshmallow import Schema, fields


class ModuleSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    content = fields.Str()
    training_id = fields.Int()
