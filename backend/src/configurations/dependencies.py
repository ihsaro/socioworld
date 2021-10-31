from fastapi import (
    Depends,
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from sqlalchemy.orm import Session

from configurations.constants.security import (
    ALGORITHM,
    SECRET_KEY
)
from configurations.database import SessionLocal
from configurations.errors.service.authentication import AuthenticationServiceErrors

from features.authentication import selectors as authentication_selectors


def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="api/v1/authentication/login")),
    database: Session = Depends(get_database)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=AuthenticationServiceErrors.INVALID_CREDENTIALS.value,
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        application_user_id: int = payload.get("sub")
        if application_user_id is None:
            raise credentials_exception
        application_user = authentication_selectors.get_application_user(
            database=database,
            application_user_id=application_user_id
        )
        if application_user is None:
            raise credentials_exception
        return application_user
    except JWTError:
        raise credentials_exception
