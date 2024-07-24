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


items = [{"item_id": i} for i in range(1000)]

@main.get("/items")
async def get_items():
    return {"items": items}
