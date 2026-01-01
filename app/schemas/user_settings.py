from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated,Optional
from core.enums import Screen_Mode, Background_Color
from .user import UserResponse

class User_settings_Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    screenmode : Annotated[Screen_Mode,Field(title="screenmode")]
    background_color : Annotated[Background_Color,Field(title="background_color")]
    font : Annotated[int,Field(title="font")]

class User_settings_respone(User_settings_Base):
    usersettingS_id : int 
    user : UserResponse

class User_settings_update(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    usersettings_id : int 
    screenmode : Optional[Screen_Mode]
    background_color : Optional[Background_Color]
    font : Optional[int]