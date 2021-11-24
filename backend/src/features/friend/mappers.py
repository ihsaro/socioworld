from features.friend.entities import Friendship
from features.friend.models import FriendshipOutput


def map_friendship_to_friendship_output(*, friendship: Friendship) -> FriendshipOutput:
    return FriendshipOutput(
        client_id=friendship.client_id,
        friend_id=friendship.friend_id,
        requested=friendship.requested,
        approved=friendship.approved
    )
