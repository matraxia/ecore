from sqlalchemy import Column, Integer, DateTime, Enum as SQLEnum
from datetime import datetime

from sqlalchemy.dialects.postgresql import JSONB

# Import Base from your database setup
from ecore.db.database import Base # Adjust the import path based on your project structure
# from .schemas import SwapStatus # Import the Pydantic Enum to use in SQLAlchemy's Enum type

# SQLAlchemy ORM model for the 'swaps' table
class Swap(Base):
    __tablename__ = "swaps" # The name of the table in your PostgreSQL database

    # Primary key, typically auto-incremented by the database
    id_swap = Column(Integer, primary_key=True, index=True)
    id_item = Column(Integer, nullable=False)
    id_user_giver = Column(Integer, nullable=False)
    id_user_taker = Column(Integer, nullable=False)
    # date_swap defaults to the current UTC time if not provided
    date_swap = Column(DateTime, default=datetime.utcnow, nullable=False)
    item_metadata = Column(JSONB, nullable=False, default={})


    def __repr__(self):
        return f"<Swap(id_swap={self.id_swap}, status='{self.status}')>"
