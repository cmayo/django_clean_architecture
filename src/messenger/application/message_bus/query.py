from dataclasses import dataclass
from typing import TypeVar, Generic, Any


@dataclass(frozen=True)
class Query:
    pass


class QueryBus:
    def dispatch(self, query: Query) -> Any:
        raise NotImplementedError


class QueryHandler[TQuery: Query, TResultQuery: Any]:
    def handle(self, query: TQuery) -> TResultQuery:
        raise NotImplementedError
