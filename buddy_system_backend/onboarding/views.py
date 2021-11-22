"""Onboarding views."""

from flask import Blueprint, jsonify, request

from buddy_system_backend.onboarding.errors import OnboardingDoesNotExistError
from buddy_system_backend.onboarding.model import Onboarding
from buddy_system_backend.onboarding.schema import OnboardingSchema
from buddy_system_backend.user.decorators import is_admin

onboardings_blueprint = Blueprint("onboarding", __name__)


@onboardings_blueprint.route("/onboardings")
def list_onboardings():
    """Get all onboardings."""
    onboardings = Onboarding.query.all()
    schema = OnboardingSchema(many=True)
    return jsonify(schema.dump(onboardings))


@onboardings_blueprint.route("/onboardings/<int:onboarding_id>")
def get_onboarding(onboarding_id):
    """Get a onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    schema = OnboardingSchema()
    return jsonify(schema.dump(onboarding))


@onboardings_blueprint.route("/onboardings", methods=["POST"])
@is_admin
def create_onboarding():
    """Create a onboarding."""
    request_data = request.json
    schema = OnboardingSchema()
    onboarding = schema.load(request_data)
    onboarding_created = Onboarding.create(**onboarding)
    return jsonify(schema.dump(onboarding_created))


@onboardings_blueprint.route(
    "/onboardings/<int:onboarding_id>", methods=["PUT"]
)
@is_admin
def update_onboarding(onboarding_id):
    """Update a onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    request_data = request.json
    schema = OnboardingSchema()
    onboarding_dict = schema.load(request_data)
    onboarding.update(**onboarding_dict)
    return jsonify(schema.dump(onboarding))


@onboardings_blueprint.route(
    "/onboardings/<int:onboarding_id>", methods=["DELETE"]
)
@is_admin
def delete_onboarding(onboarding_id):
    """Delete a onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    onboarding.delete()
    return "", 204
