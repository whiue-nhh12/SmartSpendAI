from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated

class UserBase(BaseModel):
    username : Annotated[str,Field(title="username")]
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password : Annotated[str,Field(title="password")]
    repassword : Annotated[str,Field(title="repassword")]


class UserResponse(UserBase):
    user_id : Annotated[str,Field(title="user_id")]

class UserUpdate(UserBase):
    password : str
    new_password : Annotated[str,Field(title="new_password")]


