from pydantic import BaseModel


class Request(BaseModel):
    id_request: int
    id_item: int
    id_user: int
    date_request: str
    status: str
    message: str | None
    request_type: str