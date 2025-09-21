from typing import Optional
from pydantic import BaseModel
from .car_model_dto import CarModelDTO
from app.users.dtos import UserDTO
from .body_type_dto import BodyTypeDTO
from .engine_type_dto import EngineTypeDTO
from .transmission_type_dto import TransmissionTypeDTO
from .drive_type_dto import DriveTypeDTO

class CarReadDTO(BaseModel):
    id: int
    vin: str
    license_plate: str

    model: Optional[CarModelDTO] = None
    owner: Optional[UserDTO] = None
    body_type: Optional[BodyTypeDTO] = None
    engine_type: Optional[EngineTypeDTO] = None
    transmission_type: Optional[TransmissionTypeDTO] = None
    drive_type: Optional[DriveTypeDTO] = None

    engine_capacity: Optional[float] = None
    fuel_consumption: Optional[float] = None
    mileage: Optional[float] = None
    color: Optional[str] = None
    doors: Optional[int] = None
    registration_year: Optional[int] = None
    price: Optional[float] = None

    class Config:
        from_attributes = True
