from typing import Type, Dict, Callable, List

from src.messenger.application.message_bus.event import EventBus, Event, EventHandler


class SimpleEventBus(EventBus):
    def __init__(self):
        self._handlers: Dict[
            Type[Event], List[Callable[[], EventHandler] | Type[EventHandler]]
        ] = {}

    def register(
        self,
        event: Type[Event],
        handler: Callable[[], EventHandler] | Type[EventHandler],
    ) -> None:
        self._handlers.setdefault(event, []).append(handler)

    def dispatch(self, event: Event) -> None:
        try:
            handlers = self._handlers[type(event)]
        except KeyError:
            raise Exception

        for handler in handlers:
            handler().handle(event)
