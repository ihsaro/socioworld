from typing import Union

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.session import Session

from configurations.errors.repository.authentication import AuthenticationRepositoryErrors
from configurations.types import Error

from features.authentication.entities import ApplicationUser


def create_application_user(*, database: Session, application_user: ApplicationUser) -> Union[ApplicationUser, Error]:
    try:
        database.add(application_user)
        database.commit()
        database.refresh(application_user)
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
        return Error()


def get_application_user(*, database: Session, application_user_id: int) -> Union[ApplicationUser, Error]:
    try:
        return database.query(ApplicationUser).filter(ApplicationUser.id == application_user_id).first()
    except SQLAlchemyError:
        return Error()
