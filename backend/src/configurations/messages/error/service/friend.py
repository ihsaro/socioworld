from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class FriendServiceErrorMessages(Enum):
    FRIENDSHIP_EXISTS = Message(
        message="Friendship already exists between the 2 clients",
        status_code=status.HTTP_400_BAD_REQUEST
    )
    FRIENDSHIP_DOES_NOT_EXIST = Message(
        message="Friendship does not exist between the 2 clients",
        status_code=status.HTTP_404_NOT_FOUND
    )
    FRIENDSHIP_ALREADY_APPROVED = Message(
        message="Friendship already approved between the 2 clients",
        status_code=status.HTTP_400_BAD_REQUEST
    )
    CLIENT_REQUESTED_DOES_NOT_EXIST = Message(
        message="Client requested does not exist",
        status_code=status.HTTP_404_NOT_FOUND
    )
    TARGET_CLIENT_CANNOT_BE_CURRENT_USER = Message(
        message="Target client cannot be current user",
        status_code=status.HTTP_400_BAD_REQUEST
    )
