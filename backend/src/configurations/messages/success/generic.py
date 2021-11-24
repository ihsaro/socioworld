from enum import Enum
from fastapi import status

from configurations.messages.models import Message


class GenericSuccessMessages(Enum):
    OBJECT_DELETED = Message(message="Object has been deleted successfully", status_code=status.HTTP_204_NO_CONTENT)
