from pydantic import BaseModel, ConfigDict

class TransmissionTypeDTO(BaseModel):
    """DTO for transmission type information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
