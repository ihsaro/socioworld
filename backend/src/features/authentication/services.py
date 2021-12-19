from datetime import datetime, timedelta
from typing import Union

from jose import jwt

from passlib.context import CryptContext

from sqlalchemy.orm.session import Session

from configurations.constants.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY
)
from configurations.messages.error.service.authentication import AuthenticationServiceErrorMessages
from configurations.types import Error

from features.authentication.entities import (
    ApplicationUser,
    Roles
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


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def __generate_jwt_token__(*, to_encode: dict):
    to_encode_copy = to_encode.copy()
    expires_in = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode_copy.update({"exp": expires_in})
    return jwt.encode(to_encode_copy, SECRET_KEY, algorithm=ALGORITHM)


def __get_hashed_password__(*, password: str) -> str:
    return pwd_context.hash(password)


def __verify_password__(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def login(*, database: Session, login_credentials: LoginCredentials) -> Union[TokenCreated, Error]:
    application_user = authentication_repositories.get_application_user_for_login(
        database=database,
        username=login_credentials.username
    )
    if application_user is None:
        return Error(
            code=AuthenticationServiceErrorMessages.INVALID_CREDENTIALS.name,
            message=AuthenticationServiceErrorMessages.INVALID_CREDENTIALS.value
        )
    else:
        if __verify_password__(
            plain_password=login_credentials.password,
            hashed_password=application_user.password
        ):
            access_token = __generate_jwt_token__(to_encode={"sub": str(application_user.id)})
            return TokenCreated(access_token=access_token, token_type="bearer")
        else:
            return Error(
                code=AuthenticationServiceErrorMessages.INVALID_CREDENTIALS.name,
                message=AuthenticationServiceErrorMessages.INVALID_CREDENTIALS.value
            )


def register(*, user_registration_details: UserRegistrationDetails, role: Roles, database: Session) -> Union[
    RegisteredUser,
    Error
]:
    application_user_to_be_created = map_user_registration_details_to_application_user(
            user_registration_details=user_registration_details
    )
    application_user_to_be_created.password = __get_hashed_password__(password=application_user_to_be_created.password)
    application_user_to_be_created.role = role
    application_user = authentication_repositories.create_application_user(
        database=database,
        application_user=application_user_to_be_created
    )
    if isinstance(application_user, ApplicationUser):
        return map_application_user_to_registered_user(application_user=application_user)
    elif isinstance(application_user, Error):
        return application_user
