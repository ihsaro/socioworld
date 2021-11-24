from sqlalchemy.orm import Session

from features.authentication import repositories as authentication_repositories
from features.authentication.entities import (
    ApplicationUser,
    Client
)


def get_application_user(*, database: Session, application_user_id: int) -> ApplicationUser:
    return authentication_repositories.get_application_user(database=database, application_user_id=application_user_id)


def get_client_user_from_application_user_id(*, database: Session, application_user_id: int) -> Client:
    return authentication_repositories.get_client_user_from_application_user_id(
        database=database,
        application_user_id=application_user_id
    )


def get_client_user_from_client_id(*, database: Session, client_id: int) -> Client:
    return authentication_repositories.get_client_user_from_client_id(
        database=database,
        client_id=client_id
    )
