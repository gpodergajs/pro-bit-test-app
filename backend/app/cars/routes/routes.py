from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError

from app.common.decorators.auth import role_required
from ..dtos import CarCreateDTO, CarUpdateDTO, CarReadDTO, TransmissionTypeDTO, DriveTypeDTO, BodyTypeDTO, EngineTypeDTO, CarModelDTO
from app.common.dtos.pagination_dto import PaginatedResult
from ..services import CarService, CarNotFoundException
from app.users.dtos.user_dto import UserDTO


car_bp = Blueprint("car", __name__)


# Get all cars
# Get all cars with optional filters
@car_bp.route("/", methods=["GET", "OPTIONS"])
def list_cars() -> Response:
    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    # Filters
    price_from = request.args.get("price_from", type=float)
    price_to = request.args.get("price_to", type=float)
    mileage_to = request.args.get("mileage_to", type=float)
    year_from = request.args.get("year_from", type=int)
    year_to = request.args.get("year_to", type=int)

    filters = {}
    if price_from is not None:
        filters["price_from"] = price_from
    if price_to is not None:
        filters["price_to"] = price_to
    if mileage_to is not None:
        filters["mileage_to"] = mileage_to
    if year_from is not None:
        filters["year_from"] = year_from
    if year_to is not None:
        filters["year_to"] = year_to

    try:
        paginated_result = CarService.get_all_cars(page=page, per_page=per_page, filters=filters)
        cars = [CarReadDTO.model_validate(car).model_dump() for car in paginated_result.items]
        return jsonify({
            "cars": cars,
            "page": paginated_result.page,
            "total_pages": paginated_result.total_pages,
            "total_items": paginated_result.total_items,
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get car by ID
@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id) -> Response:
    try:
        car = CarService.get_car_by_id(car_id)
        car_dto = CarReadDTO.model_validate(car)
        return jsonify(car_dto.model_dump()), 200
    except CarNotFoundException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Create car
@car_bp.route("/", methods=["POST"])
@jwt_required()
def add_car() -> Response:
    data = request.get_json()
    try:
        dto = CarCreateDTO(**data)
        car = CarService.create_car(dto)
        car_dto = CarReadDTO.model_validate(car)
        return jsonify(car_dto.model_dump()), 201
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update car
@car_bp.route("/<int:car_id>", methods=["PUT"])
#@jwt_required()
def edit_car(car_id) -> Response:
    data = request.get_json()
    try:
        dto = CarUpdateDTO(**data)
        car = CarService.update_car(car_id=car_id, dto=dto)
        car_dto = CarReadDTO.model_validate(car)
        return jsonify(car_dto.model_dump()), 200
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 422
    except CarNotFoundException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Delete car
@car_bp.route("/<int:car_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def remove_car(car_id) -> Response:
    try:
        CarService.delete_car(car_id)
        return jsonify({"message": "Car deleted successfully"}), 200
    except CarNotFoundException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/transmissions", methods=["GET"])
def get_transmissions() -> Response:
    try:
        transmissions = CarService.get_transmission_types()
        transmissions_data = [TransmissionTypeDTO.model_validate(t).model_dump() for t in transmissions]
        return jsonify({"transmission_types": transmissions_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/drives", methods=["GET"])
def get_drives() -> Response:
    try:
        drives = CarService.get_drive_types()
        drives_data = [DriveTypeDTO.model_validate(d).model_dump() for d in drives]
        return jsonify({"drive_types": drives_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/bodies", methods=["GET"])
def get_bodies() -> Response:
    try:
        body_types = CarService.get_body_types()
        body_types_data = [BodyTypeDTO.model_validate(b).model_dump() for b in body_types]
        return jsonify({"body_types": body_types_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/engines", methods=["GET"])
def get_engines() -> Response:
    try:
        engine_types = CarService.get_engine_types()
        engine_types_data = [EngineTypeDTO.model_validate(e).model_dump() for e in engine_types]
        return jsonify({"engine_types": engine_types_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/models", methods=["GET"])
def get_models() -> Response:
    try:
        models = CarService.get_models()
        models_data = [CarModelDTO.model_validate(m).model_dump() for m in models]
        return jsonify({"models": models_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@car_bp.route("/owners", methods=["GET"])
def get_owners() -> Response:
    try:
        owners = CarService.get_owners()
        owners_data = [UserDTO.model_validate(o).model_dump() for o in owners]
        return jsonify({"owners": owners_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
