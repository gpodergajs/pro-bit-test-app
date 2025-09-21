from typing import Dict, Any, Optional, List
from ..dtos import CarCreateDTO, CarUpdateDTO
from app.common.logger import get_logger
from ..repositories.repository import CarRepository
from app.common.dtos.pagination_dto import PaginatedResult
from ..models import Car, BodyType, DriveType, EngineType, TransmissionType, CarModel
from app.users.models import User

logger = get_logger(__name__)

class CarNotFoundException(Exception):
    pass

class CarService:
    
    @staticmethod
    def get_all_cars(
        page: int = 1,
        per_page: int = 10,
        filters: Dict[str, Any] = None
    ) -> PaginatedResult[Car]:
        """
        Retrieves a paginated list of cars with optional filters.

        Args:
            page (int): The page number for pagination.
            per_page (int): The number of items per page.
            filters (Dict[str, Any]): A dictionary of filters to apply to the query.

        Returns:
            PaginatedResult[Car]: A paginated result containing Car objects.
        """
        logger.info(f"Fetching all cars with page={page}, per_page={per_page}, filters={filters}")
        paginated_result = CarRepository.get_all_cars(page, per_page, filters)
        logger.info(f"Successfully fetched {len(paginated_result.items)} cars for page {page}.")
        return paginated_result


    @staticmethod
    def get_car_by_id(car_id: int) -> Optional[Car]:
        """
        Retrieves a car by its unique ID.

        Args:
            car_id (int): The unique identifier of the car.

        Returns:
            Optional[Car]: The Car object if found.

        Raises:
            CarNotFoundException: If the car with the given ID is not found.
        """
        logger.info(f"Fetching car with ID: {car_id}")
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found.")
            raise CarNotFoundException(f"Car with ID {car_id} not found")
        logger.info(f"Successfully fetched car with ID: {car_id}.")
        return car


    @staticmethod
    def delete_car(car_id: int) -> None:
        """
        Deletes a car by its unique ID.

        Args:
            car_id (int): The unique identifier of the car to delete.

        Raises:
            CarNotFoundException: If the car with the given ID is not found.
            Exception: For other deletion failures.
        """
        logger.info(f"Attempting to delete car with ID: {car_id}")
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found for deletion.")
            raise CarNotFoundException(f"Car with ID {car_id} not found for deletion")

        try:
            CarRepository.delete_car(car)
            logger.info(f"Car with ID {car_id} deleted successfully.")
            return
        except Exception as e:
            logger.error(f"Error deleting car with ID {car_id}: {e}")
            raise Exception(f"Failed to delete car with ID {car_id}") from e

    @staticmethod
    def create_car(dto: CarCreateDTO) -> Car:
        """
        Creates a new car from the provided DTO.

        Args:
            dto (CarCreateDTO): The data transfer object containing car details.

        Returns:
            Car: The newly created Car object.

        Raises:
            Exception: For creation failures.
        """
        logger.info(f"Attempting to create car with data: {dto.model_dump()}")
        try:
            car = CarRepository.create_car(dto.model_dump())
            logger.info(f"Car created successfully with ID: {car.id}")
            return car
        except Exception as e:
            logger.error(f"Error creating car: {e}")
            raise Exception(f"Failed to create car") from e

    @staticmethod
    def update_car(car_id: int, dto: CarUpdateDTO) -> Car:
        """
        Updates an existing car identified by its ID with data from the DTO.

        Args:
            car_id (int): The unique identifier of the car to update.
            dto (CarUpdateDTO): The data transfer object containing updated car details.

        Returns:
            Car: The updated Car object.

        Raises:
            CarNotFoundException: If the car with the given ID is not found.
            Exception: For other update failures.
        """
        car = CarRepository.get_car_by_id(car_id)
        if not car:
            logger.warning(f"Car with ID {car_id} not found for update.")
            raise CarNotFoundException(f"Car with ID {car_id} not found for update")

        logger.info(f"Attempting to update car with ID {car_id} with data: {dto.model_dump(exclude_unset=True)}")
        try:
            updated_car = CarRepository.update_car(car, dto.model_dump(exclude_unset=True))
            logger.info(f"Car with ID {car_id} updated successfully.")
            return updated_car
        except Exception as e:
            logger.error(f"Error updating car with ID {car_id}: {e}")
            raise Exception(f"Failed to update car with ID {car_id}") from e

    @staticmethod
    def get_owners() -> List[User]:
        """
        Retrieves all car owners.

        Returns:
            List[User]: A list of User objects who are car owners.
        """
        logger.info("Fetching all car owners.")
        owners = CarRepository.get_owners()
        logger.info(f"Successfully fetched {len(owners)} car owners.")
        return owners

    @staticmethod
    def get_models() -> List[CarModel]:
        """
        Retrieves all car models.

        Returns:
            List[CarModel]: A list of CarModel objects.
        """
        logger.info("Fetching all car models.")
        models = CarRepository.get_models()
        logger.info(f"Successfully fetched {len(models)} car models.")
        return models

    @staticmethod
    def get_body_types() -> List[BodyType]:
        """
        Retrieves all available car body types.

        Returns:
            List[BodyType]: A list of BodyType objects.
        """
        logger.info("Fetching all body types.")
        body_types = CarRepository.get_body_types()
        logger.info(f"Successfully fetched {len(body_types)} body types.")
        return body_types

    @staticmethod
    def get_transmission_types() -> List[TransmissionType]:
        """
        Retrieves all available transmission types.

        Returns:
            List[TransmissionType]: A list of TransmissionType objects.
        """
        logger.info("Fetching all transmission types.")
        transmissions = CarRepository.get_transmission_types()
        logger.info(f"Successfully fetched {len(transmissions)} transmission types.")
        return transmissions

    @staticmethod
    def get_drive_types() -> List[DriveType]:
        """
        Retrieves all available drive types.

        Returns:
            List[DriveType]: A list of DriveType objects.
        """
        logger.info("Fetching all drive types.")
        drives = CarRepository.get_drive_types()
        logger.info(f"Successfully fetched {len(drives)} drive types.")
        return drives

    @staticmethod
    def get_engine_types() -> List[EngineType]:
        """
        Retrieves all available engine types.

        Returns:
            List[EngineType]: A list of EngineType objects.
        """
        logger.info("Fetching all engine types.")
        engines = CarRepository.get_engine_types()
        logger.info(f"Successfully fetched {len(engines)} engine types.")
        return engines