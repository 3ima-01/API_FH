from app.dao.base import BaseDAO

from app.profiles.models import Profiles


class ProfileDAO(BaseDAO):
    model = Profiles
