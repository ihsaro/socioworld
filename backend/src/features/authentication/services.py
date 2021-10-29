from sqlalchemy.orm.session import Session

from features.authentication.mappers import (
    map_application_user_to_register_output,
    map_register_input_to_application_user
)
from features.authentication.models import (
    RegisterInput,
    RegisterOutput
)

from features.authentication import repositories as authentication_repositories


def register(*, database: Session, register_input: RegisterInput) -> RegisterOutput:
    application_user = map_register_input_to_application_user(register_input=register_input)
    created_user = authentication_repositories.register(database=database, application_user=application_user)
    if created_user is not None:
        return map_application_user_to_register_output(application_user=created_user)
    else:
        return None
