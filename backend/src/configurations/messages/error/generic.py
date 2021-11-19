from enum import Enum


class GenericErrorMessages(Enum):
    SERVER_ERROR = "Server error, please try again"
    INTEGRITY_ERROR = "Data integrity error, please check the data and try again"
    OBJECT_NOT_FOUND = "Object not found"
    UNAUTHORIZED_OBJECT_ACCESS = "User does not have the rights to access this object"
