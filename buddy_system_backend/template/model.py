"""Template models."""
from buddy_system_backend.database import PkModel, db
from buddy_system_backend.db.relation_tables import (
    team_template,
    template_role,
)


class Template(PkModel):
    __tablename__ = "template"

    name = db.Column(db.String)
    description = db.Column(db.String)
    teams = db.relationship("Team", secondary=team_template)
    roles = db.relationship("Role", secondary=template_role)
    onboardings = db.relationship("Onboarding", backref="template", lazy=True)
    sections = db.relationship("Section", backref="template", lazy=True)

    @classmethod
    def get_by_name(cls, name):
        """Get records by name."""
        if isinstance(name, str):
            return cls.query.filter(cls.name.contains(name))
        return None

    def __init__(self, name, description, teams=[], roles=[], sections=[], onboardings=[]):
        self.name = name
        self.description = description
        self.teams = teams
        self.roles = roles
        self.onboardings = onboardings
        self.sections = sections
