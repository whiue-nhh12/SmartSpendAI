from sqlalchemy import (String,TIMESTAMP,DECIMAL,ForeignKey,CheckConstraint,)
from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import(relationship,Mapped,mapped_column,validates)
from db.base_class import Base
from .category import Category
from .account import Account
from .user import User
from core.validators import check_positive_number

class Transaction(Base):
    __tablename__="transactions"
    transaction_id : Mapped[int] = mapped_column(primary_key=True)
    category_id : Mapped[int] = mapped_column(ForeignKey("categories.category_id"))
    category : Mapped["Category"] = relationship(back_populates="transactions",uselist=False)
    amount : Mapped[Decimal] = mapped_column(DECIMAL(12,2),CheckConstraint("amount > 0"))
    created_at : Mapped[datetime] = mapped_column(TIMESTAMP,insert_default=datetime.now())
    description : Mapped[str] = mapped_column(String(200),server_default="")
    account_id : Mapped[int] = mapped_column(ForeignKey("accounts.account_id"))
    account : Mapped["Account"] = relationship(back_populates="account",uselist=False)
    user_id : Mapped[int]= mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user")

    @validates("amount")
    def check_amount(self,amount:Decimal):
        return check_positive_number(amount)