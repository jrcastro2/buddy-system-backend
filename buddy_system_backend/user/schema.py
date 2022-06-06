"""User schema."""
from marshmallow import Schema, fields, post_load
from buddy_system_backend.extensions import bcrypt


def encrypt_password(user_dict):
    user_dict["password"] = bcrypt.generate_password_hash(
        user_dict["password"]
    ).decode("utf8")
    return user_dict


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

    @post_load
    def post_load(self, in_data, **kwargs):
        return encrypt_password(in_data)


class UpdateProfileSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    is_admin = fields.Bool()


class UpdateUserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str(load_only=True)
    is_admin = fields.Bool()

    @post_load
    def post_load(self, in_data, **kwargs):
        return encrypt_password(in_data)


class UpdatePasswordSchema(Schema):
    new_password = fields.Str(load_only=True)
    confirm_password = fields.Str(load_only=True)
    old_password = fields.Str(load_only=True)


class MeSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(
        required=True, error_messages={"required": "Username is required."}
    )
    email = fields.Email(
        required=True, error_messages={"required": "Email is required."}
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
