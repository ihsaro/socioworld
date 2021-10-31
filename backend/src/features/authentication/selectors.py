from sqlalchemy.orm import Session

from features.authentication import repositories as authentication_repositories
from features.authentication.entities import ApplicationUser


def get_application_user(*, database: Session, application_user_id: int) -> ApplicationUser:
    return authentication_repositories.get_application_user(database=database, application_user_id=application_user_id)
