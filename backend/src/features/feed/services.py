from sqlalchemy.orm import Session

from configurations.types import Error

from features.authentication.entities import ApplicationUser
from features.feed.entities import Feed
from features.feed.mappers import (
    map_feed_to_created_feed,
    map_new_feed_to_feed
)
from features.feed.models import NewFeed, CreatedFeed
from features.feed import repositories as feed_repositories


def create_feed(*, database: Session, current_user: ApplicationUser, new_feed: NewFeed) -> CreatedFeed:
    feed_to_create = map_new_feed_to_feed(new_feed=new_feed)
    feed_to_create.application_user_id = current_user.id
    feed = feed_repositories.create_feed(database=database, feed=feed_to_create)
    if isinstance(feed, Feed):
        return map_feed_to_created_feed(feed=feed)
    elif isinstance(feed, Error):
        return feed
