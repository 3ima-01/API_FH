from sqlalchemy import insert

from app.dao.base import BaseDAO
from app.profiles.dao import ProfileDAO
from app.users.models import Users, UnverifiedUsers

from app.database import async_session_maker


class UserDAO(BaseDAO):
    model = Users

    @classmethod
    async def create(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

            new_user = await UserDAO.find_one_or_none(**data)
            await ProfileDAO.create(
                user_id=new_user.user_id, name=str(new_user.user_id)[-12:]
            )
            await UnverifiedUsersDAO.delete(**data)
            await session.commit()


class UnverifiedUsersDAO(BaseDAO):
    model = UnverifiedUsers
