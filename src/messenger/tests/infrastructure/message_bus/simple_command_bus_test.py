from unittest.mock import Mock

import pytest

from src.messenger.infrastructure.message_bus.simple_command_bus import SimpleCommandBus
from src.messenger.tests.infrastructure.message_bus.fixtures import (
    ExampleCommandHandler,
    ExampleCommand,
)


def test_handler_is_executed() -> None:
    # arrange
    command_bus = SimpleCommandBus()
    handler_mock = Mock(spec_set=ExampleCommandHandler)
    command_bus.register(ExampleCommand, lambda: handler_mock)

    # act
    command_bus.dispatch(ExampleCommand(id=1))

    # assert
    handler_mock.handle.assert_called_once_with(ExampleCommand(id=1))


def test_should_raise_exception_if_not_registered_command() -> None:
    # arrange
    command_bus = SimpleCommandBus()

    # assert
    with pytest.raises(Exception):
        command_bus.dispatch(ExampleCommand(id=1))


def test_should_raise_exception_if_already_registered_handler() -> None:
    # arrange
    command_bus = SimpleCommandBus()
    command_bus.register(ExampleCommand, ExampleCommandHandler)

    # assert
    with pytest.raises(Exception):
        command_bus.register(ExampleCommand, ExampleCommandHandler())
