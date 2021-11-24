from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class AuthenticationRepositoryErrorMessages(Enum):
    DUPLICATE_USER = Message(message="User already exists", status_code=status.HTTP_400_BAD_REQUEST)
