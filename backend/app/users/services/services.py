from flask_jwt_extended import create_access_token
from app.common.logger import get_logger
from app.users.models.user import User
from ..repositories.repository import UserRepository

logger = get_logger(__name__)

class UserAlreadyExistsException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass

class UserService:
    @staticmethod
    def register(username: str, email: str, password: str) -> User:
        """
        Registers a new user.

        Args:
            username (str): The desired username.
            email (str): The user's email address.
            password (str): The user's plain-text password.

        Returns:
            User: The newly created User object.

        Raises:
            UserAlreadyExistsException: If a user with the given username already exists.
            Exception: For other registration failures.
        """
        logger.info(f"Attempting to register user: {username}")
        try:
            if UserRepository.get_user_by_username(username):
                raise UserAlreadyExistsException(f"User with username {username} already exists")

            user = UserRepository.create_user(username, email, User().set_password(password))
            logger.info(f"User {username} registered successfully.")
            return user
        except UserAlreadyExistsException as e:
            logger.warning(f"Registration failed for {username}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error registering user {username}: {e}")
            raise Exception(f"Failed to register user {username}") from e

    @staticmethod
    def login(username: str, password: str) -> str:
        """
        Authenticates a user and returns an access token.

        Args:
            username (str): The user's username.
            password (str): The user's plain-text password.

        Returns:
            str: An access token if authentication is successful.

        Raises:
            InvalidCredentialsException: If the username or password is incorrect.
            Exception: For other login failures.
        """
        logger.info(f"Attempting to log in user: {username}")
        try:
            user = UserRepository.get_user_by_username(username)
            if not user or not user.check_password(password):
                logger.warning(f"Failed login attempt for user: {username}")
                raise InvalidCredentialsException("Invalid credentials")

            access_token = create_access_token(
                identity=str(user.id),
                additional_claims={"user_type_id": str(user.user_type_id)}
            )
            logger.info(f"User {username} logged in successfully.")
            return access_token
        except InvalidCredentialsException as e:
            logger.warning(f"Login failed for {username}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error during login for user {username}: {e}")
            raise Exception(f"Failed to log in user {username}") from e
