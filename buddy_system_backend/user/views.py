"""User views."""
from flask import Blueprint, current_app, request, flash
from flask_login import login_user, login_required, logout_user

from buddy_system_backend.extensions import login_manager
from buddy_system_backend.user.model import User

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    current_app.logger.info("Hello from the home page!")
    user = User.query.all()[0]
    if request.method == "POST":
        login_user(user)
        flash("You are logged in.", "success")
        return "POST"
    return "hey"


@blueprint.route("/test/")
@login_required
def test():
    """Test."""
    return "Test!"


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return "BYE!"
