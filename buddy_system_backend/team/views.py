"""Team views."""
from flask import Blueprint, jsonify, request

from buddy_system_backend.team.errors import TeamDoesNotExistError
from buddy_system_backend.team.model import Team
from buddy_system_backend.team.schema import TeamSchema

teams_blueprint = Blueprint("team", __name__)


@teams_blueprint.route("/teams")
def list_teams():
    """Get all teams."""
    teams = Team.query.all()
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
def create_team():
    """Create a team."""
    request_data = request.json
    schema = TeamSchema()
    team = schema.load(request_data)
    team_created = Team.create(**team)
    return jsonify(schema.dump(team_created))


@teams_blueprint.route("/teams/<int:team_id>", methods=["PUT"])
def update_team(team_id):
    """Update a team."""
    team = Team.get_by_id(team_id)
    if not team:
        raise TeamDoesNotExistError(team_id)
    request_data = request.json
    schema = TeamSchema()
    team_dict = schema.load(request_data)
    team.update(**team_dict)
    return jsonify(schema.dump(team))


@teams_blueprint.route("/teams/<int:team_id>", methods=["DELETE"])
def delete_team(team_id):
    """Delete a team."""
    team = Team.get_by_id(team_id)
    if not team:
        raise TeamDoesNotExistError(team_id)
    team.delete()
    return "", 204
