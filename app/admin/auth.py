from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.auth import auth
from app.auth.dao import PermissionsDAO
from app.users.dependencies import get_current_user

from app.config import settings


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await auth.aunthenticate_user(email, password)
        if user:
            permissions = await PermissionsDAO.find_all_permissions_by_role(
                user.role_id
            )
            if "can_use_admin_site" in permissions:
                access_token = auth.create_access_token(
                    {
                        "sub": str(user.user_id),
                        "permissions": permissions,
                    }
                )
                request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        user, permissions = await get_current_user(token)

        if not user or permissions == None:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
        if "can_use_admin_site" not in permissions:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
