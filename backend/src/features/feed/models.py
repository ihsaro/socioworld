from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class FeedBase(BaseModel):
    title: str
    description: str
    published: bool = True


class FeedInput(FeedBase):
    pass


class FeedOutput(FeedBase):
    id: int
    created_timestamp: datetime
    last_modified_timestamp: Optional[datetime]
