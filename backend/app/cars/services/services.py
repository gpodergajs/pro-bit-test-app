from typing import Dict, Tuple, Any
from app import db
from ..models import Car, BodyType, DriveType, EngineType, TransmissionType, CarModel
from ..dtos import CarCreateDTO, CarUpdateDTO
from app.users.models import User

class CarService:
    
    @staticmethod
    def get_all_cars(
        page: int = 1,
        per_page: int = 10,
        filters: Dict[str, Any] = None
    ) -> Tuple[Any, int]:
        """
        Get all cars with pagination and optional filters.
        Filters can include:
        - price_from
        - price_to
        - mileage_to
        - year_from
        - year_to
        Returns a dict with pagination data and Car objects.
        """
        query = Car.query  # Start with base query

        if filters:
            if "price_from" in filters and filters["price_from"] is not None:
                query = query.filter(Car.price >= filters["price_from"])
            if "price_to" in filters and filters["price_to"] is not None:
                query = query.filter(Car.price <= filters["price_to"])
            if "mileage_to" in filters and filters["mileage_to"] is not None:
                query = query.filter(Car.mileage <= filters["mileage_to"])
            if "year_from" in filters and filters["year_from"] is not None:
                query = query.filter(Car.registration_year >= filters["year_from"])
            if "year_to" in filters and filters["year_to"] is not None:
                query = query.filter(Car.registration_year <= filters["year_to"])

        paginated = query.paginate(page=page, per_page=per_page, error_out=False)

        return {
            "items": paginated.items,
            "page": paginated.page,
            "total_pages": paginated.pages,
            "total_items": paginated.total
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

    @staticmethod
    def get_owners():
        owners = User.query.all()  # query the User table directly
        return [{"id": o.id, "username": o.username} for o in owners], 200

    @staticmethod
    def get_models():
        models = CarModel.query.all()  # query the CarModel table directly
        return [{"id": m.id, "name": m.name} for m in models], 200

    @staticmethod
    def get_body_types():
        body_types = BodyType.query.all()
        return [{"id": b.id, "name": b.name} for b in body_types], 200

    @staticmethod
    def get_transmission_types():
        transmissions = TransmissionType.query.all()
        return [{"id": t.id, "name": t.name} for t in transmissions], 200

    @staticmethod
    def get_drive_types():
        drives = DriveType.query.all()
        return [{"id": d.id, "name": d.name} for d in drives], 200

    @staticmethod
    def get_engine_types():
        engines = EngineType.query.all()
        return [{"id": e.id, "name": e.name} for e in engines], 200