"""Module views."""

from flask import Blueprint, jsonify, request

from buddy_system_backend.module.errors import ModuleDoesNotExistError
from buddy_system_backend.module.model import Module
from buddy_system_backend.module.schema import ModuleSchema

modules_blueprint = Blueprint("module", __name__)


@modules_blueprint.route("/modules")
def list_modules():
    """Get all modules."""
    modules = Module.query.all()
    schema = ModuleSchema(many=True)
    return jsonify(schema.dump(modules))


@modules_blueprint.route("/modules/<int:module_id>")
def get_module(module_id):
    """Get a module."""
    module = Module.get_by_id(module_id)
    if not module:
        raise ModuleDoesNotExistError(module_id)
    schema = ModuleSchema()
    return jsonify(schema.dump(module))


@modules_blueprint.route("/modules", methods=["POST"])
def create_module():
    """Create a module."""
    request_data = request.json
    schema = ModuleSchema()
    module = schema.load(request_data)
    module_created = Module.create(**module)
    return jsonify(schema.dump(module_created))


@modules_blueprint.route("/modules/<int:module_id>", methods=["PUT"])
def update_module(module_id):
    """Update a module."""
    module = Module.get_by_id(module_id)
    if not module:
        raise ModuleDoesNotExistError(module_id)
    request_data = request.json
    schema = ModuleSchema()
    module_dict = schema.load(request_data)
    module.update(**module_dict)
    return jsonify(schema.dump(module))


@modules_blueprint.route("/modules/<int:module_id>", methods=["DELETE"])
def delete_module(module_id):
    """Delete a module."""
    module = Module.get_by_id(module_id)
    if not module:
        raise ModuleDoesNotExistError(module_id)
    module.delete()
    return "", 204
