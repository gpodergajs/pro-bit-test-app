from pydantic import BaseModel, ConfigDict

class UserDTO(BaseModel):
    """DTO for user information."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
