"""Role views."""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from buddy_system_backend.role.errors import RoleDoesNotExistError
from buddy_system_backend.role.model import Role
from buddy_system_backend.role.schema import RoleSchema
from buddy_system_backend.user.decorators import is_admin

roles_blueprint = Blueprint("role", __name__)


@roles_blueprint.route("/roles")
def list_roles():
    """Get all roles."""
    roles = Role.query.all()
    schema = RoleSchema(many=True)
    return jsonify(schema.dump(roles))


@roles_blueprint.route("/roles/search")
def search_teams():
    """Search roles."""
    search_query = request.args.get('q')
    teams = Role.get_by_name(search_query)
    schema = RoleSchema(many=True)
    return jsonify(schema.dump(teams))


@roles_blueprint.route("/roles/<int:role_id>")
def get_role(role_id):
    """Get a role."""
    role = Role.get_by_id(role_id)
    if not role:
        raise RoleDoesNotExistError(role_id)
    schema = RoleSchema()
    return jsonify(schema.dump(role))


@roles_blueprint.route("/roles", methods=["POST"])
@jwt_required()
@is_admin
def create_role():
    """Create a role."""
    request_data = request.json
    schema = RoleSchema()
    role = schema.load(request_data)
    role_created = Role.create(**role)
    return jsonify(schema.dump(role_created))


@roles_blueprint.route("/roles/<int:role_id>", methods=["PUT"])
@jwt_required()
@is_admin
def update_role(role_id):
    """Update a role."""
    role = Role.get_by_id(role_id)
    if not role:
        raise RoleDoesNotExistError(role_id)
    request_data = request.json
    schema = RoleSchema()
    role_dict = schema.load(request_data)
    role.update(**role_dict)
    return jsonify(schema.dump(role))


@roles_blueprint.route("/roles/<int:role_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_role(role_id):
    """Delete a role."""
    role = Role.get_by_id(role_id)
    if not role:
        raise RoleDoesNotExistError(role_id)
    role.delete()
    return "", 204
