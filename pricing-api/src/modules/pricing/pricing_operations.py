from typing import List, Optional
from fastapi import Query
from datetime import date

class PricingQueryParams:
    def __init__(
        self,
        limit: int = Query(10, description="Query limit"),
        offset: int = Query(15, description="Query offset"),
        sort: Optional[str] = Query("count", description="Atributo de ordenação"),
        order: Optional[str] = Query("desc", description="Critério de ordenação", regex="^asc|desc$"),
        city: Optional[str] = Query(None, description="Município do órgão licitante"),
        region: Optional[str] = Query(None, description="Região do licitante"),
        before: Optional[date] = Query(None, description="Limite superio de data"),
        after: Optional[date] = Query(None, description="Limite inferior de data"),
        description: Optional[List[str]] = Query(None, description="The item description"),
        units_of_measure: Optional[List[str]] = Query(None, description="Selected units of measure"),
        group: Optional[List[str]] = Query(None, description="The group name"),
        first_token: Optional[str] = Query(None, description="Primeiro termo do item")
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.order = order
        self.city = city
        self.region = region
        self.before = before
        self.after = after
        self.description = description
        self.group = group
        self.first_token = first_token
        self.units_of_measure = units_of_measure
