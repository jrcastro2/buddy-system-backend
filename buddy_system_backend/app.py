"""The app module."""
import logging
import sys

from flask import Flask

from buddy_system_backend.extensions import db, login_manager
from buddy_system_backend.user.views import blueprint


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
    app.register_blueprint(blueprint)
    return None


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)


app = create_app()
