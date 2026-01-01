from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated
from decimal import Decimal
from .user import UserResponse

class AccountResponse(BaseModel):
    account_name : Annotated[str,Field(title="account_name")]
    balance : Annotated[Decimal,Field(title="balance")]
    user : Annotated[UserResponse,Field(title="owner")]
    model_config = ConfigDict(from_attributes=True)

class AccountUpdate(BaseModel):
    account_id : int
    account_name : str
    model_config = ConfigDict(from_attributes=True)

