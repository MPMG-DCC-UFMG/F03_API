from typing import Optional, List
from fastapi import Query
from datetime import date

class ListItemsQueryParams:
    def __init__(
        self,
        limit: int = Query(10, description="Query limit"),
        offset: int = Query(15, description="Query offset"),
        sort: Optional[str] = Query(None,description="The sorting attribute"),
        order: Optional[str] = Query("desc",description="The sorting order", regex="^asc|desc$"),
        county: Optional[str] = Query(None,description="Município do órgão licitante"),
        year: Optional[List[str]] = Query(None, description="Ano da licitação"),
        before: Optional[date] = Query(None, description="Limite superior de data"),
        after: Optional[date] = Query(None, description="Limite inferior de data"),
        description: Optional[str] = Query(None, min_length=3, description="Texto na descrição original do item"),
        group: Optional[str] = Query(None, description="Nome do grupo do item")
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.order = order
        self.county = county
        self.year = year
        self.before = before
        self.after = after
        self.description = description
        self.group = group