from typing import Union

from django.http import HttpRequest

from src.auth.domain.model import User


class HttpApiRequest(HttpRequest):
    def __init__(self):
        super().__init__()
        self.auth: Union[User, None] = None
