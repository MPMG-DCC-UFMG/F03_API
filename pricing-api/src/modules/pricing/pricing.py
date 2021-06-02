from typing import Any, List
from pydantic import  BaseModel

class PricingModel(BaseModel):
    years: List[int]
    units_of_measure: List[str]
    items: List[Any]
