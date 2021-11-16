from enum import Enum


class GenericErrors(Enum):
    SERVER_ERROR = "Server error, please try again"
    OBJECT_NOT_FOUND = "Object not found"
    UNAUTHORIZED_OBJECT_ACCESS = "User does not have the rights to access this object"
