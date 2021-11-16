"""Training schema."""
from marshmallow import Schema, fields

from buddy_system_backend.training.schema import TrainingSchema
from buddy_system_backend.user.schema import UserSchema


class OnboardingSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    starting_date = fields.Date()
    trainings = fields.List(fields.Nested(TrainingSchema()))
    users = fields.List(fields.Nested(UserSchema()))
    team_id = fields.Int()
    template_id = fields.Int()
