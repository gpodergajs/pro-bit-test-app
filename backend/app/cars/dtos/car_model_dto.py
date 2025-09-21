from pydantic import BaseModel

class CarModelDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
