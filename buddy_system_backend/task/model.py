"""Task models."""
from buddy_system_backend.database import PkModel, db


class Task(PkModel):
    __tablename__ = "task"

    name = db.Column(db.String)
    deadline = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    parent_task_id = db.Column(db.Integer, db.ForeignKey("task.id"))
    parent_task = db.relationship(
        "Task", remote_side="Task.id", backref=db.backref("subtasks")
    )
    section_id = db.Column(
        db.Integer, db.ForeignKey("section.id"), nullable=False
    )

    def __init__(
        self, name, deadline, subtasks, role_id, section_id, task_id=None
    ):
        self.name = name
        self.deadline = deadline
        self.subtasks = subtasks
        self.role_id = role_id
        self.section_id = section_id
        self.task_id = task_id
