from typing import Optional, Annotated
from pydantic import BaseModel, Field

class CarUpdateDTO(BaseModel):
    """DTO for updating an existing car's information."""
    vin: Optional[Annotated[str, Field(max_length=50)]] = None
    license_plate: Optional[Annotated[str, Field(max_length=20)]] = None
    model_id: Optional[int] = None
    owner_id: Optional[int] = None
    body_type_id: Optional[int] = None
    engine_type_id: Optional[int] = None
    transmission_type_id: Optional[int] = None
    drive_type_id: Optional[int] = None

    engine_capacity: Optional[Annotated[float, Field(gt=0)]] = None
    fuel_consumption: Optional[Annotated[float, Field(gt=0)]] = None
    mileage: Optional[Annotated[float, Field(ge=0)]] = None
    color: Optional[str] = None
    doors: Optional[Annotated[int, Field(ge=2)]] = None
    registration_year: Optional[int] = None
    price: Optional[float] = None
