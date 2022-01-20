from typing import Optional
from fastapi import APIRouter, Query

class ListFiltersQueryParams:
    def __init__(self,
                 column: str = Query(..., min_length=3, max_length=30, description="Lista valores distintos"),
                 prefix: Optional[str] = Query(None, description="Lista valores distintos que iniciam com <prefix>"),
                 contains: Optional[str] = Query(None, description="Lista valores que contém <contains>"),
                 offset: int = Query(0, description="Query offset"),
                 limit: int = Query(15, description="Query limit")):
        self.column = column
        self.prefix = prefix
        self.contains = contains
        self.offset = offset
        self.limit = limit
