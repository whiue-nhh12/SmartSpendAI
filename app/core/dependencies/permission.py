from .dependencies import get_current_user
from fastapi import Depends
from typing import Annotated
from models.user import User
from fastapi import HTTPException,status

async def get_current_vip_user(user : Annotated[User,Depends(get_current_user)]):
    if user.userprofile.role != "Vip":
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Do not have permission"
        )
    return user

async def get_current_admin_user(user : Annotated[User,Depends(get_current_user)]):
    if user.userprofile.role != "Admin":
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Do not have permission"
        )
    return user

