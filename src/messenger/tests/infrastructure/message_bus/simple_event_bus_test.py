from unittest.mock import Mock

import pytest

from src.messenger.infrastructure.message_bus.simple_event_bus import SimpleEventBus
from src.messenger.tests.infrastructure.message_bus.fixtures import (
    FirstExampleEventHandler,
    SecondExampleEventHandler,
    ExampleEvent,
)


def test_handler_is_executed() -> None:
    # arrange
    event_bus = SimpleEventBus()
    handler_mock = Mock(spec_set=FirstExampleEventHandler)
    event_bus.register(ExampleEvent, lambda: handler_mock)

    # act
    event_bus.dispatch(ExampleEvent(id=1))

    # assert
    handler_mock.handle.assert_called_once_with(ExampleEvent(id=1))


def test_multiple_handler_are_executed() -> None:
    # arrange
    event_bus = SimpleEventBus()
    first_handler_mock = Mock(spec_set=FirstExampleEventHandler)
    second_handler_mock = Mock(spec_set=SecondExampleEventHandler)
    event_bus.register(ExampleEvent, lambda: first_handler_mock)
    event_bus.register(ExampleEvent, lambda: second_handler_mock)

    # act
    event_bus.dispatch(ExampleEvent(id=1))

    # assert
    first_handler_mock.handle.assert_called_once_with(ExampleEvent(id=1))
    second_handler_mock.handle.assert_called_once_with(ExampleEvent(id=1))


def test_should_raise_exception_if_not_registered_event() -> None:
    # arrange
    event_bus = SimpleEventBus()

    # assert
    with pytest.raises(Exception):
        event_bus.dispatch(ExampleEvent(id=1))
