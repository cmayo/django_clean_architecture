from typing import Union

from src.auth.domain.model import User


class UserRepository:
    def get_user_with_password(self, username: str, password: str) -> Union[User, None]:
        raise NotImplementedError()

    def get_user(self, username: str) -> User:
        raise NotImplementedError()
