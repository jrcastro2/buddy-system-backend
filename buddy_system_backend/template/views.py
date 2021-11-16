"""Template views."""
from flask import Blueprint, jsonify, request

from buddy_system_backend.template.errors import TemplateDoesNotExistError
from buddy_system_backend.template.model import Template
from buddy_system_backend.template.schema import TemplateSchema

templates_blueprint = Blueprint("template", __name__)


@templates_blueprint.route("/templates")
def list_templates():
    """Get all templates."""
    templates = Template.query.all()
    schema = TemplateSchema(many=True)
    return jsonify(schema.dump(templates))


@templates_blueprint.route("/templates/<int:template_id>")
def get_template(template_id):
    """Get a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)
    schema = TemplateSchema()
    return jsonify(schema.dump(template))


@templates_blueprint.route("/templates", methods=["POST"])
def create_template():
    """Create a template."""
    request_data = request.json
    schema = TemplateSchema()
    template = schema.load(request_data)
    template_created = Template.create(**template)
    return jsonify(schema.dump(template_created))


@templates_blueprint.route("/templates/<int:template_id>", methods=["PUT"])
def update_template(template_id):
    """Update a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)
    request_data = request.json
    schema = TemplateSchema()
    template_dict = schema.load(request_data)
    template.update(**template_dict)
    return jsonify(schema.dump(template))


@templates_blueprint.route("/templates/<int:template_id>", methods=["DELETE"])
def delete_template(template_id):
    """Delete a template."""
    template = Template.get_by_id(template_id)
    if not template:
        raise TemplateDoesNotExistError(template_id)
    template.delete()
    return "", 204
