from sqlalchemy.orm.session import Session

from features.authentication.entities import ApplicationUser


def register(*, database: Session, application_user: ApplicationUser) -> ApplicationUser:
    database.add(application_user)
    database.commit()
    database.refresh(application_user)
    return application_user
