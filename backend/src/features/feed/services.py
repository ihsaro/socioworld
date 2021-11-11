from sqlalchemy.orm import Session

from configurations.types import Error

from features.feed.entities import Feed
from features.feed.mappers import (
    map_feed_to_created_feed,
    map_new_feed_to_feed
)
from features.feed.models import NewFeed, CreatedFeed
from features.feed import repositories as feed_repositories


def create_feed(*, database: Session, new_feed: NewFeed) -> CreatedFeed:
    feed = feed_repositories.create_feed(database=database, feed=map_new_feed_to_feed(new_feed=new_feed))
    if isinstance(feed, Feed):
        return map_feed_to_created_feed(feed=feed)
    elif isinstance(feed, Error):
        return feed
