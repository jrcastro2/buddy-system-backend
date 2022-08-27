from buddy_system_backend.database import db


team_user = db.Table(
    "team_user",
    db.Column(
        "team_id", db.Integer, db.ForeignKey("team.id"), primary_key=True
    ),
    db.Column(
        "user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True
    ),
)

training_team = db.Table(
    "training_team",
    db.Column(
        "training_id",
        db.Integer,
        db.ForeignKey("training.id"),
        primary_key=True,
    ),
    db.Column(
        "team_id", db.Integer, db.ForeignKey("team.id"), primary_key=True
    ),
)

team_template = db.Table(
    "team_template",
    db.Column(
        "team_id", db.Integer, db.ForeignKey("team.id"), primary_key=True
    ),
    db.Column(
        "template_id",
        db.Integer,
        db.ForeignKey("template.id"),
        primary_key=True,
    ),
)

onboarding_training = db.Table(
    "onboarding_training",
    db.Column(
        "onboarding_id",
        db.Integer,
        db.ForeignKey("onboarding.id"),
        primary_key=True,
    ),
    db.Column(
        "training_id",
        db.Integer,
        db.ForeignKey("training.id"),
        primary_key=True,
    ),
)


template_role = db.Table(
    "template_role",
    db.Column(
        "template_id",
        db.Integer,
        db.ForeignKey("template.id"),
        primary_key=True,
    ),
    db.Column(
        "role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True
    ),
)

# TODO: DELETE all db and recreate it
# onboarding_user = db.Table(
#     "onboarding_user",
#     db.Column(
#         "onboarding_id",
#         db.Integer,
#         db.ForeignKey("onboarding.id"),
#         primary_key=True,
#     ),
#     db.Column(
#         "user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True
#     ),
#     db.Column(
#         "role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True
#     ),
# )
