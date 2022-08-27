"""Training schema."""
from marshmallow import Schema, fields, EXCLUDE, INCLUDE

from buddy_system_backend.role.schema import RoleSchema
from buddy_system_backend.training.schema import TrainingSchema
from buddy_system_backend.user.schema import UserSchema


class UserRoleSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    user = fields.Int()
    role = fields.Int()


class OnboardingUser(Schema):

    user_id = fields.Int()
    role_id = fields.Int()


class OnboardingTaskUser(Schema):

    user_id = fields.Int()
    task_id = fields.Int()
    onboarding_id = fields.Int()
    completed = fields.Bool()


class OnboardingSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    starting_date = fields.Date()
    trainings = fields.List(fields.Int())
    users = fields.List(fields.Nested(UserRoleSchema()))
    team_id = fields.Int()
    template_id = fields.Int()


class OutputOnboardingSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    starting_date = fields.Date()
    onboarding_user = fields.List(fields.Nested(OnboardingUser()))
    onboarding_task_user = fields.List(fields.Nested(OnboardingTaskUser()))
    trainings = fields.List(fields.Nested(TrainingSchema()))
    users = fields.List(fields.Nested(UserSchema()))
    team_id = fields.Int()
    template_id = fields.Int()


class Output_User_Role_Schema(Schema):
    user = fields.Nested(UserSchema())
    role = fields.Nested(RoleSchema())


class User_Task_Schema(Schema):
    onboarding_id = fields.Int()
    task_id = fields.Int()
    user_id = fields.Int()
    completed = fields.Boolean()


class ModelOnboardingSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id = fields.Integer(dump_only=True)
    name = fields.Str()
    starting_date = fields.Date()
    team_id = fields.Int()
    template_id = fields.Int()
