"""Training schema."""
from marshmallow import Schema, fields, EXCLUDE

from buddy_system_backend.onboarding.schema import OnboardingSchema, \
    OutputOnboardingSchema
from buddy_system_backend.role.schema import RoleSchema
from buddy_system_backend.section.schema import SectionSchema, \
    CustomSectionSchema
from buddy_system_backend.team.schema import TeamSchema


class OutputTemplateSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    teams = fields.List(fields.Nested(TeamSchema()))
    roles = fields.List(fields.Nested(RoleSchema()))
    onboardings = fields.List(fields.Nested(OutputOnboardingSchema()))
    sections = fields.List(fields.Nested(SectionSchema()))


class TemplateSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    teams = fields.List(fields.Integer)
    roles = fields.List(fields.Integer)
    onboardings = fields.List(fields.Nested(OutputOnboardingSchema()))
    sections = fields.List(fields.Nested(CustomSectionSchema()))


class ModelTemplateSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
