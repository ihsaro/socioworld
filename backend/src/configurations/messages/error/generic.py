from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class GenericErrorMessages(Enum):
    SERVER_ERROR = Message(message="Server error, please try again", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    INTEGRITY_ERROR = Message(
        message="Data integrity error, please check the data and try again",
        status_code=status.HTTP_400_BAD_REQUEST
    )
    OBJECT_NOT_FOUND = Message(message="Object not found", status_code=status.HTTP_404_NOT_FOUND)
    UNAUTHORIZED_OBJECT_ACCESS = Message(
        message="User does not have the rights to access this object",
        status_code=status.HTTP_403_FORBIDDEN
    )
