from typing import Any, List
from pydantic import  BaseModel
from datetime import datetime

class ItemModel(BaseModel):
    id: str
    description: str
    unit_of_measure: str
    word_tokens: List[str]
    material_tokens: List[str]
    number_tokens: List[str]
    color_tokens: List[str]
    size_tokens: List[str]
    units_of_measure: List[str]
    price: float
    created_at: datetime
    updated_at: datetime
