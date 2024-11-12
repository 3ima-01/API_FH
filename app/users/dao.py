from app.dao.base import BaseDAO
from app.users.models import User, UnverifiedUsers


class UserDAO(BaseDAO):
    model = User


class UnverifiedUsersDAO(BaseDAO):
    model = UnverifiedUsers
