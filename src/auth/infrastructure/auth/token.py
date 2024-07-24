from dataclasses import dataclass


@dataclass
class AuthToken:
    exp: int
    sub: str
