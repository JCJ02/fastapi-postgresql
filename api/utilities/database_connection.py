from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..configurations.configuration import settings

# SYNCHRONOUS POSTGRESQL CONNECTION (USING PSYCOPG2)
DATABASE_URL = settings.DATABASE_URL

# CREATE SYNCHRONOUS ENGINE
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=10, max_overflow=20)

# CREATE SESSION FACTORY
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DEPENDENCY TO GET DB SESSION (SYNCHRONOUS)
def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()