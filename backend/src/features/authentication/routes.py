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

from configurations.dependencies import get_database
from configurations.types import Error

from features.authentication.models import (
    LoginInput,
    LoginOutput,
    RegisterInput,
    RegisterOutput
)

from features.authentication import services as authentication_services

router = APIRouter(prefix="/api/v1/authentication", tags=["Authentication"])


@router.post("/register", response_model=RegisterOutput, status_code=status.HTTP_201_CREATED)
async def register(
    register_input: RegisterInput = Body(
        ...,
        title="User details for registration in the system",
        description="User details for registration in the system"
    ),

    # Dependencies
    database: Session = Depends(get_database),
):
    register_output = authentication_services.register(register_input=register_input, database=database)
    if isinstance(register_output, RegisterOutput):
        return register_output
    elif isinstance(register_output, Error):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=register_output.message)


@router.post("/login", response_model=LoginOutput)
async def login(
    # Dependencies
    credentials: OAuth2PasswordRequestForm = Depends(),
    database: Session = Depends(get_database)
):
    login_output = authentication_services.login(
        database=database,
        login_input=LoginInput(
            username=credentials.username,
            password=credentials.password
        )
    )

    if isinstance(login_output, Error):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=login_output.message)
    else:
        return {"access_token": login_output.access_token, "token_type": login_output.token_type}


@router.post("/forgot-password")
async def forgot_password():
    pass
