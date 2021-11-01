from buddy_system_backend.app import app
from buddy_system_backend.database import db

with app.app_context():
    db.drop_all()
