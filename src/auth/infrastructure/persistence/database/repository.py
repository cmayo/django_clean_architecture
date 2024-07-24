from typing import Union

from django.core.exceptions import ObjectDoesNotExist

from src.auth.domain.model import User
from src.auth.domain.repository import UserRepository
from . import models


class DbUserRepository(UserRepository):
    def get_user_with_password(self, username: str, password: str) -> Union[User, None]:
        try:
            user = models.User.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

        if not user.check_password(password):
            return None

        return User(**user.__dict__)

    def get_user(self, username: str) -> User:
        pass
