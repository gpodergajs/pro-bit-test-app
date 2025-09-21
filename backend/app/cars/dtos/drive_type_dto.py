from pydantic import BaseModel

class DriveTypeDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
