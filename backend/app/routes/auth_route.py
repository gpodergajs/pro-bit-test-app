from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response, status = AuthService.register(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    return jsonify(response), status

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status = AuthService.login(
        username=data["username"],
        password=data["password"]
    )
    return jsonify(response), status
