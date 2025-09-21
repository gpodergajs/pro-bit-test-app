from typing import Optional, Annotated
from pydantic import BaseModel, Field

class CarCreateDTO(BaseModel):
    """DTO for creating a new car."""
    vin: Annotated[str, Field(max_length=50)]
    license_plate: Annotated[str, Field(max_length=20)]
    model_id: int
    owner_id: int
    body_type_id: int
    engine_type_id: int
    transmission_type_id: int
    drive_type_id: int

    engine_capacity: Optional[Annotated[float, Field(gt=0)]] = None
    fuel_consumption: Optional[Annotated[float, Field(gt=0)]] = None
    mileage: Optional[Annotated[float, Field(ge=0)]] = None
    color: Optional[str] = None
    doors: Optional[Annotated[int, Field(ge=2)]] = None
    registration_year: Optional[int] = None
    price: Optional[float] = None
