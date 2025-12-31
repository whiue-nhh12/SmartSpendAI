from sqlalchemy import (INTEGER,VARCHAR,ForeignKey,CheckConstraint,Enum as SQLENUM)
from sqlalchemy.orm import(relationship,Mapped,mapped_column,validates)
from typing import Optional
from db.base_class import Base
from .user import User
from core.exceptions import MyExeption
from core.enums import Role
from core.validators import check_positive_number

class UserProfile(Base):
    __tablename__ = "user_profiles"
    userprofile_id: Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] =relationship(back_populates="userprofile")
    role : Mapped[Role] =  mapped_column(SQLENUM(Role),insert_default=Role.BASIC,server_default=Role.BASIC.value)
    name : Mapped[str] = mapped_column(VARCHAR(75),insert_default="Bob")
    age : Mapped[int] = mapped_column(INTEGER,CheckConstraint("age>0"))
    location : Mapped[Optional[str]]
    
    @validates("age")
    def check_age(self,age : int):
        return check_positive_number(age)
    def updaterole(self,new_role : str):
        if self.role != Role.ADMIN :
            raise MyExeption("Ban khong co quyen sua")
        if self.role == Role.ADMIN and new_role != Role.BASIC:
            raise ValueError("Ban khong the ha quyen Admin")