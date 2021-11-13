from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    status
)
from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from configurations.dependencies import (
    get_database,
    get_current_application_user_admin
)
from configurations.types import Error

from features.authentication.entities import (
    ApplicationUser,
    Roles
)
from features.authentication.models import (
    LoginCredentials,
    TokenCreated,
    UserRegistrationDetails,
    RegisteredUser
)

from features.authentication import services as authentication_services

router = APIRouter(prefix="/api/v1/authentication", tags=["Authentication"])


@router.post("/register-client", response_model=RegisteredUser, status_code=status.HTTP_201_CREATED)
async def register_client(
    register_input: UserRegistrationDetails = Body(
        ...,
        title="User details for registration in the system",
        description="User details for registration in the system"
    ),

    # Dependencies
    database: Session = Depends(get_database),
):
    registered_user = authentication_services.register(
        user_registration_details=register_input,
        role=Roles.CLIENT,
        database=database
    )
    if isinstance(registered_user, RegisteredUser):
        return registered_user
    elif isinstance(registered_user, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=registered_user.message)


@router.post("/register-admin", response_model=RegisteredUser, status_code=status.HTTP_201_CREATED)
async def register_admin(
    register_input: UserRegistrationDetails = Body(
        ...,
        title="Admin registration in the system",
        description="Admin registration in the system"
    ),

    # Dependencies
    database: Session = Depends(get_database),
    current_user: ApplicationUser = Depends(get_current_application_user_admin)
):
    registered_user = authentication_services.register(
        user_registration_details=register_input,
        role=Roles.ADMIN,
        database=database
    )
    if isinstance(registered_user, RegisteredUser):
        return registered_user
    elif isinstance(registered_user, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=registered_user.message)


@router.post("/login", response_model=TokenCreated)
async def login(
    # Dependencies
    credentials: OAuth2PasswordRequestForm = Depends(),
    database: Session = Depends(get_database)
):
    token_created = authentication_services.login(
        database=database,
        login_credentials=LoginCredentials(
            username=credentials.username,
            password=credentials.password
        )
    )

    if isinstance(token_created, Error):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=token_created.message)
    else:
        return {"access_token": token_created.access_token, "token_type": token_created.token_type}


@router.post("/forgot-password")
async def forgot_password():
    pass
