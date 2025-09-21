from flask_jwt_extended import create_access_token
from ..models import User
from app import db

class UserService:
    @staticmethod
    def register(username: str, email: str, password: str):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered"}, 201

    @staticmethod
    def login(username: str, password: str):
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"user_type_id": str(user.user_type_id)}
        )
        return {"access_token": access_token}, 200
