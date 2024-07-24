from typing import Optional, List

from ninja import Router

from src.auth.infrastructure.factory import factory


class APIAuthenticatedRouter(Router):
    def __init__(self, *, tags: Optional[List[str]] = None) -> None:
        auth = factory.create_token_authenticator()
        super().__init__(auth=auth, tags=tags)
