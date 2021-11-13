from typing import Union

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
