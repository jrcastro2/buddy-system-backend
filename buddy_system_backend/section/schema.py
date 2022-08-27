"""Training schema."""
from marshmallow import Schema, fields, EXCLUDE

from buddy_system_backend.task.schema import TaskSchema
from buddy_system_backend.training.schema import TrainingSchema
from buddy_system_backend.user.schema import UserSchema


class SectionSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    template_id = fields.Int()
    tasks = fields.List(fields.Nested(TaskSchema()))


class CustomTaskSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    name = fields.Str()
    role_id = fields.Int()


class CustomSectionSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    name = fields.Str()
    tasks = fields.List(fields.Nested(CustomTaskSchema()))
