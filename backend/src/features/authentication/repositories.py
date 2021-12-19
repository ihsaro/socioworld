from typing import Union

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.session import Session

from configurations.messages.error.generic import GenericErrorMessages
from configurations.messages.error.repository.authentication import AuthenticationRepositoryErrorMessages
from configurations.types import Error

from features.authentication.entities import (
    Admin,
    ApplicationUser,
    Client,
    Roles
)


def create_application_user(*, database: Session, application_user: ApplicationUser) -> Union[ApplicationUser, Error]:
    try:
        database.add(application_user)
        database.commit()
        if application_user.role == Roles.ADMIN:
            database.add(Admin(application_user_id=application_user.id))
        elif application_user.role == Roles.CLIENT:
            database.add(Client(application_user_id=application_user.id))
        database.commit()
        return application_user
    except IntegrityError:
        return Error(
            code=AuthenticationRepositoryErrorMessages.DUPLICATE_USER.name,
            message=AuthenticationRepositoryErrorMessages.DUPLICATE_USER.value
        )


def get_application_user_for_login(*, database: Session, username: str) -> Union[ApplicationUser, Error]:
    try:
        return database.query(ApplicationUser).filter(
            ApplicationUser.username == username).first()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def get_application_user(*, database: Session, application_user_id: int) -> Union[ApplicationUser, Error]:
    try:
        return database.query(ApplicationUser).filter(ApplicationUser.id == application_user_id).first()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def get_client_user_from_application_user_id(*, database: Session, application_user_id: int) -> Union[Client, Error]:
    try:
        return database.query(Client).filter(Client.application_user_id == application_user_id).first()
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)


def get_client_user_from_client_id(*, database: Session, client_id: int) -> Union[Client, Error]:
    try:
        return database.query(Client).get(client_id)
    except SQLAlchemyError:
        return Error(code=GenericErrorMessages.SERVER_ERROR.name, message=GenericErrorMessages.SERVER_ERROR.value)
