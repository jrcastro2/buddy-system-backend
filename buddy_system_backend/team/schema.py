"""Training schema."""
from marshmallow import Schema, fields

# from buddy_system_backend.onboarding.schema import OnboardingSchema
from buddy_system_backend.user.schema import UserSchema


class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    # onboardings = fields.List(fields.Nested(OnboardingSchema()))
    users = fields.List(fields.Nested(UserSchema()))
