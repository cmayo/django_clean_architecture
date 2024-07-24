from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Event:
    pass


class EventBus:
    def dispatch(self, event: Event) -> Any:
        raise NotImplementedError


class EventHandler[TEvent: Event]:
    def handle(self, event: TEvent) -> None:
        raise NotImplementedError
