"""Task views."""
from flask import Blueprint, jsonify, request

from buddy_system_backend.task.errors import TaskDoesNotExistError
from buddy_system_backend.task.model import Task
from buddy_system_backend.task.schema import TaskSchema
from buddy_system_backend.user.decorators import is_admin

tasks_blueprint = Blueprint("task", __name__)


@tasks_blueprint.route("/tasks")
def list_tasks():
    """Get all tasks."""
    tasks = Task.query.all()
    schema = TaskSchema(many=True)
    return jsonify(schema.dump(tasks))


@tasks_blueprint.route("/tasks/<int:task_id>")
def get_task(task_id):
    """Get a task."""
    task = Task.get_by_id(task_id)
    if not task:
        raise TaskDoesNotExistError(task_id)
    schema = TaskSchema()
    return jsonify(schema.dump(task))


@tasks_blueprint.route("/tasks", methods=["POST"])
@is_admin
def create_task():
    """Create a task."""
    request_data = request.json
    schema = TaskSchema()
    task = schema.load(request_data)
    task_created = Task.create(**task)
    return jsonify(schema.dump(task_created))


@tasks_blueprint.route("/tasks/<int:task_id>", methods=["PUT"])
@is_admin
def update_task(task_id):
    """Update a task."""
    task = Task.get_by_id(task_id)
    if not task:
        raise TaskDoesNotExistError(task_id)
    request_data = request.json
    schema = TaskSchema()
    task_dict = schema.load(request_data)
    task.update(**task_dict)
    return jsonify(schema.dump(task))


@tasks_blueprint.route("/tasks/<int:task_id>", methods=["DELETE"])
@is_admin
def delete_task(task_id):
    """Delete a task."""
    task = Task.get_by_id(task_id)
    if not task:
        raise TaskDoesNotExistError(task_id)
    task.delete()
    return "", 204
