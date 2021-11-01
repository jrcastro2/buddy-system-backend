from buddy_system_backend.app import app
from buddy_system_backend.database import db
from buddy_system_backend.module.model import Module
from buddy_system_backend.role.model import Role
from buddy_system_backend.section.model import Section
from buddy_system_backend.task.model import Task
from buddy_system_backend.team.model import Team
from buddy_system_backend.template.model import Template
from buddy_system_backend.training.model import Training
from buddy_system_backend.user.model import User
import lorem

with app.app_context():
    db.init_app(app)

    # Create and save roles
    roles = [
        Role(name="Buddy Manager"),
        Role(name="Buddy"),
        Role(name="Supervisor"),
        Role(name="Section leader"),
        Role(name="Newcomer"),
    ]

    for rol in roles:
        Role.save(rol)

    # Create and save users
    users = [
        User(name="Javier", password="123456", email="javier@test.com"),
        User(name="Miguel", password="123456", email="miguel@test.com"),
        User(name="Jose", password="123456", email="jose@test.com"),
        User(name="Luis", password="123456", email="luis@test.com"),
        User(name="Jesus", password="123456", email="jesus@test.com"),
    ]

    for user in users:
        User.save(user)

    # Create and save trainings
    trainings = [
        Training(name="IT", description=lorem.paragraph(), modules=[], teams=[]),
        Training(name="CDS", description=lorem.paragraph(), modules=[], teams=[]),
        Training(name="REAN", description=lorem.paragraph(), modules=[], teams=[]),
        Training(name="RDM", description=lorem.paragraph(), modules=[], teams=[])
    ]

    for training in trainings:
        Training.save(training)

    # Create and save templates
    templates = [
        Template(name="IT", description=lorem.paragraph(), teams=[], roles=[],
                 onboardings=[], sections=[]),
        Template(name="CDS", description=lorem.paragraph(), teams=[], roles=[],
                 onboardings=[], sections=[]),
        Template(name="REANA", description=lorem.paragraph(), teams=[], roles=[],
                 onboardings=[], sections=[]),
        Template(name="RDM", description=lorem.paragraph(), teams=[], roles=[],
                 onboardings=[], sections=[])
    ]

    for template in templates:
        Template.save(template)

    # Create and save teams
    teams = [
        Team(name="IT", description=lorem.paragraph(), onboardings=[], users=[]),
        Team(name="CDS", description=lorem.paragraph(), onboardings=[], users=[]),
        Team(
            name="REANA", description=lorem.paragraph(), onboardings=[], users=[]
        ),
        Team(name="RDM", description=lorem.paragraph(), onboardings=[], users=[])
    ]

    for team in teams:
        Team.save(team)

    # Create and save sections
    sections = [
        Section(name="IT", template_id=templates[0].id, tasks=[]),
        Section(name="CDS", template_id=templates[0].id, tasks=[]),
        Section(name="REANA", template_id=templates[0].id, tasks=[]),
        Section(name="RDM", template_id=templates[0].id, tasks=[])
    ]

    for section in sections:
        Section.save(section)

    # Create and save tasks
    tasks = [
        Task(name=lorem.sentence(), deadline=1, role_id=roles[0].id,
             section_id=sections[0].id, subtasks=[]),
        Task(name=lorem.sentence(), deadline=1, role_id=roles[0].id,
             section_id=sections[0].id, subtasks=[]),
        Task(name=lorem.sentence(), deadline=1, role_id=roles[0].id,
             section_id=sections[0].id, subtasks=[]),
        Task(name=lorem.sentence(), deadline=1, role_id=roles[0].id,
             section_id=sections[0].id, subtasks=[]),
    ]

    for task in tasks:
        Task.save(task)

    # Create and save modules
    modules = [
        Module(name=lorem.sentence(), description=lorem.paragraph(),
               content=lorem.text(), training_id=trainings[0].id),
        Module(name=lorem.sentence(), description=lorem.paragraph(),
               content=lorem.text(), training_id=trainings[0].id),
        Module(name=lorem.sentence(), description=lorem.paragraph(),
               content=lorem.text(), training_id=trainings[0].id),
        Module(name=lorem.sentence(), description=lorem.paragraph(),
               content=lorem.text(), training_id=trainings[0].id),
    ]

    for module in modules:
        Module.save(module)
