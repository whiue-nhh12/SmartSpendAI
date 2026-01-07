from pwdlib import PasswordHash
from typing import Optional
from schemas.token import Token
import jwt
from datetime import timedelta,datetime,timezone

SECRET_KEY = "11a483529a469595b166bec8c9b9aa842336ad07e4e65974b5ff9fad6b3970a5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
password_hasher = PasswordHash.recommended()

def password_hash (plain_password : str):
    return password_hasher.hash(plain_password)

def verify_password(plain_password : str,hashed_password : str):
    return password_hasher.verify(plain_password,hashed_password)

def create_access_token(data : dict , exprie_delta : Optional[timedelta] = None):
    to_encode = data.copy()
    if exprie_delta is None:
        exprie_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":datetime.now(timezone.utc)+exprie_delta})
    access_token = jwt.encode(to_encode,SECRET_KEY,ALGORITHM)
    return Token(access_token=access_token,token_type="bearer")

