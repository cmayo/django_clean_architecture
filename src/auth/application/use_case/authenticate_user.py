from dataclasses import dataclass
from typing import Union

from src.auth.domain.model import User
from src.auth.domain.repository import UserRepository
from src.messenger.application.message_bus.query import QueryHandler, Query


@dataclass(frozen=True)
class AuthenticateUserQuery(Query):
    username: str
    password: str


class AuthenticateUserQueryHandler(
    QueryHandler[AuthenticateUserQuery, Union[User, None]]
):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def handle(self, query: AuthenticateUserQuery) -> Union[User, None]:
        user = self._user_repository.get_user_with_password(
            query.username, query.password
        )

        if user is None or not user.active:
            return None

        return user
