from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated,Optional
from core.enums import Transaction_Types
from .budget import BudgetResponse
from .user import UserResponse

class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    category_name : Annotated[str,Field(title="category_name")]
    type_transaction : Annotated[Transaction_Types,Field(title="types_transaction")]
    budget : Annotated[Optional["BudgetResponse"],Field(title="budget")]

class CategoryResponse(CategoryBase):
    category_id : int 
    user : UserResponse

class CategoryUpdate(BaseModel):
    category_id : int 
    new_category_name : Optional[str]
    type_transaction : Optional[Transaction_Types]
    
