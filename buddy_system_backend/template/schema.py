"""Training schema."""
from marshmallow import Schema, fields

from buddy_system_backend.onboarding.schema import OnboardingSchema
from buddy_system_backend.role.schema import RoleSchema
from buddy_system_backend.section.schema import SectionSchema
from buddy_system_backend.team.schema import TeamSchema


class TemplateSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    teams = fields.List(fields.Nested(TeamSchema()))
    roles = fields.List(fields.Nested(RoleSchema()))
    onboardings = fields.List(fields.Nested(OnboardingSchema()))
    sections = fields.List(fields.Nested(SectionSchema()))
