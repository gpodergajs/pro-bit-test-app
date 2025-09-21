from pydantic import BaseModel, ConfigDict

class EngineTypeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
