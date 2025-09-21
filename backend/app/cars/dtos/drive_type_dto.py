from pydantic import BaseModel, ConfigDict

class DriveTypeDTO(BaseModel):
    """DTO for drive type information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
