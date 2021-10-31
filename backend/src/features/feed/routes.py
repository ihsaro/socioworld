from fastapi import (
    APIRouter,
    Body,
    Depends,
    Path
)

from configurations.dependencies import get_current_user

from features.feed.models import FeedInput


router = APIRouter(prefix="/api/v1/feeds", tags=["Feed"])


@router.post("")
async def create_feed(
    # Body parameters
    feed: FeedInput = Body(..., title="New feed details"),

    # Dependencies
    current_user=Depends(get_current_user)
):
    pass


@router.get("")
async def read_feeds():
    pass


@router.post("/{feed_id}")
async def read_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be read")
):
    pass


@router.patch("/{feed_id}")
async def update_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be updated"),

    # Body parameters
    feed: FeedInput = Body(..., title="Updated feed details")
):
    pass


@router.delete("/{feed_id}")
async def delete_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be deleted")
):
    pass
