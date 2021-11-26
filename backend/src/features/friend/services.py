from typing import (
    List,
    Union
)

from sqlalchemy.orm import Session

from configurations.messages.error.generic import GenericErrorMessages
from configurations.messages.error.service.friend import FriendServiceErrorMessages
from configurations.types import (
    Error,
    Success
)

from features.authentication import selectors as authentication_selectors
from features.authentication.entities import ApplicationUser
from features.friend import repositories as friend_repositories
from features.friend.entities import Friendship
from features.friend.mappers import (
    map_friendship_to_friendship_output
)
from features.friend.models import (
    FriendOutput,
    FriendshipOutput
)


def request_friend(
    *,
    database: Session,
    current_user: ApplicationUser,
    client_id: int
) -> Union[
    FriendshipOutput, Error
]:
    current_user_client_id = authentication_selectors.get_client_user_from_application_user_id(
        database=database,
        application_user_id=current_user.id
    ).id

    friendship = __validate_and_get_friendship__(
        database=database,
        current_user_client_id=current_user_client_id,
        target_client_id=client_id
    )

    if isinstance(friendship, Error) and friendship.code != GenericErrorMessages.OBJECT_NOT_FOUND.name:
        return friendship
    elif isinstance(friendship, Friendship):
        return Error(
            code=FriendServiceErrorMessages.FRIENDSHIP_EXISTS.name,
            message=FriendServiceErrorMessages.FRIENDSHIP_EXISTS.value
        )

    requested_friendship = friend_repositories.add_friendship(
        database=database,
        client_one_id=current_user_client_id,
        client_two_id=client_id
    )

    if isinstance(requested_friendship, Friendship):
        return map_friendship_to_friendship_output(friendship=requested_friendship)
    elif isinstance(requested_friendship, Error):
        return requested_friendship


def approve_friend(
    *,
    database: Session,
    current_user: ApplicationUser,
    client_id: int
) -> Union[
    FriendshipOutput, Error
]:
    current_user_client_id = authentication_selectors.get_client_user_from_application_user_id(
        database=database,
        application_user_id=current_user.id
    ).id

    friendship = __validate_and_get_friendship__(
        database=database,
        current_user_client_id=current_user_client_id,
        target_client_id=client_id
    )

    if isinstance(friendship, Error):
        return Error(
            code=FriendServiceErrorMessages.FRIENDSHIP_DOES_NOT_EXIST.name,
            message=FriendServiceErrorMessages.FRIENDSHIP_DOES_NOT_EXIST.value
        )

    if friendship.approved:
        return Error(
            code=FriendServiceErrorMessages.FRIENDSHIP_ALREADY_APPROVED.name,
            message=FriendServiceErrorMessages.FRIENDSHIP_ALREADY_APPROVED.value
        )

    friendship_approved = friend_repositories.approve_friendship(
        database=database,
        client_one_id=current_user_client_id,
        client_two_id=client_id
    )

    if isinstance(friendship_approved, Friendship):
        return map_friendship_to_friendship_output(friendship=friendship_approved)
    elif isinstance(friendship_approved, Error):
        return friendship_approved


def get_friends(
    *,
    database: Session,
    current_user: ApplicationUser
) -> Union[
    List[FriendOutput], Error
]:
    pass


def delete_friend(
    *,
    database: Session,
    current_user: ApplicationUser,
    client_id: int
) -> Union[
    Success, Error
]:
    current_user_client_id = authentication_selectors.get_client_user_from_application_user_id(
        database=database,
        application_user_id=current_user.id
    ).id

    friendship = __validate_and_get_friendship__(
        database=database,
        current_user_client_id=current_user_client_id,
        target_client_id=client_id
    )

    if isinstance(friendship, Error):
        return friendship

    return friend_repositories.delete_friendship(
        database=database,
        client_one_id=current_user_client_id,
        client_two_id=client_id
    )


def __validate_and_get_friendship__(
    *,
    database: Session,
    current_user_client_id: int,
    target_client_id: int) -> Union[
    Friendship, Error
]:
    if current_user_client_id == target_client_id:
        return Error(
            code=FriendServiceErrorMessages.TARGET_CLIENT_CANNOT_BE_CURRENT_USER.name,
            message=FriendServiceErrorMessages.TARGET_CLIENT_CANNOT_BE_CURRENT_USER.value
        )

    target_client = authentication_selectors.get_client_user_from_client_id(
        database=database,
        client_id=target_client_id
    )

    if target_client is None:
        return Error(
            code=FriendServiceErrorMessages.CLIENT_REQUESTED_DOES_NOT_EXIST.name,
            message=FriendServiceErrorMessages.CLIENT_REQUESTED_DOES_NOT_EXIST.value
        )

    return friend_repositories.get_friendship(
        database=database,
        client_one_id=current_user_client_id,
        client_two_id=target_client_id
    )
