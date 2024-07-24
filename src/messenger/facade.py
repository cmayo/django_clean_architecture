from .application.message_bus.event import EventBus
from .application.message_bus.query import QueryBus
from .infrastructure.factory import factory


class Facade:
    event_bus: EventBus | None = None

    def create_query_bus(self) -> QueryBus:
        return factory.create_query_bus()

    def get_event_bus(self) -> EventBus:
        if not self.event_bus:
            self.event_bus = factory.create_eventBus()

        return self.event_bus
