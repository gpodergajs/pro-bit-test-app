from functools import wraps
from flask_jwt_extended import get_jwt_identity, get_jwt

def role_required(role_name: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            claims = get_jwt()
            user_type_id = claims.get("user_type_id")

            if not user_id or not user_type_id:
                return {"error": "Unauthorized"}, 401

            from app.models.user import UserType
            user_type = UserType.query.get(int(user_type_id))

            if not user_type or user_type.name.lower() != role_name.lower():
                return {"error": "Forbidden"}, 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
