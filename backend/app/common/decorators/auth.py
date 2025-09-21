from functools import wraps
from flask_jwt_extended import get_jwt_identity, get_jwt

from app.common.enums.user_type_enum import UserTypeEnum

def role_required(role_type: UserTypeEnum):
    """
    A decorator that checks if the current user has the required role.

    Args:
        role_type (UserTypeEnum): The minimum role required to access the resource.

    Returns:
        function: The decorated function if the user has the required role, otherwise returns an error response.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            claims = get_jwt()
            user_type_id = claims.get("user_type_id")

            if not user_id or not user_type_id:
                return {"error": "Unauthorized"}, 401

            # Compare directly against the enum value (ID)
            if int(user_type_id) != role_type.value:
                return {"error": "Forbidden"}, 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
