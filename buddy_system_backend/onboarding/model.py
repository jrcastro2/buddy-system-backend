"""Onboarding models."""
from buddy_system_backend.database import PkModel, db
from buddy_system_backend.db.relation_tables import (
    onboarding_training,
)


class Onboarding(PkModel):
    __tablename__ = "onboarding"

    name = db.Column(db.String)
    starting_date = db.Column(db.Date)
    trainings = db.relationship("Training", secondary=onboarding_training)
    onboarding_user = db.relationship("OnboardingUser", back_populates="onboarding", cascade="all, delete")
    onboarding_task_user = db.relationship("OnboardingTaskUser", back_populates="onboarding", cascade="all, delete")
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"), nullable=False)
    template_id = db.Column(
        db.Integer, db.ForeignKey("template.id"), nullable=False
    )

    @classmethod
    def get_by_name(cls, name):
        """Get records by name."""
        if isinstance(name, str):
            return cls.query.filter(cls.name.contains(name))
        return None

    def __init__(
        self, name, starting_date, team_id, template_id, trainings=[]
    ):
        self.name = name
        self.starting_date = starting_date
        self.team_id = team_id
        self.template_id = template_id
        self.trainings = trainings


class OnboardingUser(PkModel):
    __tablename__ = "onboarding_user"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    onboarding_id = db.Column(
        db.Integer, db.ForeignKey("onboarding.id"), nullable=False
    )
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(user_id, onboarding_id, role_id),)

    user = db.relationship("User")
    onboarding = db.relationship(
        "Onboarding", back_populates="onboarding_user"
    )
    role = db.relationship("Role")


class OnboardingTaskUser(PkModel):
    __tablename__ = "onboarding_task_user"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    onboarding_id = db.Column(
        db.Integer, db.ForeignKey("onboarding.id"), nullable=False
    )
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)

    __table_args__ = (db.UniqueConstraint(user_id, onboarding_id, task_id),)

    user = db.relationship("User")
    onboarding = db.relationship(
        "Onboarding", back_populates="onboarding_task_user"
    )
    task = db.relationship("Task")
    completed = db.Column(db.Boolean(), default=False)

    @classmethod
    def get_by_user_task_id(cls, user_id, task_id, onboarding_id):
        """Get records by name."""
        if any(
                (
                        isinstance(user_id,
                                   (str, bytes)) and user_id.isdigit(),
                        isinstance(user_id, (int, float)),
                )
        ) and any(
                (
                        isinstance(task_id,
                                   (str, bytes)) and task_id.isdigit(),
                        isinstance(task_id, (int, float)),
                )
        ) and any(
                (
                        isinstance(onboarding_id,
                                   (str, bytes)) and onboarding_id.isdigit(),
                        isinstance(onboarding_id, (int, float)),
                )
        ):
            return cls.query.filter_by(
                user_id=user_id, task_id=task_id, onboarding_id=onboarding_id
            ).one_or_none()
        return None
