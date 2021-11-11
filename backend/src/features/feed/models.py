from pydantic import BaseModel


class NewFeed(BaseModel):
    title: str
    description: str


class CreatedFeed(BaseModel):
    id: int
    title: str
    description: str


class UpdatedFeed(BaseModel):
    id: int
    title: str
    description: str
