from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from ..decorator.auth import Auth
from ..dto import (
    SignInOutputSchema, InternalErrorSchema, SignInSchema, SignInInput
)
from ..services.security_service import SecurityService


http_bearer = HTTPBearer()

security = APIRouter(prefix="/security", tags=["security"])
@security.post(
    "/sign-in",
    description="",
    responses = {
        200: {"model": SignInOutputSchema},
        400: {"model": InternalErrorSchema}
    },
    include_in_schema=True
)
async def sign_in(body: SignInSchema):
    input : SignInSchema = SignInInput.create(body)
    return await SecurityService().sign_in(input)

@security.get(
    "/get-me",
    description="",
    responses = {
        200: {"model": SignInOutputSchema},
        400: {"model": InternalErrorSchema}
    },
    include_in_schema=True
)
async def get_me(token: dict = Depends(http_bearer)):
    await Auth(token)
    return await SecurityService().get_me()