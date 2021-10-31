"""User models."""
from buddy_system_backend.app import db
from buddy_system_backend.database import PkModel


class User(PkModel):
    __tablename__ = 'user'

    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)
    is_admin = db.Column(db.Boolean(), default=False)

    def __init__(self, name, password, email, is_admin=False):
        self.name = name
        self.password = password
        self.email = email
        self.is_admin = is_admin
