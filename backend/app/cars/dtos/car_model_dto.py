from pydantic import BaseModel, ConfigDict

class CarModelDTO(BaseModel):
    """DTO for car model information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
