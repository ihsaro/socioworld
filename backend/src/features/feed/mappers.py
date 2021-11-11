from features.feed.entities import Feed
from features.feed.models import (
    CreatedFeed,
    NewFeed
)


def map_new_feed_to_feed(*, new_feed: NewFeed) -> Feed:
    return Feed(
        title=new_feed.title,
        description=new_feed.description
    )


def map_feed_to_created_feed(*, feed: Feed) -> CreatedFeed:
    return CreatedFeed(
        id=feed.id,
        title=feed.title,
        description=feed.description
    )
