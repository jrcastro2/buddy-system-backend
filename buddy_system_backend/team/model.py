"""Team models."""
from buddy_system_backend.database import PkModel, db
from buddy_system_backend.db.relation_tables import team_user


class Team(PkModel):
    __tablename__ = "team"

    name = db.Column(db.String)
    description = db.Column(db.String)
    onboardings = db.relationship("Onboarding", backref="team", lazy=True)
    users = db.relationship(
        "User", secondary=team_user, backref=db.backref("teams", lazy=True)
    )

    def __init__(self, name, description, users, onboardings=[]):
        self.name = name
        self.description = description
        self.onboardings = onboardings
        self.users = users
