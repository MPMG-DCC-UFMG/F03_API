from typing import Any, List, Optional
from pydantic import  BaseModel, Field


class Pricing(BaseModel):
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida do objeto na licitação correspondente")
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    mean: float = Field(example=20.50, title="Preço médio do item considerando a unidade de medida e ano correspondentes")
    max: float = Field(example=50.50, title="Preço máximo do item considerando a unidade de medida e ano correspondentes")
    min: float = Field(example=15.50, title="Preço mínimo do item considerando a unidade de medida e ano correspondentes")
    count: int = Field(example=35, title="Número de itens com a descrição, unidade de medida e ano correspondentes")

class PricingItem(BaseModel):
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida do objeto na licitação correspondente")
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    original_dsc: str = Field(example="gasolina comum 5 litros", title='Descrição padronizada do objeto na licitação correspondente')
    mean: float = Field(example=20.50, title="Preço médio do item considerando a unidade de medida e ano correspondentes")
    max: float = Field(example=50.50, title="Preço máximo do item considerando a unidade de medida e ano correspondentes")
    min: float = Field(example=15.50, title="Preço mínimo do item considerando a unidade de medida e ano correspondentes")
    count: int = Field(example=35, title="Número de itens com a descrição, unidade de medida e ano correspondentes")

class PricingGroup(BaseModel):
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida do objeto na licitação correspondente")
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    grupo: str = Field(example="gasolina_0", title="Grupo de itens")
    mean: float = Field(example=20.50, title="Preço médio do item considerando a unidade de medida e ano correspondentes")
    max: float = Field(example=50.50, title="Preço máximo do item considerando a unidade de medida e ano correspondentes")
    min: float = Field(example=15.50, title="Preço mínimo do item considerando a unidade de medida e ano correspondentes")
    count: int = Field(example=35, title="Número de itens com a descrição, unidade de medida e ano correspondentes")
