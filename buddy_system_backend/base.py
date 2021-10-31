"""Base module."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgresql+psycopg2://postgres:123456@localhost/buddysystem'
)
Session = sessionmaker(bind=engine)

Base = declarative_base()
