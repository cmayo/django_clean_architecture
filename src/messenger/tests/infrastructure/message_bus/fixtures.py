from dataclasses import dataclass

from src.messenger.application.message_bus.command import Command, CommandHandler
from src.messenger.application.message_bus.event import Event, EventHandler
from src.messenger.application.message_bus.query import Query, QueryHandler


@dataclass(frozen=True)
class ExampleCommand(Command):
    id: int


class ExampleCommandHandler(CommandHandler[ExampleCommand]):
    def handle(self, command: ExampleCommand) -> None:
        pass


@dataclass(frozen=True)
class ExampleQuery(Query):
    id: int


class ExampleQueryHandler(QueryHandler[ExampleQuery, int]):
    def handle(self, query: ExampleQuery) -> int:
        return query.id


@dataclass(frozen=True)
class ExampleEvent(Event):
    id: int


class FirstExampleEventHandler(EventHandler[ExampleQuery]):
    def handle(self, event: ExampleEvent) -> None:
        pass


class SecondExampleEventHandler(EventHandler[ExampleQuery]):
    def handle(self, event: ExampleEvent) -> None:
        pass
