from typing import Union

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from configurations.types import Error
from configurations.messages.error.generic import GenericErrorMessages

from features.friend.entities import Friendship


def get_friendship(*, database: Session, client_one_id: int, client_two_id: int) -> Union[Friendship, Error]:
    try:
        friendship = database.query(Friendship).filter(
            Friendship.client_id == client_one_id
        ).filter(
            Friendship.friend_id == client_two_id
        ).first()

        if friendship is None:
            return Error(
                code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
                message=GenericErrorMessages.OBJECT_NOT_FOUND.value
            )
        return friendship
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def add_friendship(*, database: Session, client_one_id: int, client_two_id: int) -> Union[Friendship, Error]:
    try:
        friendship_relationship_client_side = Friendship(
            client_id=client_one_id,
            friend_id=client_two_id,
            requested=True,
            approved=False
        )

        friendship_relationship_friend_side = Friendship(
            client_id=client_two_id,
            friend_id=client_one_id,
            requested=False,
            approved=False
        )

        database.add(friendship_relationship_client_side)
        database.add(friendship_relationship_friend_side)

        database.commit()
        return friendship_relationship_client_side
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def approve_friendship(database: Session, client_one_id: int, client_two_id: int) -> Union[Friendship, Error]:
    try:
        friendship_relationship_client_side = database.query(Friendship).filter(
            Friendship.client_id == client_one_id
        ).filter(
            Friendship.friend_id == client_two_id
        )

        friendship_relationship_friend_side = database.query(Friendship).filter(
            Friendship.client_id == client_two_id
        ).filter(
            Friendship.friend_id == client_one_id
        )

        friendship_relationship_client_side.update({"approved": True})
        friendship_relationship_friend_side.update({"approved": True})

        database.commit()

        return friendship_relationship_client_side.first()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)
