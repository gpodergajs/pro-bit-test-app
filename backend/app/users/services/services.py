from flask_jwt_extended import create_access_token
from ..models import User
from app import db
from app.common.logger import get_logger

logger = get_logger(__name__)

class UserService:
    @staticmethod
    def register(username: str, email: str, password: str):
        logger.info(f"Attempting to register user: {username}")
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            logger.info(f"User {username} registered successfully.")
            return {"message": "User registered"}, 201
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error registering user {username}: {e}")
            return {"error": str(e)}, 500

    @staticmethod
    def login(username: str, password: str):
        logger.info(f"Attempting to log in user: {username}")
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            logger.warning(f"Failed login attempt for user: {username}")
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"user_type_id": str(user.user_type_id)}
        )
        logger.info(f"User {username} logged in successfully.")
        return {"access_token": access_token}, 200
