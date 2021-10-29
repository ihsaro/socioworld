from fastapi import (
    APIRouter,
    Body,
    Depends,
    Response,
    status
)

from sqlalchemy.orm import Session

from configurations.dependencies import get_database

from features.authentication.models import (
    LoginInput,
    RegisterInput,
    RegisterOutput
)

from features.authentication import services as authentication_services

router = APIRouter(prefix="/api/v1/authentication", tags=["Authentication"])


@router.post("/register", response_model=RegisterOutput)
async def register(
        # Response object
        response: Response,

        # Payload
        register_input: RegisterInput = Body(
            ...,
            title="User details for registration in the system",
            description="User details for registration in the system"
        ),

        # Dependencies
        database: Session = Depends(get_database),
):
    created_user = authentication_services.register(register_input=register_input, database=database)
    if created_user is not None:
        response.status_code = status.HTTP_201_CREATED
        return created_user
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@router.post("/login")
async def login(credentials: LoginInput):
    pass


@router.post("/forgot-password")
async def forgot_password():
    pass
