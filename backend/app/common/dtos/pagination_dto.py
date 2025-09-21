from typing import Generic, List, TypeVar
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')

class PaginatedResult(BaseModel, Generic[T]):
    """DTO for paginated results."""
    model_config = ConfigDict(arbitrary_types_allowed=True)

    items: List[T]
    page: int
    total_pages: int
    total_items: int
