from enum import Enum


class FriendServiceErrorMessages(Enum):
    FRIENDSHIP_EXISTS = "Friendship already exists between the 2 clients"
    CLIENT_REQUESTED_DOES_NOT_EXIST = "Client requested does not exists"
