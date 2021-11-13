from features.authentication.entities import ApplicationUser
from features.authentication.models import UserRegistrationDetails, RegisteredUser


def map_user_registration_details_to_application_user(
    *, user_registration_details: UserRegistrationDetails
) -> ApplicationUser:
    return ApplicationUser(
        first_name=user_registration_details.first_name,
        last_name=user_registration_details.last_name,
        date_of_birth=user_registration_details.date_of_birth,
        is_active=True,
        email=user_registration_details.email,
        username=user_registration_details.username,
        password=user_registration_details.password
    )


def map_application_user_to_registered_user(*, application_user: ApplicationUser) -> RegisteredUser:
    return RegisteredUser(
        id=application_user.id,
        first_name=application_user.first_name,
        last_name=application_user.last_name,
        date_of_birth=application_user.date_of_birth,
        email=application_user.email,
        username=application_user.username
    )
