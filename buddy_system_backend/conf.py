"""Application configuration."""
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = (
    "postgresql+psycopg2://postgres:123456@db:5432/buddysystem"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "not-so-secret :/"
JWT_SECRET_KEY = "please-remember-to-change-me"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
