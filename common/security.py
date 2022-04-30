from datetime import datetime, timedelta
from typing import List, Tuple, Union, Optional
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
import bcrypt
from jose import JWTError, jwt
from sqlalchemy.sql.expression import select
from models import Session
from repository.authRepository import authRepository
from settings import JWT_PREFIX, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from models.user import User

class OAuth2PasswordJWT(OAuth2PasswordBearer):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[dict] = None,
        auto_error: bool = True,
    ):
        super().__init__(
            tokenUrl=tokenUrl,
            scopes=scopes,
            scheme_name=scheme_name,
            auto_error=auto_error,
        )

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme != JWT_PREFIX:
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": JWT_PREFIX},
                )
            else:
                return None
        return param

oauth2_scheme = OAuth2PasswordJWT(tokenUrl="auth/sign-in")


async def generate_jwt_token_from_user(user:User)->str:
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {'username': user.username, 'email': user.email, 'exp': expire}
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

def get_user_from_jwt_token(jwt_token:str)->Union[User, None]:
    try:
        payload = jwt.decode(token=jwt_token, key=SECRET_KEY,algorithms=ALGORITHM)
        username = payload.get('username')
        user = authRepository.get_user(user=username)
    except JWTError:
        return None
    except Exception as e:
        print(e)
        return None
    
    return user

