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
    pass


@router.get("")
async def get_friends(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass


@router.get("/feeds")
async def get_friends_feeds(
    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass


@router.post("/{friend_id}")
async def get_friend(
    # Path parameters
    friend_id: int = Path(..., title="The ID of the friend to be obtained"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass


@router.delete("/{friend_id}")
async def delete_friend(
    # Path parameters
    friend_id: int = Path(..., title="The ID of the friend to be deleted"),

    # Dependencies
    current_user=Depends(get_current_application_user_client),
    database=Depends(get_database)
):
    pass
