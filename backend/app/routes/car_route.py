from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from pydantic import ValidationError
from app.dto import CarCreateDTO, CarUpdateDTO, CarReadDTO
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
        # Convert each Car instance to CarReadDTO dict
        cars = [CarReadDTO.model_validate(car).model_dump() for car in response["items"]]
        return {
            "cars": cars,
            "page": response["page"],
            "total_pages": response["total_pages"],
            "total_items": response["total_items"],
        }, status
    return response, status


# Get car by ID
@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car, status = CarService.get_car_by_id(car_id)
    if isinstance(car, dict):  # error response
        return car, status

    car_dto = CarReadDTO.model_validate(car)
    return car_dto.model_dump(), status


# Create car
@car_bp.route("/", methods=["POST"])
@jwt_required()
def add_car():
    data = request.get_json()
    try:
        dto = CarCreateDTO(**data)
    except ValidationError as e:
        return {"errors": e.errors()}, 422

    response, status = CarService.create_car(dto)

    # If an error dictionary was returned, pass it through
    if isinstance(response, dict):
        return response, status

    # Otherwise, serialize Car object using Pydantic DTO
    car_dto = CarReadDTO.model_validate(response)
    return car_dto.model_dump(), status

# Update car
@car_bp.route("/<int:car_id>", methods=["PUT"])
@jwt_required()
def edit_car(car_id):
    data = request.get_json()
    try:
        dto = CarUpdateDTO(**data)
    except ValidationError as e:
        return {"errors": e.errors()}, 422

    car, status = CarService.update_car(car_id=car_id, dto=dto)
    
    if isinstance(car, dict):
        return car, status

    car_dto = CarReadDTO.model_validate(car)
    return car_dto.model_dump(), status


# Delete car
@car_bp.route("/<int:car_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def remove_car(car_id):
    response, status = CarService.delete_car(car_id)
    return response, status
