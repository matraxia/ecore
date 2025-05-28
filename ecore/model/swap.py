from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SwapStatus(Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Swap(BaseModel):
    id_swap: int
    id_item: int
    id_user_giver: int
    id_user_taker: int
    date_swap: datetime
    status: SwapStatus



