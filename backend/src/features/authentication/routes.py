from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Request,
    Response,
    status
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from configurations.dependencies import (
    get_database,
    get_current_application_user,
    get_current_application_user_admin
)
from configurations.types import Error, Success

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
        raise HTTPException(status_code=registered_user.message.status_code, detail=registered_user.message.message)


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
        raise HTTPException(status_code=registered_user.message.status_code, detail=registered_user.message.message)


@router.post("/login", include_in_schema=False, response_model=TokenCreated)
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
        raise HTTPException(status_code=token_created.message.status_code, detail=token_created.message.message)
    else:
        return {
            "access_token": token_created.access_token,
            "token_type": token_created.token_type
        }


@router.post("/change-password")
async def change_password(
    # Dependencies
    database: Session = Depends(get_database),
    current_user: ApplicationUser = Depends(get_current_application_user)
):
    pass


# Should change
@router.post("/get-access-token", include_in_schema=False)
async def get_access_token(
    # Response object
    response: Response,

    # Dependencies
    database: Session = Depends(get_database),

    # Body parameter
    credentials: LoginCredentials = Body(..., title="Login credentials"),
):
    token_created = authentication_services.login(
        database=database,
        login_credentials=LoginCredentials(
            username=credentials.username,
            password=credentials.password
        )
    )

    if isinstance(token_created, Error):
        raise HTTPException(status_code=token_created.message.status_code, detail=token_created.message.message)
    else:
        response.set_cookie(
            "Authorization",
            f"{token_created.token_type} {token_created.access_token}",
            httponly=True,
            samesite="strict"
        )
        return {
            "access_token": token_created.access_token,
            "token_type": token_created.token_type
        }


@router.get("/is-authenticated", include_in_schema=False)
async def is_authenticated(
    # Request object
    request: Request,

    # Dependencies
    current_user: ApplicationUser = Depends(get_current_application_user)
):
    return {}


@router.post("/blacklist-token", include_in_schema=False)
async def blacklist_token(
    # Request object
    request: Request,

    # Response object
    response: Response,

    # Dependencies
    current_user: ApplicationUser = Depends(get_current_application_user),
    database: Session = Depends(get_database)
):
    if request.headers.get("Authorization"):
        token = request.headers.get("Authorization")
    elif request.cookies.get("Authorization"):
        token = request.cookies.get("Authorization")    

    blacklisted_token = authentication_services.blacklist_token(token=token, database=database)
    if isinstance(blacklisted_token, Success):
        response.delete_cookie("Authorization")
        return blacklisted_token
    elif isinstance(blacklisted_token, Error):
        raise HTTPException(
            status_code=blacklisted_token.message.status_code,
            detail=blacklisted_token.message.message
        )
