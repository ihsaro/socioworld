from typing import Optional
from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, ExpiredSignatureError
from starlette.status import HTTP_401_UNAUTHORIZED

from configurations.constants.security import SECRET_KEY, ALGORITHM


class OAuth2PasswordBearerExtended(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        if request.headers.get("Authorization") is not None:
            authorization: str = request.headers.get("Authorization")
        elif request.cookies.get("Authorization") is not None:
            authorization: str = request.cookies.get("Authorization")
        else:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None

        token = __decode_jwt_token__(token=param)
        if not token:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return param


def __decode_jwt_token__(*, token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except ExpiredSignatureError:
        return None
