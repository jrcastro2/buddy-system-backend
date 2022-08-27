"""Template views."""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from buddy_system_backend import Team, Role
from buddy_system_backend.section.api import create_section_and_tasks
from buddy_system_backend.template.errors import TemplateDoesNotExistError
from buddy_system_backend.template.model import Template
from buddy_system_backend.template.schema import TemplateSchema, \
    OutputTemplateSchema, ModelTemplateSchema
from buddy_system_backend.user.decorators import is_admin

templates_blueprint = Blueprint("template", __name__)


@templates_blueprint.route("/templates")
def list_templates():
    """Get all templates."""
    templates = Template.query.all()
    schema = OutputTemplateSchema(many=True)
    return jsonify(schema.dump(templates))


@templates_blueprint.route("/templates/search")
def search_teams():
    """Search templates."""
    search_query = request.args.get('q')
    teams = Template.get_by_name(search_query)
    schema = OutputTemplateSchema(many=True)
    return jsonify(schema.dump(teams))


@templates_blueprint.route("/templates/<int:template_id>")
def get_template(template_id):
    """Get a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)
    schema = OutputTemplateSchema()

    return jsonify(schema.dump(template))


@templates_blueprint.route("/templates", methods=["POST"])
@jwt_required()
@is_admin
def create_template():
    """Create a template."""
    request_data = request.json

    schema = TemplateSchema()
    output_schema = OutputTemplateSchema()
    model_schema = ModelTemplateSchema()

    template_dict = schema.load(request_data)
    teams = Team.get_by_ids(template_dict.get("teams", []))
    roles = Role.get_by_ids(template_dict.get("roles", []))
    template_model_dict = model_schema.load(request_data)
    template_created = Template.create(**template_model_dict)

    create_section_and_tasks(
        template_dict.get("sections", []), template_created.id
    )

    template_created.teams = teams
    template_created.roles = roles
    template_created.save()
    return jsonify(output_schema.dump(template_created))


@templates_blueprint.route("/templates/<int:template_id>", methods=["PUT"])
@jwt_required()
@is_admin
def update_template(template_id):
    """Update a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)

    request_data = request.json

    schema = TemplateSchema()
    output_schema = OutputTemplateSchema()
    model_schema = ModelTemplateSchema()

    template_dict = schema.load(request_data)
    template_model_dict = model_schema.load(request_data)
    teams = Team.get_by_ids(template_dict.get("teams", []))
    roles = Role.get_by_ids(template_dict.get("roles", []))
    template.teams = teams
    template.roles = roles

    for section in template.sections:
        section.delete()

    create_section_and_tasks(template_dict.get("sections", []), template.id)

    template.update(**template_model_dict)
    return jsonify(output_schema.dump(template))


@templates_blueprint.route("/templates/<int:template_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_template(template_id):
    """Delete a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)
    template.delete()
    return "", 204
