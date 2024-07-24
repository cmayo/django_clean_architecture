from unittest import mock

from src.auth.application.use_case.authenticate_user import (
    AuthenticateUserQuery,
    AuthenticateUserQueryHandler,
)
from src.auth.domain.model import User
from src.auth.domain.repository import UserRepository


@mock.patch("src.auth.application.use_case.authenticate_user.UserRepository")
def test_user_is_invalid(mock_user_repository: UserRepository):
    # Arrange
    authenticate_user_query = AuthenticateUserQuery(
        "invalid_username", "invalid_password"
    )
    mock_user_repository.get_user_with_password.return_value = None

    # Act
    authenticate_user_query_handler = AuthenticateUserQueryHandler(
        mock_user_repository,
    )
    authenticated_user = authenticate_user_query_handler.handle(authenticate_user_query)

    # Assert
    assert authenticated_user is None


@mock.patch("src.auth.application.use_case.authenticate_user.UserRepository")
def test_user_is_valid_but_not_active(mock_user_repository: UserRepository):
    # Arrange
    user = User(username="username", active=False)
    authenticate_user_query = AuthenticateUserQuery("username", "password")
    mock_user_repository.get_user_with_password.return_value = user

    # Act
    authenticate_user_query_handler = AuthenticateUserQueryHandler(
        mock_user_repository,
    )
    authenticated_user = authenticate_user_query_handler.handle(authenticate_user_query)

    # Assert
    assert authenticated_user is None


@mock.patch("src.auth.application.use_case.authenticate_user.UserRepository")
def test_user_password_does_not_match(mock_user_repository: UserRepository):
    # Arrange
    user = User(username="username", password="password", active=True)
    authenticate_user_query = AuthenticateUserQuery("username", "invalid_password")
    mock_user_repository.get_user_with_password.return_value = None

    # Act
    authenticate_user_query_handler = AuthenticateUserQueryHandler(
        mock_user_repository,
    )
    authenticated_user = authenticate_user_query_handler.handle(authenticate_user_query)

    # Assert
    assert authenticated_user is None


@mock.patch("src.auth.application.use_case.authenticate_user.UserRepository")
def test_user_is_valid_and_password_match(mock_user_repository: UserRepository):
    # Arrange
    user = User(username="username", password="password", active=True)
    authenticate_user_query = AuthenticateUserQuery("username", "invalid_password")
    mock_user_repository.get_user_with_password.return_value = user

    # Act
    authenticate_user_query_handler = AuthenticateUserQueryHandler(
        mock_user_repository,
    )
    authenticated_user = authenticate_user_query_handler.handle(authenticate_user_query)

    # Assert
    assert user.username == authenticated_user.username
