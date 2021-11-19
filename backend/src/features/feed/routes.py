from typing import List

from fastapi import (
    APIRouter,
    Body,
    Depends,
    Path,
    HTTPException,
    status,
    Response
)

from configurations.messages.error.generic import GenericErrorMessages
from configurations.types import (
    Error,
    Success
)
from configurations.dependencies import (
    get_current_application_user,
    get_current_application_user_client,
    get_database
)

from features.feed.models import (
    FeedOutput,
    FeedInput,
    FeedInputPatch
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


@router.get("/{feed_id}", response_model=FeedOutput)
async def read_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be read"),

    # Dependencies
    current_user=Depends(get_current_application_user),
    database=Depends(get_database)
):
    feed = feed_services.read_feed(database=database, current_user=current_user, feed_id=feed_id)
    if isinstance(feed, Error):
        if feed.code == GenericErrorMessages.OBJECT_NOT_FOUND.name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=feed.message)
        elif feed.code == GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.name:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=feed.message)
    elif isinstance(feed, FeedOutput):
        return feed


@router.patch("/{feed_id}", response_model=FeedOutput)
async def update_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be updated"),

    # Body parameters
    feed: FeedInputPatch = Body(..., title="Updated feed details"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    updated_feed = feed_services.update_feed(
        database=database,
        current_user=current_user,
        feed_id=feed_id,
        updated_feed=feed
    )
    if isinstance(updated_feed, FeedOutput):
        return updated_feed
    elif isinstance(updated_feed, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=updated_feed.message)


@router.delete("/{feed_id}")
async def delete_feed(
    # Path parameters
    feed_id: int = Path(..., title="The ID of the feed to be deleted"),

    # Dependencies
    current_user=Depends(get_current_application_user),
    database=Depends(get_database)
):
    deleted_feed = feed_services.delete_feed(database=database, current_user=current_user, feed_id=feed_id)

    if isinstance(deleted_feed, Error):
        if deleted_feed.code == GenericErrorMessages.OBJECT_NOT_FOUND.name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=deleted_feed.message)
        elif deleted_feed.code == GenericErrorMessages.UNAUTHORIZED_OBJECT_ACCESS.name:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=deleted_feed.message)
    elif isinstance(deleted_feed, Success):
        return Response(None, status_code=status.HTTP_204_NO_CONTENT)

