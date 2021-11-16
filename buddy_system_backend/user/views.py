"""User views."""
from flask import Blueprint, current_app, request, flash, jsonify
from flask_login import login_user, login_required, logout_user
from marshmallow import ValidationError

from buddy_system_backend.errors import JSONSchemaValidationError
from buddy_system_backend.extensions import login_manager
from buddy_system_backend.user.api import get_and_validate_user
from buddy_system_backend.user.decorators import is_admin
from buddy_system_backend.user.errors import UserDoesNotExistError
from buddy_system_backend.user.model import User
from buddy_system_backend.user.schema import UserSchema, LoginSchema

users_blueprint = Blueprint("user", __name__)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@users_blueprint.errorhandler(ValidationError)
def validation_error(error):
    """Catch validation errors."""
    return JSONSchemaValidationError(error=error).get_response()


@users_blueprint.route("/login", methods=["POST"])
def login():
    """Login."""
    request_data = request.get_json()
    schema = LoginSchema()
    user_dict = schema.load(request_data)
    user = get_and_validate_user(user_dict)
    login_user(user)
    return "", 204


@users_blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    return "", 204


@users_blueprint.route("/users")
@is_admin
@login_required
def list_users():
    """Get all users."""
    users = User.query.all()
    schema = UserSchema(many=True)
    return jsonify(schema.dump(users))


@users_blueprint.route("/users/<int:user_id>")
@login_required
def get_user(user_id):
    """Get user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    schema = UserSchema()
    return jsonify(schema.dump(user))


@users_blueprint.route("/users", methods=["POST"])
@login_required
# TODO: Permissions
def create_user():
    """Create user."""
    request_data = request.json
    schema = UserSchema()
    user = schema.load(request_data)
    user_created = User.create(**user)
    return jsonify(schema.dump(user_created))


@users_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
@login_required
# TODO: Permissions
def delete_user(user_id):
    """Delete user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    user.delete()
    return "", 204


@users_blueprint.route("/users/<int:user_id>", methods=["PUT"])
@login_required
# TODO: Permissions
def update_user(user_id):
    """Update user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    request_data = request.json
    schema = UserSchema()
    user_dict = schema.load(request_data)
    user.update(**user_dict)
    return jsonify(schema.dump(user))
