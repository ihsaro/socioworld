from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import user

from features.authentication.entities import ApplicationUser
from features.authentication.models import RegisterInput

from features.authentication.repositories import (
    register as register_repository
)


def register(*, database: Session, user_details: RegisterInput) -> ApplicationUser:
    return register_repository(database=database, application_user=ApplicationUser(
        first_name=user_details.first_name,
        last_name=user_details.last_name,
        date_of_birth=user_details.date_of_birth,
        email=user_details.email,
        username=user_details.username,
        password=user_details.password
    ))
