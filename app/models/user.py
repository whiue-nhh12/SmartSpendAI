from db.base_class import Base
from sqlalchemy.orm import(relationship,Mapped,mapped_column)
from .userprofile import UserProfile
from typing import (List)
from .transaction import Transaction
from .account import Account
from .category import Category
from .user_settings import User_Settings

class User(Base):
    __tablename__ = "users"
    user_id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] =  mapped_column(nullable=False)
    password : Mapped[str] = mapped_column(nullable=False)
    userprofile : Mapped["UserProfile"] = relationship(back_populates="user",uselist=False)
    account : Mapped[List["Account"]] = relationship(back_populates="user")
    user_setting : Mapped["User_Settings"] = relationship(back_populates="user_setting",uselist=False)
    category : Mapped[List["Category"]] = relationship(back_populates="category")
    transaction : Mapped[List["Transaction"]] = relationship(back_populates="transaction")