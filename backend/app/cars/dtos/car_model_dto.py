from pydantic import BaseModel, ConfigDict

class CarModelDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
