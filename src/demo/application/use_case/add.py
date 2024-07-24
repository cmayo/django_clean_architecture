from dataclasses import dataclass

from src.messenger.application.message_bus.query import Query, QueryHandler


@dataclass(frozen=True)
class AddQuery(Query):
    a: int
    b: int


class AddQueryHandler(QueryHandler[AddQuery, int]):
    def handle(self, query: AddQuery) -> int:
        return query.a + query.b
