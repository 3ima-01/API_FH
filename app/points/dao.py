from app.dao.base import BaseDAO

from app.points.models import Point


class PointDAO(BaseDAO):
    model = Point
