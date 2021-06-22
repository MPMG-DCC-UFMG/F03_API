from typing import Optional, List

from sqlalchemy.sql.sqltypes import Date
from fastapi import Query

class ListItemsQueryParams:
    def __init__(
        self,
        limit: int = Query(0, description="Query limit"),
        offset: int = Query(15, description="Query offset"),
        sort: Optional[str] = Query(None,description="The sorting attribute"),
        county: Optional[str] = Query(None,description="Município do órgão licitante"),
        year: Optional[List[str]] = Query(None, description="Ano da licitação"),
        description: Optional[str] = Query(None, description="Texto na descrição original do item"),
        group: Optional[str] = Query(None, description="Nome do grupo do item")
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.county = county
        self.year = year
        self.description = description
        self.group = group