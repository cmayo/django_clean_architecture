from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    password: Union[str, None] = None
    active: Union[bool, None] = None
