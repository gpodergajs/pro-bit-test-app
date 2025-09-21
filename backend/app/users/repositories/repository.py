from app import db
from ..models import User
from app.common.logger import get_logger
from typing import Optional

logger = get_logger(__name__)

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        """
        Retrieves a user by their username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            Optional[User]: The User object if found, otherwise None.
        """
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username: str, email: str, password_hash: str) -> User:
        """
        Creates a new user in the database.

        Args:
            username (str): The username for the new user.
            email (str): The email address for the new user.
            password_hash (str): The hashed password for the new user.

        Returns:
            User: The newly created User object.
        """
        user = User(username=username, email=email)
        user.password_hash = password_hash
        db.session.add(user)
        db.session.commit()
        return user
