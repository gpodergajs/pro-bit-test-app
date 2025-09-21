from flask import Blueprint, request, jsonify, Response
from ..services import UserService, UserAlreadyExistsException, InvalidCredentialsException

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register() -> Response:
    """
    Registers a new user via API.

    Request Body:
        username (str): The desired username.
        email (str): The user's email address.
        password (str): The user's password.
    """
    data = request.get_json()
    try:
        user = UserService.register(
            username=data["username"],
            email=data["email"],
            password=data["password"]
        )
        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201
    except UserAlreadyExistsException as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route("/login", methods=["POST"])
def login() -> Response:
    """
    Authenticates a user and returns an access token via API.

    Request Body:
        username (str): The user's username.
        password (str): The user's password.
    """
    data = request.get_json()
    try:
        access_token = UserService.login(
            username=data["username"],
            password=data["password"]
        )
        return jsonify({"access_token": access_token}), 200
    except InvalidCredentialsException as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
