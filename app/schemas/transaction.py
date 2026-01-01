from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated
from decimal import Decimal
from .user import UserResponse

class TransactionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    amount : Annotated[Decimal,Field(title="amount")]
    description : Annotated[str,Field(title="description")]

class TransactionResponse(TransactionBase):
    transaction_id : int 
    category_id : int 
    account_id : int
    user : UserResponse

