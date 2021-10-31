"""Onboarding models."""
from buddy_system_backend.app import db
from buddy_system_backend.database import PkModel
from buddy_system_backend.db.relation_tables import onboarding_training, \
    onboarding_user


class Onboarding(PkModel):
    __tablename__ = 'onboarding'

    name = db.Column(db.String)
    starting_date = db.Column(db.Date)
    trainings = db.relationship("Training", secondary=onboarding_training)
    users = db.relationship("User", secondary=onboarding_user)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'),
                            nullable=False)

    def __init__(
            self, name, starting_date, trainings, users, team_id, template_id
    ):
        self.name = name
        self.starting_date = starting_date
        self.trainings = trainings
        self.users = users
        self.team_id = team_id
        self.template_id = template_id
