from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder


class SignInSchema(BaseModel):
    userid: str = Field(description="")

class SigniInSchemaRoot(BaseModel):
    __root__: SignInSchema

class SignInInput:
    @staticmethod
    def create(signIn: SignInSchema) -> dict:
        return jsonable_encoder(SigniInSchemaRoot(__root__=signIn))