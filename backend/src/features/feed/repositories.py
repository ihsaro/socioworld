from typing import (
    List,
    Union
)

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from configurations.errors.generic import GenericErrors
from configurations.types import Error
from features.feed.entities import Feed


def create_feed(*, database: Session, feed: Feed) -> Union[Feed, Error]:
    try:
        database.add(feed)
        database.commit()
        return feed
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def read_feeds_for_client(*, database: Session, client_id: int) -> Union[List[Feed], Error]:
    try:
        return database.query(Feed).filter(Feed.client_id == client_id).all()
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def read_feeds(*, database: Session) -> Union[List[Feed], Error]:
    try:
        return database.query(Feed).all()
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def read_feed(*, database: Session, feed_id: int) -> Union[Feed, Error]:
    try:
        feed = database.query(Feed).get(feed_id)
        if feed is None:
            return Error(code=GenericErrors.OBJECT_NOT_FOUND.name, message=GenericErrors.OBJECT_NOT_FOUND.value)
        else:
            return feed
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)
