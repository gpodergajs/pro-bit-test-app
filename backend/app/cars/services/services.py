from typing import Dict, Tuple, Any
from ..dtos import CarCreateDTO, CarUpdateDTO
from app.common.logger import get_logger
from ..repositories.repository import CarRepository

logger = get_logger(__name__)

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
        logger.info(f"Fetching all cars with page={page}, per_page={per_page}, filters={filters}")
        cars_data = CarRepository.get_all_cars(page, per_page, filters)
        return cars_data, 200


    @staticmethod
    def get_car_by_id(car_id: int) -> Tuple[Any, int]:
        """
        Get a car by its ID.
        """
        logger.info(f"Fetching car with ID: {car_id}")
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found.")
            return {"error": "Car not found"}, 404
        return car, 200


    @staticmethod
    def delete_car(car_id: int) -> Tuple[Any, int]:
        """
        Delete a car by its ID.
        """
        logger.info(f"Attempting to delete car with ID: {car_id}")
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found for deletion.")
            return {"error": "Car not found"}, 404

        try:
            CarRepository.delete_car(car)
            logger.info(f"Car with ID {car_id} deleted successfully.")
            return {"message": "Car deleted"}, 200
        except Exception as e:
            logger.error(f"Error deleting car with ID {car_id}: {e}")
            return {"error": str(e)}, 500

    @staticmethod
    def create_car(dto: CarCreateDTO):
        logger.info(f"Attempting to create car with data: {dto.model_dump()}")
        try:
            car = CarRepository.create_car(dto.model_dump())
            logger.info(f"Car created successfully with ID: {car.id}")
            return car, 201
        except Exception as e:
            logger.error(f"Error creating car: {e}")
            return {"error": str(e)}, 500

    @staticmethod
    def update_car(car_id: int, dto: CarUpdateDTO):
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found for update.")
            return {"error": "Car not found"}, 404

        logger.info(f"Attempting to update car with ID {car_id} with data: {dto.model_dump(exclude_unset=True)}")
        try:
            updated_car = CarRepository.update_car(car, dto.model_dump(exclude_unset=True))
            logger.info(f"Car with ID {car_id} updated successfully.")
            return updated_car, 200
        except Exception as e:
            logger.error(f"Error updating car with ID {car_id}: {e}")
            return {"error": str(e)}, 500

    @staticmethod
    def get_owners():
        logger.info("Fetching all car owners.")
        owners = CarRepository.get_owners()
        return [{"id": o.id, "username": o.username} for o in owners], 200

    @staticmethod
    def get_models():
        logger.info("Fetching all car models.")
        models = CarRepository.get_models()
        return [{"id": m.id, "name": m.name} for m in models], 200

    @staticmethod
    def get_body_types():
        logger.info("Fetching all body types.")
        body_types = CarRepository.get_body_types()
        return [{"id": b.id, "name": b.name} for b in body_types], 200

    @staticmethod
    def get_transmission_types():
        logger.info("Fetching all transmission types.")
        transmissions = CarRepository.get_transmission_types()
        return [{"id": t.id, "name": t.name} for t in transmissions], 200

    @staticmethod
    def get_drive_types():
        logger.info("Fetching all drive types.")
        drives = CarRepository.get_drive_types()
        return [{"id": d.id, "name": d.name} for d in drives], 200

    @staticmethod
    def get_engine_types():
        logger.info("Fetching all engine types.")
        engines = CarRepository.get_engine_types()
        return [{"id": e.id, "name": e.name} for e in engines], 200