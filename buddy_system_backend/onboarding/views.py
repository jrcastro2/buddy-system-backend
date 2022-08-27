"""Onboarding views."""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user

from buddy_system_backend import Template, User, Role, Task
from buddy_system_backend.onboarding.api import create_onboarding, \
    update_onboarding
from buddy_system_backend.onboarding.errors import OnboardingDoesNotExistError
from buddy_system_backend.onboarding.model import Onboarding, \
    OnboardingTaskUser
from buddy_system_backend.onboarding.schema import OutputOnboardingSchema, \
    Output_User_Role_Schema, User_Task_Schema
from buddy_system_backend.template.schema import OutputTemplateSchema
from buddy_system_backend.user.decorators import is_admin

onboardings_blueprint = Blueprint("onboarding", __name__)


@onboardings_blueprint.route("/onboardings")
def list_onboardings():
    """Get all onboardings."""
    onboardings = Onboarding.query.all()
    schema = OutputOnboardingSchema(many=True)
    return jsonify(schema.dump(onboardings))


@onboardings_blueprint.route("/onboardings/search")
def search_onboardings():
    """Search onboardings."""
    search_query = request.args.get('q')
    onboardings = Onboarding.get_by_name(search_query)
    schema = OutputOnboardingSchema(many=True)
    onboarding_dict = schema.dump(onboardings)
    for onboarding in onboarding_dict:
        users = []
        for onboarding_user in onboarding.get("onboarding_user", []):
            user = User.get_by_id(onboarding_user["user_id"])
            role = Role.get_by_id(onboarding_user["role_id"])
            users.append(Output_User_Role_Schema().dump(
                {"user": user, "role": role})
            )
        onboarding["users"] = users

    return jsonify(onboarding_dict)


@onboardings_blueprint.route("/my/onboardings/search")
@jwt_required()
def search_my_onboardings():
    """Search my onboardings."""
    search_query = request.args.get('q')
    onboardings = Onboarding.get_by_name(search_query)
    onboarding_filtered = []
    for onboarding in onboardings:
        for onboarding_user in onboarding.onboarding_user:
            if onboarding_user.user_id == current_user.id:
                onboarding_filtered.append(onboarding)
                break

    schema = OutputOnboardingSchema(many=True)
    onboarding_dict = schema.dump(onboarding_filtered)
    for onboarding in onboarding_dict:
        users = []
        for onboarding_user in onboarding.get("onboarding_user", []):
            user = User.get_by_id(onboarding_user["user_id"])
            role = Role.get_by_id(onboarding_user["role_id"])
            users.append(Output_User_Role_Schema().dump(
                {"user": user, "role": role})
            )
        onboarding["users"] = users

    return jsonify(onboarding_dict)


@onboardings_blueprint.route("/onboardings/<int:onboarding_id>")
def get_onboarding(onboarding_id):
    """Get an onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    template = Template.get_by_id(onboarding.template_id)
    schema = OutputOnboardingSchema()
    onboarding_dict = schema.dump(onboarding)

    template_schema = OutputTemplateSchema()
    onboarding_dict["template"] = template_schema.dump(template)


    users = []
    for onboarding_user in onboarding_dict.get("onboarding_user", []):
        user = User.get_by_id(onboarding_user["user_id"])
        role = Role.get_by_id(onboarding_user["role_id"])
        users.append(Output_User_Role_Schema().dump(
            {"user": user, "role": role})
        )

    onboarding_dict["users"] = users

    return jsonify(onboarding_dict)


@onboardings_blueprint.route("/onboardings/task/complete", methods=["PUT"])
@jwt_required()
def complete_tasks():
    """Complete a task from an onboarding."""
    request_data = request.json
    schema = User_Task_Schema()
    onboarding_dict = schema.load(request_data)
    onboarding = Onboarding.get_by_id(onboarding_dict["onboarding_id"])
    task = Task.get_by_id(onboarding_dict["task_id"])
    user = User.get_by_id(onboarding_dict["user_id"])
    OnboardingTaskUser.create(
        user=user, onboarding=onboarding, task=task,
    )
    return "Completed", 201


@onboardings_blueprint.route("/onboardings/task", methods=["PUT"])
@jwt_required()
def delte_task():
    """Delete a task from an onboarding."""
    request_data = request.json
    schema = User_Task_Schema()
    onboarding_dict = schema.load(request_data)
    onboarding_task_user = OnboardingTaskUser.get_by_user_task_id(
        onboarding_id=onboarding_dict["onboarding_id"],
        user_id=onboarding_dict["user_id"],
        task_id=onboarding_dict["task_id"],
    )

    task_dict = schema.load(request_data)
    onboarding_task_user.update(**task_dict)

    return jsonify(schema.dump(onboarding_task_user))


@onboardings_blueprint.route("/onboardings", methods=["POST"])
@jwt_required()
@is_admin
def create_onboarding_view():
    """Create an onboarding."""
    request_data = request.json

    onboarding = create_onboarding(request_data)

    return jsonify(OutputOnboardingSchema().dump(onboarding))


@onboardings_blueprint.route(
    "/onboardings/<int:onboarding_id>", methods=["PUT"]
)
def update_onboarding_view(onboarding_id):
    """Update a onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    request_data = request.json

    onboarding = update_onboarding(onboarding, request_data)

    return jsonify(OutputOnboardingSchema().dump(onboarding))


@onboardings_blueprint.route(
    "/onboardings/<int:onboarding_id>", methods=["DELETE"]
)
@jwt_required()
@is_admin
def delete_onboarding(onboarding_id):
    """Delete a onboarding."""
    onboarding = Onboarding.get_by_id(onboarding_id)
    if not onboarding:
        raise OnboardingDoesNotExistError(onboarding_id)
    onboarding.delete()
    return "", 204
