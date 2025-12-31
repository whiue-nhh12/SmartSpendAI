from sqlalchemy import (String,ForeignKey,Enum as SQLENUM)
from sqlalchemy.orm import(relationship,Mapped,mapped_column)
from typing import Optional
from typing import (List)
from db.base_class import Base
from .user import User
from .budget import Budget
from core.enums import Transaction_Types
from .transaction import Transaction

class Category(Base):
    __tablename__ = "categories"
    category_id : Mapped[int] = mapped_column(primary_key=True)
    category_name : Mapped[str] = mapped_column(String(55),insert_default="Category 1")
    type_transaction : Mapped[Transaction_Types] = mapped_column(SQLENUM(Transaction_Types))
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user",uselist=False)
    budget : Mapped[Optional["Budget"]] = relationship(back_populates="budget")
    transactions : Mapped[List["Transaction"]]= relationship(back_populates="category")
