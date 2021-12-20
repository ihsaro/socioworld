from typing import (
    List,
    Union
)

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError

from configurations.types import (
    Error,
    Success
)
from configurations.messages.error.generic import GenericErrorMessages
from configurations.messages.success.generic import GenericSuccessMessages

from features.authentication.entities import (
    ApplicationUser,
    Client
)
from features.feed.entities import Feed
from features.friend.entities import Friendship
from features.friend.models import (
    FriendFeed,
    FriendOutput
)


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


def delete_friendship(database: Session, client_one_id: int, client_two_id: int) -> Union[Success, Error]:
    try:
        friendship_relationship_client_side = database.query(Friendship).filter(
            Friendship.client_id == client_one_id
        ).filter(
            Friendship.friend_id == client_two_id
        ).first()

        friendship_relationship_friend_side = database.query(Friendship).filter(
            Friendship.client_id == client_two_id
        ).filter(
            Friendship.friend_id == client_one_id
        ).first()

        database.delete(friendship_relationship_client_side)
        database.delete(friendship_relationship_friend_side)
        database.commit()
        return Success(
            code=GenericSuccessMessages.OBJECT_DELETED.name,
            message=GenericSuccessMessages.OBJECT_DELETED.value
        )
    except UnmappedInstanceError:
        return Error(
            code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
            message=GenericErrorMessages.OBJECT_NOT_FOUND.value
        )
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def get_friends(*, database: Session, current_user_id: int) -> Union[List[FriendOutput], Error]:
    try:
        friends: List[FriendOutput] = []

        for friendship, client, application_user in database.query(
            Friendship, Client, ApplicationUser
        ).filter(
            Friendship.client_id == current_user_id
        ).filter(
            Friendship.approved
        ).filter(
            Friendship.friend_id == Client.id
        ).filter(
            Client.application_user_id == ApplicationUser.id
        ).all():
            friends.append(
                FriendOutput(
                    client_id=client.id,
                    first_name=application_user.first_name,
                    last_name=application_user.last_name
                )
            )

        return friends
    except UnmappedInstanceError:
        return Error(
            code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
            message=GenericErrorMessages.OBJECT_NOT_FOUND.value
        )
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


# It works, though it needs to be refactored since the first_name and last_name should be aggregated in the join
def get_friends_feeds(*, database: Session, current_user_id: int) -> Union[List[FriendFeed], Error]:
    try:
        friends_feeds: List[FriendFeed] = []

        feeds = database.query(
            Feed
        ).join(
            Client
        ).join(
            Friendship, Friendship.friend_id == Client.id and Friendship.client_id == current_user_id
        ).join(
            ApplicationUser, Client.application_user_id == ApplicationUser.id
        ).filter(
            Friendship.approved
        ).filter(
            Feed.published
        ).all()

        for feed in feeds:
            friends_feeds.append(
                FriendFeed(
                    client_id=feed.client_id,
                    first_name=database.query(
                        ApplicationUser
                    ).join(
                        Client, Client.application_user_id == ApplicationUser.id
                    ).filter(
                        Client.id == feed.client_id
                    ).first().first_name,
                    last_name=database.query(
                        ApplicationUser
                    ).join(
                        Client, Client.application_user_id == ApplicationUser.id
                    ).filter(
                        Client.id == feed.client_id
                    ).first().last_name,
                    feed_title=feed.title,
                    feed_description=feed.description,
                    created_timestamp=feed.created_timestamp
                )
            )

        return friends_feeds
    except UnmappedInstanceError:
        return Error(
            code=GenericErrorMessages.OBJECT_NOT_FOUND.name,
            message=GenericErrorMessages.OBJECT_NOT_FOUND.value
        )
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)
