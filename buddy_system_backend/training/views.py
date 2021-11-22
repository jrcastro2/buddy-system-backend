"""Training views."""
from flask import Blueprint, jsonify, request

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


@trainings_blueprint.route("/trainings/<int:training_id>")
def get_training(training_id):
    """Get a training."""
    training = Training.get_by_id(training_id)
    if not training:
        raise TrainingDoesNotExistError(training_id)
    schema = TrainingSchema()
    return jsonify(schema.dump(training))


@trainings_blueprint.route("/trainings", methods=["POST"])
@is_admin
def create_training():
    """Create a training."""
    request_data = request.json
    schema = TrainingSchema()
    training = schema.load(request_data)
    training_created = Training.create(**training)
    return jsonify(schema.dump(training_created))


@trainings_blueprint.route("/trainings/<int:training_id>", methods=["PUT"])
@is_admin
def update_training(training_id):
    """Update a training."""
    training = Training.get_by_id(training_id)
    if not training:
        raise TrainingDoesNotExistError(training_id)
    request_data = request.json
    schema = TrainingSchema()
    training_dict = schema.load(request_data)
    training.update(**training_dict)
    return jsonify(schema.dump(training))


@trainings_blueprint.route("/trainings/<int:training_id>", methods=["DELETE"])
@is_admin
def delete_training(training_id):
    """Delete a training."""
    training = Training.get_by_id(training_id)
    if not training:
        raise TrainingDoesNotExistError(training_id)
    training.delete()
    return "", 204
