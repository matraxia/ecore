from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    profile_pic_url: str | None
    biography: str | None
    object_given: int
    object_taken: int
    credit: int
    item_list: list[int]
    swap__list: list[int]