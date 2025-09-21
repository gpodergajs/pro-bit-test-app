from pydantic import BaseModel, ConfigDict

class EngineTypeDTO(BaseModel):
    """DTO for engine type information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
