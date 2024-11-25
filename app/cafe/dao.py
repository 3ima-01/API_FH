from app.dao.base import BaseDAO
from app.cafe.models import Cafe


class CafeDAO(BaseDAO):
    model = Cafe
