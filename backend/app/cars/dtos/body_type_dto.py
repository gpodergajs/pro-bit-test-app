from pydantic import BaseModel, ConfigDict

class BodyTypeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
