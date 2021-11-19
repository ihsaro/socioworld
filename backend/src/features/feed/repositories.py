from typing import (
    List,
    Union
)

from sqlalchemy.exc import (
    IntegrityError,
    SQLAlchemyError
)
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError

from configurations.messages.error.generic import GenericErrorMessages
from configurations.messages.success.generic import GenericSuccessMessages
from configurations.types import (
    Error,
    Success
)
from features.feed.entities import Feed


def create_feed(*, database: Session, feed: Feed) -> Union[Feed, Error]:
    try:
        database.add(feed)
        database.commit()
        return feed
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def read_feeds_for_client(*, database: Session, client_id: int) -> Union[List[Feed], Error]:
    try:
        return database.query(Feed).filter(Feed.client_id == client_id).all()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def read_feeds(*, database: Session) -> Union[List[Feed], Error]:
    try:
        return database.query(Feed).all()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def read_feed(*, database: Session, feed_id: int) -> Union[Feed, Error]:
    try:
        feed = database.query(Feed).get(feed_id)
        if feed is None:
            return Error(
                code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
                message=GenericErrorMessages.OBJECT_NOT_FOUND.value
            )
        else:
            return feed
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def delete_feed(*, database: Session, feed: Feed) -> Union[Success, Error]:
    try:
        database.delete(feed)
        database.commit()
        return Success(
            code=GenericSuccessMessages.OBJECT_DELETED.name,
            message=GenericSuccessMessages.OBJECT_DELETED.value
        )
    except UnmappedInstanceError:
        return Error(
            code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
            message=GenericErrorMessages.OBJECT_NOT_FOUND.value
        )
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def update_feed(*, database: Session, feed_id: int, updated_feed_attributes: dict) -> Union[Feed, Error]:
    try:
        feed_queried = database.query(Feed).filter(Feed.id == feed_id)
        if feed_queried.first() is None:
            return Error(
                code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
                message=GenericErrorMessages.OBJECT_NOT_FOUND.value
            )
        feed_queried.update(updated_feed_attributes)
        database.commit()
        return feed_queried.first()
    except IntegrityError:
        return Error(code=GenericErrorMessages.INTEGRITY_ERROR.name, message=GenericErrorMessages.INTEGRITY_ERROR.value)
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)
