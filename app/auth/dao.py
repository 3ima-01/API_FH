from app.dao.base import BaseDAO
from sqlalchemy import select
from app.database import async_session_maker

from app.auth.models import Permissions, Role_Permissions


class PermissionsDAO(BaseDAO):
    model = Permissions

    @classmethod
    async def find_all_permissions_by_role(cls, role_id):
        async with async_session_maker() as session:
            query = (
                select(Permissions.name)
                .join(Role_Permissions)
                .filter(Role_Permissions.role_id == role_id)
            )
            result = await session.execute(query)
            return result.scalars().all()
