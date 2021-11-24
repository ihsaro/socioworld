from sqlalchemy.orm import Session

from configurations.messages.error.generic import GenericErrorMessages
from configurations.messages.error.service.friend import FriendServiceErrorMessages
from configurations.types import Error

from features.authentication import selectors as authentication_selectors
from features.authentication.entities import ApplicationUser
from features.friend import repositories as friend_repositories
from features.friend.entities import Friendship
from features.friend.mappers import (
    map_friendship_to_friendship_output
)


def request_friend(*, database: Session, current_user: ApplicationUser, client_id: int):
    current_user_client_id = authentication_selectors.get_client_user_from_application_user_id(
        database=database,
        application_user_id=current_user.id
    ).id

    requested_user_client = authentication_selectors.get_client_user_from_client_id(
        database=database,
        client_id=client_id
    )

    if requested_user_client is None:
        return Error(
            code=FriendServiceErrorMessages.CLIENT_REQUESTED_DOES_NOT_EXIST.name,
            message=FriendServiceErrorMessages.CLIENT_REQUESTED_DOES_NOT_EXIST.value
        )

    friendship = friend_repositories.get_friendship(
        database=database,
        client_one_id=current_user_client_id,
        client_two_id=client_id
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
    else:
        return requested_friendship


def approve_friend(*, database: Session, current_user: ApplicationUser, client_id: int):
    pass
