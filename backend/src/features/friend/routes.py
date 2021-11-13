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

router = APIRouter(prefix="/api/v1/friends", tags=["Friend"])


@router.post("/{user_id}")
async def add_friend(
    # Path parameters
    user_id: int = Path(..., title="The ID of the user to be added as friend"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.get("")
async def get_friends(
    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.get("/feeds")
async def get_friends_feeds(
    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.post("/{friend_id}")
async def get_friend(
    # Path parameters
    friend_id: int = Path(..., title="The ID of the friend to be obtained"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass


@router.delete("/{friend_id}")
async def delete_friend(
    # Path parameters
    friend_id: int = Path(..., title="The ID of the friend to be deleted"),

    # Dependencies
    current_user=Depends(get_current_user),
    database=Depends(get_database)
):
    pass
