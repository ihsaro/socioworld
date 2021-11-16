from typing import (
    Union,
    List
)

from sqlalchemy.orm import Session

from configurations.messages.error.generic import GenericErrorMessages
from configurations.types import (
    Error,
    Success
)

from features.authentication.entities import (
    ApplicationUser,
    Roles
)
from features.authentication import selectors as authentication_selectors
from features.feed.entities import Feed
from features.feed.mappers import (
    map_feed_to_feed_output,
    map_feed_input_to_feed
)
from features.feed.models import (
    FeedInput,
    FeedOutput
)
from features.feed import repositories as feed_repositories


def create_feed(*, database: Session, current_user: ApplicationUser, new_feed: FeedInput) -> Union[FeedOutput, Error]:
    feed_to_create = map_feed_input_to_feed(new_feed=new_feed)
    feed_to_create.client_id = authentication_selectors.get_client_user_from_application_user_id(
        database=database,
        application_user_id=current_user.id
    ).id
    feed = feed_repositories.create_feed(database=database, feed=feed_to_create)
    if isinstance(feed, Feed):
        return map_feed_to_feed_output(feed=feed)
    elif isinstance(feed, Error):
        return feed


def read_feeds(*, database: Session, current_user: ApplicationUser) -> List[FeedOutput]:
    if current_user.role == Roles.ADMIN:
        feeds = feed_repositories.read_feeds(
            database=database
        )
    elif current_user.role == Roles.CLIENT:
        feeds = feed_repositories.read_feeds_for_client(
            database=database,
            client_id=authentication_selectors.get_client_user_from_application_user_id(
                        database=database,
                        application_user_id=current_user.id
            ).id
        )

    feeds_list = []
    for feed in feeds:
        feeds_list.append(map_feed_to_feed_output(feed=feed))
    return feeds_list


def read_feed(*, database: Session, current_user: ApplicationUser, feed_id: int) -> [FeedOutput, Error]:
    feed = feed_repositories.read_feed(
        database=database,
        feed_id=feed_id
    )
    if current_user.role == Roles.ADMIN:
        return map_feed_to_feed_output(feed=feed)
    elif current_user.role == Roles.CLIENT:
        client_id = authentication_selectors.get_client_user_from_application_user_id(
                        database=database,
                        application_user_id=current_user.id
            ).id

        if feed.client_id != client_id:
            return Error(
                code=GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.name,
                message=GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.value
            )

        return map_feed_to_feed_output(feed=feed)


def delete_feed(*, database: Session, current_user: ApplicationUser, feed_id: int) -> [Success, Error]:
    feed = database.query(Feed).get(feed_id)

    if feed is None:
        return Error(
            code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
            message=GenericErrorMessages.OBJECT_NOT_FOUND.value
        )

    if current_user.role == Roles.ADMIN:
        return feed_repositories.delete_feed(database=database, feed=feed)
    elif current_user.role == Roles.CLIENT:
        client_id = authentication_selectors.get_client_user_from_application_user_id(
            database=database,
            application_user_id=current_user.id
        ).id

        if feed.client_id != client_id:
            return Error(
                code=GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.name,
                message=GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.value
            )

        return feed_repositories.delete_feed(database=database, feed=feed)
