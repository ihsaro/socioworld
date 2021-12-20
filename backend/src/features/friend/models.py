from datetime import datetime
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


class FriendFeed(BaseModel):
    client_id: int
    first_name: str
    last_name: str
    feed_title: str
    feed_description: str
    created_timestamp: datetime
