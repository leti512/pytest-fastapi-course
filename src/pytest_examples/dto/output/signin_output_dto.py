from pydantic import BaseModel, Field

class PayloadSchema(BaseModel):

    token: str = Field(
        description="token JWT to sign in"
    )

class SignInOutputSchema(BaseModel):
    success: bool = Field(
        description="", example=True
    )
    message: str = Field(
        description="",
        example="",
    )
    payload: PayloadSchema = Field(
        description=""
    )