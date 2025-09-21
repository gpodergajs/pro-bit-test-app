from pydantic import BaseModel, ConfigDict

class TransmissionTypeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
