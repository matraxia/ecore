from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel

# Enum for the status of a swap
# class SwapStatus(Enum):
#     PENDING = "pending"
#     ACCEPTED = "accepted"
#     COMPLETED = "completed"
#     CANCELLED = "cancelled"

# Pydantic model for creating a new Swap (input from client)
class SwapCreate(BaseModel):
    id_item: int
    id_user_giver: int
    id_user_taker: int
    # date_swap is optional, if not provided, the SQLAlchemy model's default will be used
    date_swap: Optional[datetime] = None
    # status: SwapStatus = SwapStatus.PENDING
    item_metadata: Optional[dict] = {}  # Optional metadata for the item being swapped

# Pydantic model for responding with a Swap (output to client)
class SwapResponse(BaseModel):
    id_swap: int  # id_swap is present in the response after creation
    id_item: int
    id_user_giver: int
    id_user_taker: int
    date_swap: datetime
    # status: SwapStatus

    # Pydantic's Config class for ORM mode (or from_attributes for Pydantic v2)
    # This allows Pydantic to read data directly from SQLAlchemy ORM models.
    class Config:
        from_attributes = True # For Pydantic v2. Use orm_mode = True for Pydantic v1.
