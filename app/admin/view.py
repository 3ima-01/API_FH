from sqladmin import ModelView

from app.auth.models import Roles, Permissions
from app.users.models import Users, UnverifiedUsers
from app.profiles.models import Profiles
from app.points.models import Points

from app.users.dependencies import get_current_user


class UsersAdmin(ModelView, model=Users):
    column_exclude_list = [Users.password]
    column_details_exclude_list = [Users.password]

    can_delete = False

    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"

    column_details_exclude_list = [Users.password]

    category = "Пользователи"


class UnverifiedUsersAdmin(ModelView, model=UnverifiedUsers):
    column_exclude_list = [UnverifiedUsers.user_id, UnverifiedUsers.password]
    column_details_exclude_list = [UnverifiedUsers.password]

    can_delete = False

    name = "Не верифицированный пользователь"
    name_plural = "Не верифицированные пользователи"
    icon = "fa-solid fa-user-slash"

    async def is_visible(self, request):
        token = request.session.get("token")
        user = await get_current_user(token)
        if user[1] and "can_use_admin_site" in user[1]:
            return True
        return False


class ProfilesAdmin(ModelView, model=Profiles):
    column_exclude_list = [Profiles.uuid, Profiles.user_id]

    can_delete = False

    name = "Профиль"
    name_plural = "Профили"
    icon = "fa-solid fa-address-card"

    category = "Пользователи"


class PointsAdmin(ModelView, model=Points):
    column_exclude_list = [Points.uuid, Points.user_id]

    can_delete = False

    name = "Точка"
    name_plural = "Точки"
    icon = "fa-solid fa-location-dot"


class RolesAdmin(ModelView, model=Roles):
    column_exclude_list = [Roles.user]
    column_details_exclude_list = [Roles.user]

    can_delete = False

    name = "Роль"
    name_plural = "Роли"
    icon = "fa-solid fa-user-group"

    category = "Роли и права доступа"


class PermissionsAdmin(ModelView, model=Permissions):
    column_list = [c.name for c in Permissions.__table__.columns]

    can_delete = False

    name = "Разрешение"
    name_plural = "Разрешения"
    icon = "fa-solid fa-user-group"

    category = "Роли и права доступа"
