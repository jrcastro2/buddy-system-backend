import sqlalchemy as db

from buddy_system_backend.base import engine

meta = db.MetaData(engine)
meta.reflect(bind=engine)

meta.drop_all(engine)
