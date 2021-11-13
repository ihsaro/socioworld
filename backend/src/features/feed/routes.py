from fastapi import (
    APIRouter,
    Body,
    Depends,
    Path,
    HTTPException,
    status
)

from configurations.types import Error
from configurations.dependencies import get_current_user, get_database

from features.feed.models import (
    CreatedFeed,
    NewFeed,
    UpdatedFeed
)

from features.feed import services as feed_services


router = APIRouter(prefix="/api/v1/feeds", tags=["Feed"])


@router.post("")
async def create_feed(
    # Body parameters
    feed: NewFeed = Body(..., title="New feed details"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    created_feed = feed_services.create_feed(database=database, current_user=current_user, new_feed=feed)
    if isinstance(created_feed, CreatedFeed):
        return created_feed
    elif isinstance(created_feed, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=created_feed.message)


@router.get("")
async def read_feeds(
    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.post("/{feed_id}")
async def read_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be read"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.patch("/{feed_id}")
async def update_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be updated"),

    # Body parameters
    feed: UpdatedFeed = Body(..., title="Updated feed details"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.delete("/{feed_id}")
async def delete_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be deleted"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass
