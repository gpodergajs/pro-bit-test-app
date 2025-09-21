from typing import Dict, Any, Optional, List
from app import db
from ..models import Car, BodyType, DriveType, EngineType, TransmissionType, CarModel
from app.users.models import User
from app.common.logger import get_logger
from app.common.dtos.pagination_dto import PaginatedResult

logger = get_logger(__name__)

class CarRepository:
    @staticmethod
    def get_all_cars(page: int = 1, per_page: int = 10, filters: Dict[str, Any] = None) -> PaginatedResult[Car]:
        query = Car.query

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
        return PaginatedResult(
            items=paginated.items,
            page=paginated.page,
            total_pages=paginated.pages,
            total_items=paginated.total
        )

    @staticmethod
    def get_car_by_id(car_id: int) -> Optional[Car]:
        return Car.query.get(car_id)

    @staticmethod
    def delete_car(car: Car) -> None:
        db.session.delete(car)
        db.session.commit()

    @staticmethod
    def create_car(car_data: Dict[str, Any]) -> Car:
        car = Car(**car_data)
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def update_car(car: Car, update_data: Dict[str, Any]) -> Car:
        for key, value in update_data.items():
            setattr(car, key, value)
        db.session.commit()
        return car

    @staticmethod
    def get_owners() -> List[User]:
        return User.query.all()

    @staticmethod
    def get_models() -> List[CarModel]:
        return CarModel.query.all()

    @staticmethod
    def get_body_types() -> List[BodyType]:
        return BodyType.query.all()

    @staticmethod
    def get_transmission_types() -> List[TransmissionType]:
        return TransmissionType.query.all()

    @staticmethod
    def get_drive_types() -> List[DriveType]:
        return DriveType.query.all()

    @staticmethod
    def get_engine_types() -> List[EngineType]:
        return EngineType.query.all()
