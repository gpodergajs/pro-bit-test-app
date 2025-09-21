from pydantic import BaseModel, ConfigDict

class DriveTypeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
