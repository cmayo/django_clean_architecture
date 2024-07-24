from src.demo.application.use_case.add import AddQuery, AddQueryHandler
from src.messenger import messenger_facade
from src.messenger.application.message_bus.query import QueryBus


class Factory:
    def get_query_bus(self) -> QueryBus:
        query_bus = messenger_facade.create_query_bus()
        query_bus.register(AddQuery, self._create_add_query_handler)

        return query_bus

    def _create_add_query_handler(self) -> AddQueryHandler:
        return AddQueryHandler()


factory = Factory()
