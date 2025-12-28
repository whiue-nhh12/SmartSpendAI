from sqlalchemy import (INTEGER,String,VARCHAR,TIMESTAMP,DECIMAL,ForeignKey,CheckConstraint,Enum as SQLENUM)
from datetime import datetime
import sqlalchemy
from decimal import Decimal
from enum import Enum
from sqlalchemy.orm import(relationship,Mapped,mapped_column,DeclarativeBase,registry,validates)
from typing import Optional
from typing import (Literal,Annotated,List)

class MyExeption(Exception):
    def __init__(self, error : str):
        super().__init__(error)

class Role(Enum):
    BASIC = "Basic_User"
    VIP = "Vip"
    ADMIN = "Admin"
class Screen_Mode(Enum):
    lightmode = "lightmode"
    darkmode = "darkmode"

class Background_Color(Enum):
    green = "green"
    black = "black"
    yellow = "yellow"
    red = "red"

class Transaction_Types(Enum):
    WITHDRAW = "withdraw"
    DEPOSITE = "Deposite"
    
mapped_registry = registry()
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    user_id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] =  mapped_column(nullable=False)
    password : Mapped[str] = mapped_column(nullable=False)
    userprofile : Mapped["UserProfile"] = relationship(back_populates="user_profile",uselist=False)
    account : Mapped[List["Account"]] = relationship(back_populates="accounts")
    user_setting : Mapped["User_Settings"] = relationship(back_populates="user_setting",uselist=False)
    category : Mapped[List["Category"]] = relationship(back_populates="category")
    transaction : Mapped[List["Transaction"]] = relationship(back_populates="transaction")
@mapped_registry.mapped
class UserProfile:
    __tablename__ = "user_profiles"
    userprofile_id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    User : Mapped["User"] =relationship(back_populates="userprofile")
    role : Mapped[Role] =  mapped_column(sqlalchemy.Enum(Role),insert_default=Role.BASIC,server_default=Role.BASIC.value)
    name : Mapped[str] = mapped_column(VARCHAR(75),insert_default="Bob")
    age : Mapped[int] = mapped_column(INTEGER,CheckConstraint("age>0"))
    location : Mapped[Optional[str]]
    
    @validates("age")
    def check_age(self,age : int):
        if age <= 0 :
            raise ValueError("So tuoi khong hop le")
        return age
    def updaterole(self,new_role : str):
        if self.role != Role.ADMIN :
            raise MyExeption("Ban khong co quyen sua")
        if self.role == Role.ADMIN and new_role != Role.BASIC:
            raise ValueError("Ban khong the ha quyen Admin")
        
@mapped_registry.mapped
class Account:
    __tablename__ = "accounts"
    account_id : Mapped[int]=mapped_column(primary_key=True)
    account_name : Mapped[str]
    balance : Mapped[Decimal] = mapped_column(DECIMAL(12,2),CheckConstraint("balance > 0"),insert_default=0,server_default = "0")
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user",uselist=False)
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
    def deposite(self,amount : Decimal):
        if amount < 0 :
            raise ValueError("So tien can nap khong hop le")
        self.balance += amount
class User_Settings(Base):
    __tablename__="user_settings"
    usersettings_id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user",uselist=True)
    screenmode : Mapped[Screen_Mode]
    background_color : Mapped[Background_Color]
    font : Mapped[int] = mapped_column(INTEGER,CheckConstraint("font > 0 "))
    
    @validates("font")
    def check_font(self,font : int) :
        if font < 0 :
            raise ValueError("Font chu khong hop le")
        return font

@mapped_registry.mapped
class Category:
    __tablename__ = "categorys"
    category_id : Mapped[int] = mapped_column(primary_key=True)
    categorry_name : Mapped[str] = mapped_column(String(55),insert_default="Category 1")
    type_transaction : Mapped[Transaction_Types] = mapped_column(SQLENUM(Transaction_Types))
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user : Mapped["User"] = relationship(back_populates="user",uselist=False)

class Transaction(Base):
    __tablename__="transactions"
    transaction_id : Mapped[int] = mapped_column(primary_key=True)
    category_id : Mapped[int] = mapped_column(ForeignKey("categorys.category_id"))
    catagory : Mapped["Category"] = relationship(back_populates="category",uselist=False)
    amount : Mapped[Decimal] = mapped_column(DECIMAL(12,2))
    created_at : Mapped[datetime] = mapped_column(TIMESTAMP,insert_default=datetime.now())
    description : Mapped[str] = mapped_column(String(200),server_default="")
    account_id : Mapped[int] = mapped_column(ForeignKey("accounts.account_id"))
    account : Mapped["Account"] = relationship(back_populates="account",uselist=False)
    user_id : Mapped[int]= mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user")



    


