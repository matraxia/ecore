from datetime import datetime
from typing import Optional

from pydantic import BaseModel


#  model for creating a new Swap (input from client)
class SwapCreate(BaseModel):
    id_item: str
    id_user_giver: str
    id_user_taker: str
    # date_swap is optional, if not provided, the SQLAlchemy model's default will be used
    date_swap: Optional[datetime] = None
    item_metadata: Optional[dict] = {}  # Optional metadata for the item being swapped

#  model for responding with a Swap (output to client)
class SwapResponse(BaseModel):
    id_swap: int
    id_item: str
    id_user_giver: str
    id_user_taker: str
    date_swap: datetime

    # This allows Pydantic to read data directly from SQLAlchemy ORM models.
    class Config:
        from_attributes = True


class SwapGivenCount(BaseModel):
    user_id: str
    items_given_count: int

    # This allows Pydantic to read data directly from SQLAlchemy ORM models.
    class Config:
        from_attributes = True


class SwapTakenCount(BaseModel):
    user_id: str
    items_taken_count: int

    # This allows Pydantic to read data directly from SQLAlchemy ORM models.
    class Config:
        from_attributes = True