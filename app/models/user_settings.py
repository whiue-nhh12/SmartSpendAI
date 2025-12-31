from sqlalchemy import (INTEGER,ForeignKey,CheckConstraint,Enum as SQLENUM)
from sqlalchemy.orm import(relationship,Mapped,mapped_column,validates)
from .user import User
from db.base_class import Base
from core.enums import Screen_Mode,Background_Color
from core.validators import check_positive_number

class User_Settings(Base):
    __tablename__="user_settings"
    usersettings_id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user : Mapped["User"] = relationship(back_populates="user",uselist=True)
    screenmode : Mapped[Screen_Mode] = mapped_column(SQLENUM(Screen_Mode))
    background_color : Mapped[Background_Color] = mapped_column(SQLENUM(Background_Color))
    font : Mapped[int] = mapped_column(INTEGER,CheckConstraint("font > 0 "))
    
    @validates("font")
    def check_font(self,font : int) :
       return check_positive_number(font)