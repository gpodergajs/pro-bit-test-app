from flask import Blueprint, request, jsonify
from ..services import UserService

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response, status = UserService.register(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    return jsonify(response), status

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status = UserService.login(
        username=data["username"],
        password=data["password"]
    )
    return jsonify(response), status
