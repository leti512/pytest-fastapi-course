from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

class MainOutputSchema(BaseModel):
    success: bool = Field(
        description="", example=True
    )
    message: str = Field(
        description="",
        example="ok!",
    )
    version: str  = Field(
        description="",
        example="",
    )

class MainOutput:
    @staticmethod
    def create(main: MainOutputSchema) -> dict:
        return jsonable_encoder(main)