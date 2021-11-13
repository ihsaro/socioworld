from enum import Enum


class AuthenticationServiceErrors(Enum):
    INVALID_CREDENTIALS = "Credentials are Invalid"
    INVALID_ADMINISTRATOR = "User is not a valid administrator"

