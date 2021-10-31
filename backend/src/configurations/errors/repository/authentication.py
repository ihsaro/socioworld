from enum import Enum


class AuthenticationRepositoryErrors(Enum):
    DUPLICATE_USER = "User already exists"
