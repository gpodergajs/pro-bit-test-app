from pydantic import BaseModel, ConfigDict

class BodyTypeDTO(BaseModel):
    """DTO for body type information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
