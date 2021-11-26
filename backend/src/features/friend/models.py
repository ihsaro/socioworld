from pydantic import BaseModel


class FriendshipOutput(BaseModel):
    client_id: int
    friend_id: int
    requested: bool
    approved: bool


class FriendOutput(BaseModel):
    client_id: int
    first_name: str
    last_name: str
