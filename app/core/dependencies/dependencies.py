from fastapi import (Depends)
from fastapi.security import OAuth2PasswordBearer
from models.user import User
from sqlalchemy import select
from typing import AsyncGenerator
from ..security import verify_password,SECRET_KEY,ALGORITHM
from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import AsyncSessionLocal
from jwt.exceptions import InvalidTokenError
import jwt

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_db () -> AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session 
        except Exception:
            await session.rollback()
            raise 
        finally:
            await session.close()

async def get_user(username : str,db :AsyncSession):
        user = await db.execute(select(User).where(User.username == username))
        return user.scalar_one_or_none()

async def authenticate(username:str,plain_password:str,db : AsyncSession):
     user = await get_user(username,db=db)
     if user is None:
          return False
     if not verify_password(plain_password,user.password):
          return False
     return user

async def get_current_user(db = Depends(get_db),token = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail="could not validate"
    )
    try :
        payload = jwt.decode(token,key=SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = await get_user(username,db)
    if user is None:
         raise credentials_exception
    return user
