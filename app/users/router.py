from fastapi import APIRouter, Response, Depends

from app.auth import auth
from app.users import schemas
from app.users.dao import UserDAO
from app.users.dependencies import get_current_user
from app.exceptions import UserAlreadyExistsException, UserLoginException


router_user = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router_user.post("/register", status_code=201)
async def register_user(user_data: schemas.User):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = auth.get_password_hash(user_data.password)
    new_user = await UserDAO.create(
        email=user_data.email,
        password=hashed_password,
    )
    return {"details": "Пользователь успешно создан"}


@router_user.post("/login")
async def login_user(response: Response, user_data: schemas.User):
    user = await UserDAO.find_one_or_none(email=user_data.email)
    if not (user and auth.verify_password(user_data.password, user.password)):
        raise UserLoginException
    access_token = auth.create_access_token({"sub": str(user.uuid)})
    response.set_cookie("assistant_fishing", access_token, httponly=True)
    return access_token


@router_user.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("assistant_fishing")
    return {"details": "Пользователь вышел из системы"}


@router_user.get("/me")
async def user_me(current_user=Depends(get_current_user)):
    return current_user


@router_user.get("/{user_uuid}")
async def get_user_by_id(user_uuid: str):
    user = await UserDAO.find_one_or_none(uuid=user_uuid)
    return user
