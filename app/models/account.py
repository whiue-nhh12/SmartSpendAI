from db.base_class import Base
from sqlalchemy import (DECIMAL,ForeignKey,CheckConstraint)
from decimal import Decimal
from core.exceptions import MyExeption
from sqlalchemy.orm import(relationship,Mapped,mapped_column,validates)
from typing import (List)
from .user import User
from .transaction import Transaction

class Account(Base):
    __tablename__ = "accounts"
    account_id : Mapped[int]=mapped_column(primary_key=True)
    account_name : Mapped[str]
    balance : Mapped[Decimal] = mapped_column(DECIMAL(12,2),CheckConstraint("balance > 0"),insert_default=0,server_default = "0")
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="account",uselist=False)
    transaction : Mapped[List["Transaction"]] = relationship(back_populates="transaction")

    @validates("balance")
    def check_balance(self,amount : Decimal):
        if amount < 0 :
            raise ValueError("Balance khong hop le")
        return amount
    def withdraw (self,amount : Decimal):
        if amount > self.balance:
            raise MyExeption("So du khong du")
        if amount <0 :
            raise MyExeption("So tien khong hop le")
        self.balance -= amount
    def deposit(self,amount : Decimal):
        if amount < 0 :
            raise ValueError("So tien can nap khong hop le")
        self.balance += amount