"""Training models."""

from buddy_system_backend.database import PkModel, db
from buddy_system_backend.db.relation_tables import training_team


class Training(PkModel):
    __tablename__ = "training"

    name = db.Column(db.String)
    description = db.Column(db.String)
    modules = db.relationship("Module", backref="training", lazy=True)
    teams = db.relationship("Team", secondary=training_team)

    @classmethod
    def get_by_name(cls, name):
        """Get records by name."""
        if isinstance(name, str):
            return cls.query.filter(cls.name.contains(name))
        return None

    def __init__(self, name, description, modules=[], teams=[]):
        self.name = name
        self.description = description
        self.modules = modules
        self.teams = teams
