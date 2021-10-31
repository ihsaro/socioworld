from typing import Union

from sqlalchemy.orm.session import Session

from configurations.types import Error

from features.authentication.entities import (
    ApplicationUser
)
from features.authentication.mappers import (
    map_application_user_to_register_output,
    map_register_input_to_application_user
)
from features.authentication.models import (
    RegisterInput,
    RegisterOutput
)

from features.authentication import repositories as authentication_repositories


def register(*, database: Session, register_input: RegisterInput) -> Union[RegisterOutput, Error]:
    application_user = map_register_input_to_application_user(register_input=register_input)
    register_entity = authentication_repositories.register(database=database, application_user=application_user)
    if isinstance(register_entity, ApplicationUser):
        return map_application_user_to_register_output(application_user=register_entity)
    elif isinstance(register_entity, Error):
        return register_entity
