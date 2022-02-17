from typing import Any, List, Optional
from pydantic import  BaseModel, Field


class Charts(BaseModel):
    data: str = Field(example="02/03/2015", title='Data em que a licitação foi homologada')
    qtde_item: int = Field(
        example=10, title='Quantidade total de itens homologados, agrupado por data')
    mean: float = Field(
        example=20.50, title="Média do preço do item, agrupado por data")
    median: float = Field(
        example=20.50, title="Mediana do preço do item, agrupado por data")
