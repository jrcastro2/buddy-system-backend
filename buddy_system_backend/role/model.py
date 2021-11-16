"""Role models."""
from buddy_system_backend.database import PkModel, db


class Role(PkModel):
    __tablename__ = "role"

    name = db.Column(db.String)
    tasks = db.relationship("Task", backref="role", lazy=True)

    def __init__(self, name, tasks=[]):
        self.name = name
        self.tasks = tasks
