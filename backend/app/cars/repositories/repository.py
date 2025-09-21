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
        """
        Retrieves a paginated result of cars based on filters.

        Args:
            page (int): The page number for pagination.
            per_page (int): The number of items per page.
            filters (Dict[str, Any]): A dictionary of filters to apply to the query.

        Returns:
            PaginatedResult[Car]: A paginated result containing Car objects.
        """
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
        """
        Retrieves a car by its ID.

        Args:
            car_id (int): The unique identifier of the car.

        Returns:
            Optional[Car]: The Car object if found, otherwise None.
        """
        return Car.query.get(car_id)

    @staticmethod
    def delete_car(car: Car) -> None:
        """
        Deletes a car from the database.

        Args:
            car (Car): The Car object to delete.
        """
        db.session.delete(car)
        db.session.commit()

    @staticmethod
    def create_car(car_data: Dict[str, Any]) -> Car:
        """
        Adds a new car to the database.

        Args:
            car_data (Dict[str, Any]): A dictionary containing the car's data.

        Returns:
            Car: The newly created Car object.
        """
        car = Car(**car_data)
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def update_car(car: Car, update_data: Dict[str, Any]) -> Car:
        """
        Updates an existing car in the database.

        Args:
            car (Car): The Car object to update.
            update_data (Dict[str, Any]): A dictionary containing the updated car data.

        Returns:
            Car: The updated Car object.
        """
        for key, value in update_data.items():
            setattr(car, key, value)
        db.session.commit()
        return car

    @staticmethod
    def get_owners() -> List[User]:
        """
        Retrieves all car owners from the database.

        Returns:
            List[User]: A list of User objects who are car owners.
        """
        return User.query.all()

    @staticmethod
    def get_models() -> List[CarModel]:
        """
        Retrieves all car models from the database.

        Returns:
            List[CarModel]: A list of CarModel objects.
        """
        return CarModel.query.all()

    @staticmethod
    def get_body_types() -> List[BodyType]:
        """
        Retrieves all body types from the database.

        Returns:
            List[BodyType]: A list of BodyType objects.
        """
        return BodyType.query.all()

    @staticmethod
    def get_transmission_types() -> List[TransmissionType]:
        """
        Retrieves all transmission types from the database.

        Returns:
            List[TransmissionType]: A list of TransmissionType objects.
        """
        return TransmissionType.query.all()

    @staticmethod
    def get_drive_types() -> List[DriveType]:
        """
        Retrieves all drive types from the database.

        Returns:
            List[DriveType]: A list of DriveType objects.
        """
        return DriveType.query.all()

    @staticmethod
    def get_engine_types() -> List[EngineType]:
        """
        Retrieves all engine types from the database.

        Returns:
            List[EngineType]: A list of EngineType objects.
        """
        return EngineType.query.all()
