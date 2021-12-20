from typing import List

from fastapi import (
    APIRouter,
    Body,
    Depends,
    Path,
    HTTPException,
    Response,
    status
)

from configurations.types import (
    Error,
    Success
)
from configurations.dependencies import (
    get_current_application_user_client,
    get_database
)

from features.friend import services as friend_services
from features.friend.models import FriendshipOutput

router = APIRouter(prefix="/api/v1/friends", tags=["Friend"])


@router.post("/request/{client_id}")
async def request_friend(
    # Path parameters
    client_id: int = Path(..., title="The ID of the client to be requested as friend"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    requested_friend = friend_services.request_friend(database=database, current_user=current_user, client_id=client_id)
    if isinstance(requested_friend, FriendshipOutput):
        return requested_friend
    elif isinstance(requested_friend, Error):
        raise HTTPException(status_code=requested_friend.message.status_code, detail=requested_friend.message.message)


@router.post("/approve/{client_id}")
async def approve_friend(
    # Path parameters
    client_id: int = Path(..., title="The ID of the client to be approved as friend"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    approved_friend = friend_services.approve_friend(database=database, current_user=current_user, client_id=client_id)
    if isinstance(approved_friend, FriendshipOutput):
        return approved_friend
    elif isinstance(approved_friend, Error):
        raise HTTPException(status_code=approved_friend.message.status_code, detail=approved_friend.message.message)


@router.get("")
async def get_friends(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    friends = friend_services.get_friends(database=database, current_user=current_user)
    if isinstance(friends, List):
        return friends
    elif isinstance(friends, Error):
        raise HTTPException(status_code=friends.message.status_code, detail=friends.message.message)


@router.delete("/{friend_id}")
async def delete_friend(
    # Path parameters
    friend_id: int = Path(..., title="The ID of the friend to be deleted"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    deleted_friendship = friend_services.delete_friend(
        database=database,
        current_user=current_user,
        client_id=friend_id
    )

    if isinstance(deleted_friendship, Error):
        raise HTTPException(
            status_code=deleted_friendship.message.status_code,
            detail=deleted_friendship.message.message
        )
    elif isinstance(deleted_friendship, Success):
        return Response(None, status_code=deleted_friendship.message.status_code)


@router.get("/feeds")
async def get_friends_feeds(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    friends_feeds = friend_services.get_friends_feeds(database=database, current_user=current_user)
    if isinstance(friends_feeds, List):
        return friends_feeds
    elif isinstance(friends_feeds, Error):
        raise HTTPException(status_code=friends_feeds.message.status_code, detail=friends_feeds.message.message)


@router.get("/non-friended-clients")
async def get_non_friended_clients(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass


@router.get("/pending-friendships")
async def get_pending_friendships(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass
