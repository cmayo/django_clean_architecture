from dataclasses import dataclass
from typing import TypeVar, Generic


@dataclass(frozen=True)
class Command:
    pass


class CommandBus:
    def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class CommandHandler[TCommand: Command]:
    def handle(self, command: TCommand) -> None:
        raise NotImplementedError
