"""User models."""
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from buddy_system_backend.database import PkModel, db
from buddy_system_backend.extensions import bcrypt


class User(UserMixin, PkModel):
    __tablename__ = "user"

    username = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)

    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value).decode("utf8")

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    def __init__(self, username, _password, email, is_admin=False):
        self.username = username
        self._password = _password
        self.email = email
        self.is_admin = is_admin
