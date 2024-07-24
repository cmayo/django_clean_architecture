import pytest

from src.messenger.infrastructure.message_bus.simple_query_bus import SimpleQueryBus
from src.messenger.tests.infrastructure.message_bus.fixtures import (
    ExampleQueryHandler,
    ExampleQuery,
)


def test_handler_is_executed() -> None:
    # arrange
    query_bus = SimpleQueryBus()

    def _get_query_handler() -> ExampleQueryHandler:
        return ExampleQueryHandler()

    query_bus.register(ExampleQuery, _get_query_handler)

    # act
    result = query_bus.dispatch(ExampleQuery(id=1))

    # assert
    assert result == 1


def test_should_raise_exception_if_not_registered_query() -> None:
    # arrange
    query_bus = SimpleQueryBus()

    # assert
    with pytest.raises(Exception):
        query_bus.dispatch(ExampleQuery(id=1))


def test_should_raise_exception_if_already_registered_handler() -> None:
    # arrange
    query_bus = SimpleQueryBus()
    query_bus.register(ExampleQuery, ExampleQueryHandler)

    # assert
    with pytest.raises(Exception):
        query_bus.register(ExampleQuery, ExampleQueryHandler)
