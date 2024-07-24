from typing import Optional, Any

from django.http import HttpRequest
from jose import jwt, JWTError, ExpiredSignatureError
from jose.exceptions import JWTClaimsError
from ninja.security import HttpBearer

from src.auth.application.reader.user_reader import UserReader
from src.auth.infrastructure.auth.token import AuthToken


class TokenAuthenticator(HttpBearer):
    def __init__(self, user_reader: UserReader) -> None:
        super().__init__()
        self._user_reader = user_reader

    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        try:
            decoded_token = AuthToken(**jwt.decode(token, "secret", "HS256"))
        except (JWTError, ExpiredSignatureError, JWTClaimsError):
            return None

        user = self._user_reader.get_user(decoded_token.sub)
        return user
