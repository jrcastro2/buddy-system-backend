"""The app module."""
import logging
import sys

from flask import Flask

from buddy_system_backend.extensions import db, login_manager
from buddy_system_backend.module.views import modules_blueprint
from buddy_system_backend.onboarding.views import onboardings_blueprint
from buddy_system_backend.role.views import roles_blueprint
from buddy_system_backend.section.views import sections_blueprint
from buddy_system_backend.task.views import tasks_blueprint
from buddy_system_backend.team.views import teams_blueprint
from buddy_system_backend.template.views import templates_blueprint
from buddy_system_backend.training.views import trainings_blueprint
from buddy_system_backend.user.views import users_blueprint


def create_app(config_object="buddy_system_backend.conf"):
    """Create application factory."""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    configure_logger(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    login_manager.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(users_blueprint)
    app.register_blueprint(trainings_blueprint)
    app.register_blueprint(templates_blueprint)
    app.register_blueprint(teams_blueprint)
    app.register_blueprint(tasks_blueprint)
    app.register_blueprint(sections_blueprint)
    app.register_blueprint(roles_blueprint)
    app.register_blueprint(onboardings_blueprint)
    app.register_blueprint(modules_blueprint)
    return None


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


app = create_app()
