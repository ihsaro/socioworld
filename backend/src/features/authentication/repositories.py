from typing import Union

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.session import Session

from configurations.errors.generic import GenericErrors
from configurations.errors.repository.authentication import AuthenticationRepositoryErrors
from configurations.types import Error

from features.authentication.entities import (
    Admin,
    ApplicationUser,
    User,
    Roles
)


def create_application_user(*, database: Session, application_user: ApplicationUser) -> Union[ApplicationUser, Error]:
    try:
        database.add(application_user)
        database.commit()
        if application_user.role == Roles.ADMIN:
            database.add(Admin(application_user_id=application_user.id))
        elif application_user.role == Roles.USER:
            database.add(User(application_user_id=application_user.id))
        database.commit()
        return application_user
    except IntegrityError:
        return Error(
            code=AuthenticationRepositoryErrors.DUPLICATE_USER.name,
            message=AuthenticationRepositoryErrors.DUPLICATE_USER.value
        )


def create_user(*, database: Session, user: User) -> Union[User, Error]:
    try:
        database.add(user)
        database.commit()
        return user
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


def create_user(*, database: Session, admin: Admin) -> Union[Admin, Error]:
    try:
        database.add(admin)
        database.commit()
        return admin
    except SQLAlchemyError:
        return Error(code=GenericErrors.SERVER_ERROR.name, message=GenericErrors.SERVER_ERROR.value)


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
