from typing import List

from fastapi import (
    APIRouter,
    Body,
    Depends,
    Path,
    HTTPException,
    status
)

from configurations.types import Error
from configurations.dependencies import (
    get_current_application_user,
    get_current_application_user_client,
    get_database
)

from features.feed.models import (
    FeedOutput,
    FeedInput,
)

from features.feed import services as feed_services


router = APIRouter(prefix="/api/v1/feeds", tags=["Feed"])


@router.post("", response_model=FeedOutput)
async def create_feed(
    # Body parameters
    feed: FeedInput = Body(..., title="New feed details"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    created_feed = feed_services.create_feed(database=database, current_user=current_user, new_feed=feed)
    if isinstance(created_feed, FeedOutput):
        return created_feed
    elif isinstance(created_feed, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=created_feed.message)


@router.get("", response_model=List[FeedOutput])
async def read_feeds(
    # Dependencies
    current_user=Depends(get_current_application_user),
    database=Depends(get_database)
):
    return feed_services.read_feeds(database=database, current_user=current_user)


@router.post("/{feed_id}", response_model=FeedOutput)
async def read_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be read"),

    # Dependencies
    current_user=Depends(get_current_application_user),
    database=Depends(get_database)
):
    pass


@router.patch("/{feed_id}", response_model=FeedOutput)
async def update_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be updated"),

    # Body parameters
    feed: FeedInput = Body(..., title="Updated feed details"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass


@router.delete("/{feed_id}")
async def delete_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be deleted"),

    # Dependencies
    current_user=Depends(get_current_application_user),
    database=Depends(get_database)
):
    pass
