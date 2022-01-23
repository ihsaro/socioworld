from typing import Optional
from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from starlette.status import HTTP_401_UNAUTHORIZED


class OAuth2PasswordBearerExtended(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        if request.headers.get("Authorization") is not None:
            authorization: str = request.headers.get("Authorization")
        elif request.cookies.get("Authorization") is not None:
            authorization: str = request.cookies.get("Authorization")

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
        return param
