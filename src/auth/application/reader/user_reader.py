from typing import Union

from src.auth.domain.exception import UserNotFoundException
from src.auth.domain.model import User
from src.auth.domain.repository import UserRepository


class UserReader:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user(self, username: str) -> Union[User, None]:
        try:
            user = self._user_repository.get_user(username)
        except UserNotFoundException:
            user = None

        return user
