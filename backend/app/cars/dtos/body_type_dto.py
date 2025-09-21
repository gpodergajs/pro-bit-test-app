from pydantic import BaseModel

class BodyTypeDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
