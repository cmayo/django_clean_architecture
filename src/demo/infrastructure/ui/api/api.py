from src.auth.infrastructure.auth import (
    APIAuthenticatedRouter,
    HttpApiRequest,
)
from src.demo.application.use_case.add import AddQuery
from src.demo.infrastructure.factory import factory

router = APIAuthenticatedRouter()


@router.get("/add")
def add(request: HttpApiRequest, a: int, b: int):
    query_bus = factory.get_query_bus()
    result = query_bus.dispatch(AddQuery(a, b))
    return {"result": result}
