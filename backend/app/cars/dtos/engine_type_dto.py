from pydantic import BaseModel

class EngineTypeDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
