from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class AuthenticationServiceErrorMessages(Enum):
    INVALID_CREDENTIALS = Message(message="Credentials are Invalid", status_code=status.HTTP_401_UNAUTHORIZED)
    INVALID_ADMINISTRATOR = Message(message="Invalid administrator", status_code=status.HTTP_403_FORBIDDEN)
    INVALID_CLIENT = Message(message="Invalid client", status_code=status.HTTP_403_FORBIDDEN)
