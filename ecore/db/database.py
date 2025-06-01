from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your actual PostgreSQL connection string
# For Docker, this would typically be the service name of your PostgreSQL container
DATABASE_URL = "postgresql://postgres:password@localhost:5432/ecore_test"

# Create a SQLAlchemy engine
# SQLAlchemy's create_engine by default uses QueuePool for pooling connections
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=5, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()