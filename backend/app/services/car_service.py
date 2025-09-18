from typing import Tuple, Any
from app import db
from app.models.car import Car
from app.dto.car.car_create_dto import CarCreateDTO
from app.dto.car.car_update_dto import CarUpdateDTO

class CarService:
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

    @staticmethod
    def create_car(dto: CarCreateDTO):
        try:
            car = Car(**dto.model_dump())  # unpack DTO into Car ORM
            db.session.add(car)
            db.session.commit()
            return car, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def update_car(car_id: int, dto: CarUpdateDTO):
        car = Car.query.get(car_id)
        if not car:
            return {"error": "Car not found"}, 404

        try:
            for key, value in dto.model_dump(exclude_unset=True).items():
                setattr(car, key, value)  # update only provided fields

            db.session.commit()
            return car, 200
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500