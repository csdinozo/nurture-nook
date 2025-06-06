from sqlalchemy import create_engine, declarative_base
from sqlalchemy.orm import sessionmaker
from dot_env import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
