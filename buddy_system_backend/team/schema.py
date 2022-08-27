"""Training schema."""
from marshmallow import Schema, fields, EXCLUDE

# from buddy_system_backend.onboarding.schema import OnboardingSchema
from buddy_system_backend.user.schema import UserSchema


class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    users = fields.List(fields.Nested(UserSchema()))


class CreateTeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    users = fields.List(fields.Integer)


class TeamModelSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
