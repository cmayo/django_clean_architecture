from typing import Union

from src.auth.domain.exception import UserNotFoundException
from src.auth.domain.model import User
from src.auth.domain.repository import UserRepository

fake_users_db = {
    "test_user": {
        "username": "test_user",
        "full_name": "Test Test",
        "email": "test@example.com",
        "password": "secret",
        "active": True,
    },
    "test_disabled_user": {
        "username": "test_disabled_user",
        "full_name": "Test Disabled User",
        "email": "disabled_user@example.com",
        "password": "secret",
        "active": False,
    },
}


class InMemoryUserRepository(UserRepository):
    def get_user_with_password(self, username: str, password: str) -> Union[User, None]:
        if (
            username in fake_users_db
            and fake_users_db[username]["password"] == password
        ):
            user_dict = fake_users_db[username]
            return User(**user_dict)

    def get_user(self, username: str) -> User:
        if username not in fake_users_db:
            raise UserNotFoundException()

        user_dict = fake_users_db[username]
        return User(**user_dict)
