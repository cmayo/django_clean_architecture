from typing import Type, Dict, Callable

from src.messenger.application.message_bus.command import (
    CommandBus,
    Command,
    CommandHandler,
)


class SimpleCommandBus(CommandBus):
    def __init__(self):
        self._handlers: Dict[
            Type[Command], Callable[[], CommandHandler] | Type[CommandHandler]
        ] = {}

    def register(
        self,
        command: Type[Command],
        handler: Callable[[], CommandHandler] | Type[CommandHandler],
    ):
        if command in self._handlers:
            raise Exception

        self._handlers[command] = handler

    def dispatch(self, command: Command) -> None:
        try:
            handler = self._handlers[type(command)]
            handler().handle(command)
        except KeyError:
            raise Exception
