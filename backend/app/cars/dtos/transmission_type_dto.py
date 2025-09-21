from pydantic import BaseModel

class TransmissionTypeDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
