from sqlalchemy import select
from app.dao.base import BaseDAO
from app.parts.models import Rods, Coils

from app.database import async_session_maker


class CalcDAO(BaseDAO):
    @classmethod
    async def calc_wear(cls, name, percentage):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(name=name)
            result = await session.execute(query)
            obj = result.mappings().one_or_none()["mex"]
            x = 0.7 * obj * (percentage / 100)
            N = 0.7 * obj - x + 0.3 * obj
        return float("{:.3f}".format(N))


class RodDAO(CalcDAO):
    model = Rods


class CoilDAO(CalcDAO):
    model = Coils
