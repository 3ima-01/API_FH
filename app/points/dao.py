from app.dao.base import BaseDAO

from app.points.models import Points


class PointDAO(BaseDAO):
    model = Points
