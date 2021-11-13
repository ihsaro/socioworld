from typing import Union

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.session import Session

from configurations.errors.generic import GenericErrors
from configurations.errors.repository.authentication import AuthenticationRepositoryErrors
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
            code=AuthenticationRepositoryErrors.DUPLICATE_USER.name,
            message=AuthenticationRepositoryErrors.DUPLICATE_USER.value
        )


def get_application_user_for_login(*, database: Session, username: str, password: str) -> Union[ApplicationUser, Error]:
    try:
        return database.query(ApplicationUser).filter(
            ApplicationUser.username == username).filter(
            ApplicationUser.password == password).first()
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def get_application_user(*, database: Session, application_user_id: int) -> Union[ApplicationUser, Error]:
    try:
        return database.query(ApplicationUser).filter(ApplicationUser.id == application_user_id).first()
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def get_client_user_from_application_user_id(*, database: Session, application_user_id: int) -> Union[Client, Error]:
    try:
        return database.query(Client).filter(Client.application_user_id == application_user_id).first()
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)
