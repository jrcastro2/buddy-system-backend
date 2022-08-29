"""Training views."""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from buddy_system_backend.training.api import create_training_w_modules, \
    update_training_w_modules
from buddy_system_backend.training.errors import TrainingDoesNotExistError
from buddy_system_backend.training.model import Training
from buddy_system_backend.training.schema import TrainingSchema
from buddy_system_backend.user.decorators import is_admin

trainings_blueprint = Blueprint("training", __name__)


@trainings_blueprint.route("/trainings")
def list_trainings():
    """Get all trainings."""
    trainings = Training.query.all()
    schema = TrainingSchema(many=True)
    return jsonify(schema.dump(trainings))


@trainings_blueprint.route("/trainings/search")
def search_trainings():
    """Search trainings."""
    search_query = request.args.get('q')
    users = Training.get_by_name(search_query)
    schema = TrainingSchema(many=True)
    return jsonify(schema.dump(users))


@trainings_blueprint.route("/trainings/<int:training_id>")
def get_training(training_id):
    """Get a training."""
    training = Training.get_by_id(training_id)
    if not training:
        raise TrainingDoesNotExistError(training_id)
    schema = TrainingSchema()
    return jsonify(schema.dump(training))


@trainings_blueprint.route("/trainings", methods=["POST"])
@jwt_required()
@is_admin
def create_training():
    """Create a training."""
    request_data = request.json
    output_schema = TrainingSchema()

    training_created = create_training_w_modules(request_data)
    return jsonify(output_schema.dump(training_created))


@trainings_blueprint.route("/trainings/<int:training_id>", methods=["PUT"])
@jwt_required()
@is_admin
def update_training(training_id):
    """Update a training."""
    request_data = request.json
    output_schema = TrainingSchema()
    training_updated = update_training_w_modules(training_id, request_data)

    return jsonify(output_schema.dump(training_updated))


@trainings_blueprint.route("/trainings/<int:training_id>", methods=["DELETE"])
@jwt_required()
@is_admin
def delete_training(training_id):
    """Delete a training."""
    training = Training.get_by_id(training_id)
    if not training:
        raise TrainingDoesNotExistError(training_id)
    training.delete()
    return "", 204
