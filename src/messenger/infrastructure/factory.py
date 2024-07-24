from src.messenger.application.message_bus.event import EventBus
from src.messenger.application.message_bus.query import QueryBus
from src.messenger.infrastructure.message_bus.simple_event_bus import SimpleEventBus
from src.messenger.infrastructure.message_bus.simple_query_bus import SimpleQueryBus


class Factory:
    def create_query_bus(self) -> QueryBus:
        return SimpleQueryBus()

    def create_eventBus(self) -> EventBus:
        return SimpleEventBus()


factory = Factory()
