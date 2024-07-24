from ninja.security import HttpBearer

from src.auth.application.reader.user_reader import UserReader
from src.auth.application.use_case.authenticate_user import (
    AuthenticateUserQueryHandler,
    AuthenticateUserQuery,
)
from src.auth.domain.repository import UserRepository
from src.auth.infrastructure.auth.token_authenticator import TokenAuthenticator
from src.auth.infrastructure.persistence.database.repository import DbUserRepository
from src.messenger import messenger_facade
from src.messenger.application.message_bus.event import EventBus
from src.messenger.application.message_bus.query import QueryBus


class Factory:
    def get_event_bus(self) -> EventBus:
        return messenger_facade.get_event_bus()

    def get_query_bus(self) -> QueryBus:
        query_bus = messenger_facade.create_query_bus()
        query_bus.register(
            AuthenticateUserQuery, self._create_authenticate_user_query_handler
        )

        return query_bus

    def _create_authenticate_user_query_handler(self) -> AuthenticateUserQueryHandler:
        return AuthenticateUserQueryHandler(
            self._create_user_repository(),
        )

    def _create_user_repository(self) -> UserRepository:
        return DbUserRepository()

    def _create_user_reader(self) -> UserReader:
        return UserReader(self._create_user_repository())

    def create_token_authenticator(self) -> HttpBearer:
        return TokenAuthenticator(self._create_user_reader())


factory = Factory()
