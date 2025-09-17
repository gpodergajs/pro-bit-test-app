from flask import Blueprint, request, jsonify
from app.services.car_service import (
    create_car,
    get_all_cars,
    get_car_by_id,
    update_car,
    delete_car
)
from app.schemas.car_schema import CarSchema
from app.schemas.user_schema import UserSchema

car_bp = Blueprint("car", __name__)
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# Get all cars
@car_bp.route("/", methods=["GET"])
def list_cars():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    # Get paginated cars
    cars, total_pages = get_all_cars(page=page, per_page=per_page)

    # Serialize with Marshmallow
    result = CarSchema(many=True).dump(cars)

    return jsonify({
        "cars": result,
        "page": page,
        "total_pages": total_pages
    }), 200


# Get car by ID
@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car = get_car_by_id(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car_schema.dump(car)), 200

# Create car
@car_bp.route("/", methods=["POST"])
def add_car():
    data = request.get_json()
    car = create_car(data["make"], data["model"], data["year"], data["price"])
    return jsonify(car_schema.dump(car)), 201

# Update car
@car_bp.route("/<int:car_id>", methods=["PUT"])
def edit_car(car_id):
    data = request.get_json()
    car = update_car(car_id, data.get("make"), data.get("model"), data.get("year"), data.get("price"))
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car_schema.dump(car)), 200

# Delete car
@car_bp.route("/<int:car_id>", methods=["DELETE"])
def remove_car(car_id):
    success = delete_car(car_id)
    if not success:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"message": "Car deleted successfully"}), 200
