from fastapi import APIRouter, Response, Depends

from app.auth import auth
from app.users import schemas

from app.users.dao import UserDAO, UnverifiedUsersDAO
from app.auth.dao import PermissionsDAO
from app.profiles.dao import ProfileDAO

from app.users.dependencies import get_current_user, generate_verify_code
from app.exceptions import (
    UserAlreadyExistsException,
    UserLoginException,
    PermissionDeniedException,
)

from app.smtp.smtp import send_confirmation_code


router_user = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router_user.post("/register", status_code=201)
async def register_unverified_user(
    user_data: schemas.UnverifyUser, verify_code=Depends(generate_verify_code)
):
    existing_user = await UnverifiedUsersDAO.find_one_or_none(
        email=user_data.email
    ) or await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = auth.get_password_hash(user_data.password)
    await send_confirmation_code(user_data.email, "Регистрация", verify_code)
    await UnverifiedUsersDAO.create(
        email=user_data.email,
        password=hashed_password,
        verify_code=verify_code,
    )
    return {"details": "Сообщение с подтверждением отправленно на почту"}


@router_user.post("/verify", status_code=201)
async def register_user(email: str, verify_code):
    unverified_user = await UnverifiedUsersDAO.find_one_or_none(email=email)
    if not unverified_user:
        return {"details": "Пользователь не найден"}
    if unverified_user.verify_code != verify_code:
        return {"details": "Неверный код подтверждения"}
    user_data = schemas.User(
        email=unverified_user.email, password=unverified_user.password
    )
    await UserDAO.create(
        email=user_data.email,
        password=user_data.password,
    )
    return {"details": "Пользователь успешно создан"}


@router_user.post("/login")
async def login_user(response: Response, user_data: schemas.User):
    user = await UserDAO.find_one_or_none(email=user_data.email)
    if not (user and auth.verify_password(user_data.password, user.password)):
        raise UserLoginException
    permissions = await PermissionsDAO.find_all_permissions_by_role(user.role_id)
    access_token = auth.create_access_token(
        {"sub": str(user.uuid), "permissions": permissions}
    )
    response.set_cookie("assistant_fishing", access_token, httponly=True)
    return access_token


@router_user.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("assistant_fishing")
    return {"details": "Пользователь вышел из системы"}


@router_user.get("/all")
async def get_user_by_id(current_user=Depends(get_current_user)):
    if current_user.role_id == 1:
        return await UserDAO.find_all()
    raise PermissionDeniedException
