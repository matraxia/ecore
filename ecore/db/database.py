from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:masa@localhost:5432/db_test"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=5, pool_pre_ping=True)


client_db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

