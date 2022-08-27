"""Team views."""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from buddy_system_backend.user.model import User
from buddy_system_backend.team.errors import TeamDoesNotExistError
from buddy_system_backend.team.model import Team
from buddy_system_backend.team.schema import TeamSchema, TeamModelSchema, \
    CreateTeamSchema
from buddy_system_backend.user.decorators import is_admin

teams_blueprint = Blueprint("team", __name__)


@teams_blueprint.route("/teams")
def list_teams():
    """Get all teams."""
    teams = Team.query.all()
    schema = TeamSchema(many=True)
    return jsonify(schema.dump(teams))


@teams_blueprint.route("/teams/search")
def search_teams():
    """Search teams."""
    search_query = request.args.get('q')
    teams = Team.get_by_name(search_query)
    schema = TeamSchema(many=True)
    return jsonify(schema.dump(teams))


@teams_blueprint.route("/teams/<int:team_id>")
def get_team(team_id):
    """Get a team."""
    team = Team.get_by_id(team_id)
    if not team:
        raise TeamDoesNotExistError(team_id)
    schema = TeamSchema()
    return jsonify(schema.dump(team))


@teams_blueprint.route("/teams", methods=["POST"])
@jwt_required()
@is_admin
def create_team():
    """Create a team."""
    request_data = request.json
    schema = TeamSchema()
    create_schema = CreateTeamSchema()
    model_schema = TeamModelSchema()
    team_dict = create_schema.load(request_data)
    users = User.get_by_ids(team_dict["users"])
    team = model_schema.load(request_data)
    team_created = Team.create(**team)
    team_created.users = users
    team_created.save()
    return jsonify(schema.dump(team_created))


@teams_blueprint.route("/teams/<int:team_id>", methods=["PUT"])
@jwt_required()
@is_admin
def update_team(team_id):
    """Update a team."""
    team = Team.get_by_id(team_id)
    if not team:
        raise TeamDoesNotExistError(team_id)
    request_data = request.json

    create_schema = CreateTeamSchema()
    model_schema = TeamModelSchema()
    team_dict = create_schema.load(request_data)
    users = User.get_by_ids(team_dict["users"])
    team_model_dict = model_schema.load(request_data)
    team.users = users
    team.update(**team_model_dict)

    schema = TeamSchema()
    return jsonify(schema.dump(team))


@teams_blueprint.route("/teams/<int:team_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_team(team_id):
    """Delete a team."""
    team = Team.get_by_id(team_id)
    if not team:
        raise TeamDoesNotExistError(team_id)
    team.delete()
    return "", 204
