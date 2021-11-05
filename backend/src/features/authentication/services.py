import os

from datetime import datetime, timedelta
from typing import Union

from jose import JWTError, jwt

from sqlalchemy.orm.session import Session

from configurations.constants.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY
)
from configurations.errors.service.authentication import AuthenticationServiceErrors
from configurations.types import Error

from features.authentication.entities import (
    ApplicationUser
)
from features.authentication.mappers import (
    map_application_user_to_registered_user,
    map_user_registration_details_to_application_user
)
from features.authentication.models import (
    LoginCredentials,
    TokenCreated,
    UserRegistrationDetails,
    RegisteredUser
)

from features.authentication import repositories as authentication_repositories


def __generate_jwt_token__(*, to_encode: dict):
    to_encode_copy = to_encode.copy()
    expires_in = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode_copy.update({"exp": expires_in})
    return jwt.encode(to_encode_copy, SECRET_KEY, algorithm=ALGORITHM)


def login(*, database: Session, login_credentials: LoginCredentials) -> Union[TokenCreated, Error]:
    application_user = authentication_repositories.get_application_user_for_login(
        database=database,
        username=login_credentials.username,
        password=login_credentials.password
    )
    if application_user is None:
        return Error(
            code=AuthenticationServiceErrors.INVALID_CREDENTIALS.name,
            message=AuthenticationServiceErrors.INVALID_CREDENTIALS.value
        )
    access_token = __generate_jwt_token__(to_encode={"sub": str(application_user.id)})
    return TokenCreated(access_token=access_token, token_type="bearer")


def register(*, database: Session, user_registration_details: UserRegistrationDetails) -> Union[RegisteredUser, Error]:
    application_user = authentication_repositories.create_application_user(
        database=database,
        application_user=map_user_registration_details_to_application_user(
            user_registration_details=user_registration_details)
    )
    if isinstance(application_user, ApplicationUser):
        return map_application_user_to_registered_user(application_user=application_user)
    elif isinstance(application_user, Error):
        return application_user
