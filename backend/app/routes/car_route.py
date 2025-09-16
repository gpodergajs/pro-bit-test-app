from flask import Blueprint, request, jsonify
from app.services.car_service import (
    create_car,
    get_all_cars,
    get_car_by_id,
    update_car,
    delete_car
)

car_bp = Blueprint("car", __name__)

# Create a car
@car_bp.route("/", methods=["POST"])
def add_car():
    data = request.get_json()
    car = create_car(data["make"], data["model"], data["year"], data["price"])
    return jsonify({"id": car.id, "make": car.make, "model": car.model, "year": car.year, "price": car.price}), 201

# Get all cars
@car_bp.route("/", methods=["GET"])
def list_cars():
    cars = get_all_cars()
    return jsonify([{"id": c.id, "make": c.make, "model": c.model, "year": c.year, "price": c.price} for c in cars])

# Get car by ID
@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id):
    car = get_car_by_id(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"id": car.id, "make": car.make, "model": car.model, "year": car.year, "price": car.price})

# Update car
@car_bp.route("/<int:car_id>", methods=["PUT"])
def edit_car(car_id):
    data = request.get_json()
    car = update_car(car_id, data.get("make"), data.get("model"), data.get("year"), data.get("price"))
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"id": car.id, "make": car.make, "model": car.model, "year": car.year, "price": car.price})

# Delete car
@car_bp.route("/<int:car_id>", methods=["DELETE"])
def remove_car(car_id):
    success = delete_car(car_id)
    if not success:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"message": "Car deleted successfully"})
