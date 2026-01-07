from pydantic import BaseModel,Field
from typing import Annotated

class Token(BaseModel):
    access_token : Annotated[str,Field(title="access_token")]
    token_type : Annotated[str,Field(title="token_type")]

class TokenDate(BaseModel):
    username : str