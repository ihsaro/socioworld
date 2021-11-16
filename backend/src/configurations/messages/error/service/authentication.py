from enum import Enum


class AuthenticationServiceErrorMessages(Enum):
    INVALID_CREDENTIALS = "Credentials are Invalid"
    INVALID_ADMINISTRATOR = "Invalid administrator"
    INVALID_CLIENT = "Invalid client"

