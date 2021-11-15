from features.feed.entities import Feed
from features.feed.models import (
    FeedOutput,
    FeedInput
)


def map_feed_input_to_feed(*, new_feed: FeedInput) -> Feed:
    return Feed(
        title=new_feed.title,
        description=new_feed.description
    )


def map_feed_to_feed_output(*, feed: Feed) -> FeedOutput:
    return FeedOutput(
        id=feed.id,
        title=feed.title,
        description=feed.description,
        published=feed.published,
        created_timestamp=feed.created_timestamp
    )
