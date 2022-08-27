"""User views."""
import json
from datetime import datetime, timezone, timedelta

from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, unset_jwt_cookies, get_jwt, \
    get_jwt_identity, jwt_required, current_user

from buddy_system_backend.errors import JSONSchemaValidationError
from buddy_system_backend.extensions import login_manager, jwt, bcrypt
from buddy_system_backend.user.api import get_and_validate_user, \
    validate_password
from buddy_system_backend.user.decorators import is_admin
from buddy_system_backend.user.errors import UserDoesNotExistError
from buddy_system_backend.user.model import User
from buddy_system_backend.user.schema import UserSchema, LoginSchema, MeSchema, \
    UpdateUserSchema, UpdatePasswordSchema, UpdateProfileSchema

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


# Change to client side, remove token and that's it
@users_blueprint.route("/logout", methods=["POST"])
def logout():
    """Logout."""
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    logout_user()
    return response


@users_blueprint.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


@users_blueprint.route('/token', methods=["POST"])
def create_token():
    request_data = request.get_json()
    schema = LoginSchema()
    user_dict = schema.load(request_data)
    user = get_and_validate_user(user_dict)
    access_token = create_access_token(identity=user.email)
    response = {"access_token": access_token}
    return response


@users_blueprint.route('/me')
@jwt_required()
def my_profile():
    schema = MeSchema()
    return jsonify(schema.dump(current_user))


@users_blueprint.route("/users")
@jwt_required()
# @is_admin
def list_users():
    """Get all users."""
    users = User.query.all()
    schema = UserSchema(many=True)
    return jsonify(schema.dump(users))


@users_blueprint.route("/users/search")
def search_users():
    """Search users."""
    search_query = request.args.get('q')
    users = User.get_by_query(search_query)
    schema = UserSchema(many=True)
    return jsonify(schema.dump(users))


@users_blueprint.route("/users/<int:user_id>")
@jwt_required()
# @login_required
# @is_admin
def get_user(user_id):
    """Get user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    schema = UserSchema()
    return jsonify(schema.dump(user))


@users_blueprint.route("/users", methods=["POST"])
def create_user():
    """Create user."""
    request_data = request.json
    schema = UserSchema()
    user = schema.load(request_data)
    _password = bcrypt.generate_password_hash("123456").decode("utf8")
    user["_password"] = _password
    del user["password"]
    user_created = User.create(**user)
    return jsonify(schema.dump(user_created))


@users_blueprint.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_user(user_id):
    """Delete user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    user.delete()
    return "", 204


@users_blueprint.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    """Update user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    request_data = request.json
    schema = UpdateProfileSchema()
    user_dict = schema.load(request_data)
    user.update(**user_dict)
    return jsonify(schema.dump(user))


@users_blueprint.route("/users/<int:user_id>/update-password", methods=["PUT"])
@jwt_required()
def update_password(user_id):
    """Update user."""
    user = User.get_by_id(user_id)
    if not user:
        raise UserDoesNotExistError(user_id)
    request_data = request.json
    password_schema = UpdatePasswordSchema()
    password_dict = password_schema.load(request_data)
    validate_password(password_dict, user)
    user_schema = UpdateUserSchema()
    user_dict = user_schema.dump(user)
    user_dict["password"] = password_dict["new_password"]
    user.update(**user_dict)
    return jsonify(user_schema.dump(user))


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(email=identity).one_or_none()