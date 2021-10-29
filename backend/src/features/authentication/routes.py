from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from configurations.dependencies import get_database

from features.authentication.models import (
    LoginInput, 
    RegisterInput,
    RegisterOutput
)

from features.authentication.services import (
    register as register_service
)

router = APIRouter(prefix="/api/v1/authentication", tags=["Authentication"])


@router.post("/login")
async def login(credentials: LoginInput):
    pass


@router.post("/register", response_model=RegisterOutput)
async def register(user_details: RegisterInput, database: Session = Depends(get_database)):
    return register_service(user_details=user_details, database=database)


@router.post("/forgot-password")
async def forgot_password():
    pass
