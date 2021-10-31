from buddy_system_backend.app import db
from buddy_system_backend.module.model import Module
from buddy_system_backend.onboarding.model import Onboarding
from buddy_system_backend.role.model import Role
from buddy_system_backend.section.model import Section
from buddy_system_backend.task.model import Task
from buddy_system_backend.team.model import Team
from buddy_system_backend.template.model import Template
from buddy_system_backend.training.model import Training
from buddy_system_backend.user.model import User

db.session.query(Task).delete()
db.session.query(Role).delete()
db.session.query(Module).delete()
db.session.query(Onboarding).delete()
db.session.query(Section).delete()
db.session.query(Template).delete()
db.session.query(Team).delete()
db.session.query(Training).delete()
db.session.query(User).delete()
db.session.commit()
