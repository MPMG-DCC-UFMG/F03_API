from typing import Optional
from fastapi import APIRouter, Query

class LicitanteQueryParams:
    def __init__(self, q: str = Query(None, description="Primeiro termo do item")):
        self.q = q
