"""Section models."""
from buddy_system_backend.database import PkModel, db


class Section(PkModel):
    __tablename__ = "section"

    name = db.Column(db.String)
    template_id = db.Column(
        db.Integer, db.ForeignKey("template.id"), nullable=True
    )
    tasks = db.relationship("Task", backref="section", lazy=True, cascade="all, delete")

    def __init__(self, name, template_id, tasks=[]):
        self.name = name
        self.template_id = template_id
        self.tasks = tasks
