from flask_jwt_extended import create_access_token
from app.common.logger import get_logger
from app.users.models.user import User
from ..repositories.repository import UserRepository

logger = get_logger(__name__)

class UserService:
    @staticmethod
    def register(username: str, email: str, password: str):
        logger.info(f"Attempting to register user: {username}")
        try:
            user = UserRepository.create_user(username, email, User().set_password(password))
            logger.info(f"User {username} registered successfully.")
            return {"message": "User registered"}, 201
        except Exception as e:
            logger.error(f"Error registering user {username}: {e}")
            return {"error": str(e)}, 500

    @staticmethod
    def login(username: str, password: str):
        logger.info(f"Attempting to log in user: {username}")
        user = UserRepository.get_user_by_username(username)
        if not user or not user.check_password(password):
            logger.warning(f"Failed login attempt for user: {username}")
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"user_type_id": str(user.user_type_id)}
        )
        logger.info(f"User {username} logged in successfully.")
        return {"access_token": access_token}, 200
