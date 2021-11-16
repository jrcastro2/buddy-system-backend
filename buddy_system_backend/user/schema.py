"""User schema."""
from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(
        required=True, error_messages={"required": "Username is required."}
    )
    email = fields.Email(
        required=True, error_messages={"required": "Email is required."}
    )
    password = fields.Str(
        required=True, error_messages={"required": "Password is required."}
    )
    is_admin = fields.Bool()
    active = fields.Bool(dump_only=True)


class LoginSchema(Schema):
    username = fields.Str(
        required=True, error_messages={"required": "Username is required."}
    )
    password = fields.Str(
        required=True, error_messages={"required": "Password is required."}
    )
