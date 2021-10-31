from typing import Union

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from configurations.errors.repository.authentication import AuthenticationRepositoryErrors
from configurations.types import Error

from features.authentication.entities import ApplicationUser


def register(*, database: Session, application_user: ApplicationUser) -> Union[ApplicationUser, Error]:
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
