from django.http import HttpRequest
from ninja import Router, Form
from ninja.errors import AuthenticationError

from src.auth.application.use_case.authenticate_user import AuthenticateUserQuery
from src.auth.infrastructure.auth.access_token_creator import AccessTokenCreator
from src.auth.infrastructure.factory import factory
from src.auth.infrastructure.ui.api.schema import TokenResponse

router = Router()


@router.post(
    "/login",
    response=TokenResponse,
)
def login_for_access_token(
    request: HttpRequest,
    username: Form[str],
    password: Form[str],
) -> TokenResponse:
    user = factory.get_query_bus().dispatch(AuthenticateUserQuery(username, password))
    if not user:
        raise AuthenticationError()

    access_token_creator = AccessTokenCreator()
    access_token = access_token_creator.create_access_token(user)
    return TokenResponse(access_token=access_token, token_type="bearer")
