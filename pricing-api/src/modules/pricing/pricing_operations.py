from typing import List, Optional
from fastapi import Query


class PricingQueryParams:
    def __init__(
        self,
        description: str = Query(..., description="The item description"),
        year: Optional[int] = Query(..., description="The desired year"),
        units_of_measure: Optional[List[str]] = Query(
            None, description="Selected units of measure"),
    ):
        self.description = description
        self.year = year
        self.units_of_measure = units_of_measure
