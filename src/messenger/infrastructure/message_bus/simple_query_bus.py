from inspect import signature
from typing import Type, Dict, Any, Callable

from src.messenger.application.message_bus.query import QueryBus, Query, QueryHandler


class SimpleQueryBus(QueryBus):
    def __init__(self):
        self._handlers: Dict[Type[Query], Callable[[], QueryHandler]] = {}

    def register(
        self,
        query: Type[Query],
        handler: Callable[[], QueryHandler] | Type[QueryHandler],
    ) -> None:
        sign = signature(handler)
        if not issubclass(sign.return_annotation, QueryHandler) and not issubclass(
            handler, QueryHandler
        ):
            raise Exception

        if query in self._handlers:
            raise Exception

        self._handlers[query] = handler

    def dispatch(self, query: Query) -> Any:
        try:
            handler = self._handlers[type(query)]
            return handler().handle(query)
        except KeyError:
            raise Exception
