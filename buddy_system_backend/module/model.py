"""Module models."""
from buddy_system_backend.app import db
from buddy_system_backend.database import PkModel


class Module(PkModel):
    __tablename__ = 'module'

    name = db.Column(db.String)
    description = db.Column(db.String)
    content = db.Column(db.String)
    training_id = db.Column(
        db.Integer, db.ForeignKey('training.id'), nullable=False
    )

    def __init__(self, name, description, content, training_id):
        self.name = name
        self.description = description
        self.content = content
        self.training_id = training_id
