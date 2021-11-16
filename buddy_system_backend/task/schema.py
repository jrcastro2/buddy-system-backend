"""Training schema."""
from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    deadline = fields.Int()
    role_id = fields.Int()
    parent_task_id = fields.Int()
    section_id = fields.Int()
    subtasks = fields.List(fields.Nested(lambda: TaskSchema()))
