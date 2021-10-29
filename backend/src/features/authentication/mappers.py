from features.authentication.entities import ApplicationUser
from features.authentication.models import RegisterInput, RegisterOutput


def map_register_input_to_application_user(*, register_input: RegisterInput) -> ApplicationUser:
    return ApplicationUser(
        first_name=register_input.first_name,
        last_name=register_input.last_name,
        date_of_birth=register_input.date_of_birth,
        is_active=True,
        email=register_input.email,
        username=register_input.username,
        password=register_input.password
    )


def map_application_user_to_register_output(*, application_user: ApplicationUser) -> RegisterOutput:
    return RegisterOutput(
        id=application_user.id,
        first_name=application_user.first_name,
        last_name=application_user.last_name,
        date_of_birth=application_user.date_of_birth,
        email=application_user.email,
        username=application_user.username
    )