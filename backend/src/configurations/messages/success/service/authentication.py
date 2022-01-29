from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class AuthenticationServiceSuccessMessages(Enum):
    TOKEN_BLACKLISTED = Message(message="Token has been blacklisted", status_code=status.HTTP_200_OK)
