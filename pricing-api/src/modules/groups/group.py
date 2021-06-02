from typing import Any, List
from pydantic import  BaseModel
from datetime import datetime

class GroupModel(BaseModel):
    id: str
    name: str
    first_token: str
    size: int
    units_of_measure: List[str]
    items: List[Any]
    created_at: datetime
    updated_at: datetime
