from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str | None
    pics_url: str | None
    tag_list: list[str]
    swap_place: str
    owner_id: int
    request_list: list[int]
    available: bool