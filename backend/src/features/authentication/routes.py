from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from configurations.dependencies import get_database
from configurations.types import Error

from features.authentication.models import (
    LoginInput,
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


@router.post("/login")
async def login(credentials: LoginInput):
    pass


@router.post("/forgot-password")
async def forgot_password():
    pass
