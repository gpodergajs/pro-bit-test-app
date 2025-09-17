from typing import Optional, Tuple, Any
from app import db
from app.models.car import Car

class CarService:
    @staticmethod
    def create_car(make: str, model: str, year: int, price: float) -> Tuple[Any, int]:
        """
        Create a new car entry.
        Returns the Car object and status code.
        """
        try:
            car = Car(make=make, model=model, year=year, price=price)
            db.session.add(car)
            db.session.commit()
            return car, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def get_all_cars(page: int = 1, per_page: int = 10) -> Tuple[Any, int]:
        """
        Get all cars with pagination.
        Returns a dict with pagination data and Car objects.
        """
        paginated = Car.query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            "items": paginated.items,      # list of Car objects
            "page": page,
            "total_pages": paginated.pages,
            "total_items": paginated.total,
        }, 200

    @staticmethod
    def get_car_by_id(car_id: int) -> Tuple[Any, int]:
        """
        Get a car by its ID.
        """
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404
        return car, 200

    @staticmethod
    def update_car(
        car_id: int,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[int] = None,
        price: Optional[float] = None,
    ) -> Tuple[Any, int]:
        """
        Update an existing car.
        """
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404

        if make is not None:
            car.make = make
        if model is not None:
            car.model = model
        if year is not None:
            car.year = year
        if price is not None:
            car.price = price

        try:
            db.session.commit()
            return car, 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_car(car_id: int) -> Tuple[Any, int]:
        """
        Delete a car by its ID.
        """
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404

        try:
            db.session.delete(car)
            db.session.commit()
            return {"message": "Car deleted"}, 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500
