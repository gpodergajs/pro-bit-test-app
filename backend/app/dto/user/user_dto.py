from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True