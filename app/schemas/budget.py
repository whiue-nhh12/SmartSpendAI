from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated,Optional
from datetime import date
from decimal import Decimal
from core.enums import Status

class BudgetBase(BaseModel):
    model_config =  ConfigDict(from_attributes=True)
    amount : Annotated[Decimal,Field(title="amount")]
    start_date : date
    end_date : date
    status : Status

class BudgetResponse(BudgetBase):
    budget_id : int
    category_id : int

class BudgerUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    budget_id : int
    amount : Optional[Decimal]
    start_date : Optional[date]
    end_date : Optional[date]
    status : Optional[Status]
