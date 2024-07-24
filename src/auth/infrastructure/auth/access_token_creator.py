from datetime import timedelta, datetime, timezone

from jose import jwt
from pydantic import BaseModel

from src.auth.domain.model import User
from src.auth.infrastructure.auth.token import AuthToken


class Token(BaseModel):
    access_token: str
    token_type: str


class AccessTokenCreator:
    def create_access_token(self, user: User) -> str:
        expires_delta = timedelta(minutes=5)

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        token = AuthToken(exp=int(expire.timestamp()), sub=user.username)
        encoded_jwt = jwt.encode(token.__dict__, "secret", algorithm="HS256")
        return encoded_jwt
