from flask import Blueprint, jsonify
from .models import Car
# Notice we are no longer importing 'current_app' here for the decorators.

# 1. Create a Blueprint object.
# The first argument is the blueprint's name.
# The second argument is the blueprint's import name (usually __name__).
api_bp = Blueprint('api', __name__)

# 2. Use the blueprint to define routes, not 'app'.
@api_bp.route('/cars', methods=['GET'])
def get_cars():
    """Returns a list of all cars."""
    cars = Car.query.order_by(Car.make).all()
    return jsonify([car.to_dict() for car in cars])

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({"status": "healthy"})
