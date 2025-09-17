from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.schemas.car_schema import CarSchema
from app.decorators import role_required
from app.services.car_service import CarService

car_bp = Blueprint("car", __name__)
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# Get all cars
@car_bp.route("/", methods=["GET"])
def list_cars():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    response, status = CarService.get_all_cars(page=page, per_page=per_page)
    if "items" in response:
        return {
            "cars": cars_schema.dump(response["items"]),
            "page": response["page"],
            "total_pages": response["total_pages"],
            "total_items": response["total_items"],
        }, status
    return response, status


# Get car by ID
@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id):
    response, status = CarService.get_car_by_id(car_id)
    if isinstance(response, dict):  # error response
        return response, status
    return car_schema.dump(response), status


# Create car
@car_bp.route("/", methods=["POST"])
@jwt_required()
def add_car():
    data = request.get_json()
    response, status = CarService.create_car(
        make=data["make"],
        model=data["model"],
        year=data["year"],
        price=data["price"],
    )
    if isinstance(response, dict):  # error response
        return response, status
    return car_schema.dump(response), status


# Update car
@car_bp.route("/<int:car_id>", methods=["PUT"])
@jwt_required()
def edit_car(car_id):
    data = request.get_json()
    response, status = CarService.update_car(
        car_id=car_id,
        make=data.get("make"),
        model=data.get("model"),
        year=data.get("year"),
        price=data.get("price"),
    )
    if isinstance(response, dict):  # error response
        return response, status
    return car_schema.dump(response), status


# Delete car
@car_bp.route("/<int:car_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def remove_car(car_id):
    response, status = CarService.delete_car(car_id)
    return response, status
