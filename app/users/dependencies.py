from random import randint
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, Request

from app.config import settings
from app.users.dao import UserDAO


def generate_verify_code():
    return randint(100000, 999999)


def get_token(request: Request):
    token = request.cookies.get("assistant_fishing")
    if not token:
        raise HTTPException(status_code=401, detail="User not authorized")
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=401, detail="User not authorized")
    user_id: str = payload.get("sub")
    permissions = payload.get("permissions")
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authorized")
    user = await UserDAO.find_one_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user, permissions
