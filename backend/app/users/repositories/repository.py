from app import db
from ..models import User
from app.common.logger import get_logger
from typing import Optional

logger = get_logger(__name__)

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username: str, email: str, password_hash: str) -> User:
        user = User(username=username, email=email)
        user.password_hash = password_hash
        db.session.add(user)
        db.session.commit()
        return user
