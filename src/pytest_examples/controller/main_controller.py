from fastapi import APIRouter
from ..utils.documentation import Documentation
from ..dto import (
    MainOutput, MainOutputSchema
)
from ..services.main_service import MainService

main = APIRouter(prefix="/main", tags=["Main"])
mainDocumentation = Documentation.create(success=MainOutputSchema)

@main.get(
    "/",
    description="",
    responses=mainDocumentation,
)
async def start():
    return MainOutput.create(MainService.start())