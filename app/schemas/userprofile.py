from pydantic import BaseModel,Field,ConfigDict
from typing import Annotated,Optional

class UserProfile(BaseModel):
    name : Annotated[str,Field(title="fullname")]
    age : Annotated[int,Field(gt=0,title="age")]
    role : Annotated[str,Field(title="role")]
    model_config = ConfigDict(from_attributes=True)

class UserProfileResponse(UserProfile):
    userprofile_id : Annotated[int,Field(title="userprofile_id")]
    location : str
class UserProfileCreate(UserProfile):
    location:Optional[str]

class UserProfile_Update(BaseModel):
    userprofile_id : int
    name : Optional[str]
    age : Optional[str]
    role : Optional[str]
    location : Optional[str]
    model_config = ConfigDict(from_attributes=True)
