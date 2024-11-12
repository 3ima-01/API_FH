from app.dao.base import BaseDAO

from app.profiles.models import Profile


class ProfileDAO(BaseDAO):
    model = Profile
