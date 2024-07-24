import json
from http import HTTPStatus

import pytest
from django.test import Client

from src.auth.infrastructure.persistence.database.models import User
from src.auth.infrastructure.ui.api.schema import TokenResponse


@pytest.mark.django_db
def test_login_invalid(client: Client):
    # Act
    response = client.post(
        "/api/auth/login",
        data=dict(username="invalid_user", password="invalid_password"),
    )

    # Assert
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_valid_login_data_return_token(client: Client, django_user_model: User):
    # Arrange
    username = "test_user"
    password = "secret"
    django_user_model.objects.create_user(username=username, password=password)

    # Act
    response = client.post(
        "/api/auth/login", data=dict(username=username, password=password)
    )

    # Assert
    token_response = TokenResponse(**json.loads(response.content))
    assert response.status_code == HTTPStatus.OK
    assert token_response.token_type == "bearer"
    assert token_response.access_token != ""
