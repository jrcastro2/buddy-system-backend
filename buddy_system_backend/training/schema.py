"""Training schema."""
from marshmallow import Schema, fields

from buddy_system_backend.module.schema import ModuleSchema
from buddy_system_backend.team.schema import TeamSchema


class TrainingSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    modules = fields.List(fields.Nested(ModuleSchema()))
    teams = fields.List(fields.Nested(TeamSchema()))


class CustomModuleSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    description = fields.Str()
    content = fields.Str()
    training_id = fields.Integer()


class CustomTrainingSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    modules = fields.List(fields.Nested(CustomModuleSchema()))
