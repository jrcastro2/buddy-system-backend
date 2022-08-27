"""Section views."""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from buddy_system_backend.section.errors import SectionDoesNotExistError
from buddy_system_backend.section.model import Section
from buddy_system_backend.section.schema import SectionSchema
from buddy_system_backend.user.decorators import is_admin

sections_blueprint = Blueprint("section", __name__)


@sections_blueprint.route("/sections")
def list_sections():
    """Get all sections."""
    sections = Section.query.all()
    schema = SectionSchema(many=True)
    return jsonify(schema.dump(sections))


@sections_blueprint.route("/sections/<int:section_id>")
def get_section(section_id):
    """Get a section."""
    section = Section.get_by_id(section_id)
    if not section:
        raise SectionDoesNotExistError(section_id)
    schema = SectionSchema()
    return jsonify(schema.dump(section))


@sections_blueprint.route("/sections", methods=["POST"])
@jwt_required()
@is_admin
def create_section():
    """Create a section."""
    request_data = request.json
    schema = SectionSchema()
    section = schema.load(request_data)
    section_created = Section.create(**section)
    return jsonify(schema.dump(section_created))


@sections_blueprint.route("/sections/<int:section_id>", methods=["PUT"])
@jwt_required()
@is_admin
def update_section(section_id):
    """Update a section."""
    section = Section.get_by_id(section_id)
    if not section:
        raise SectionDoesNotExistError(section_id)
    request_data = request.json
    schema = SectionSchema()
    section_dict = schema.load(request_data)
    section.update(**section_dict)
    return jsonify(schema.dump(section))


@sections_blueprint.route("/sections/<int:section_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_section(section_id):
    """Delete a section."""
    section = Section.get_by_id(section_id)
    if not section:
        raise SectionDoesNotExistError(section_id)
    section.delete()
    return "", 204
