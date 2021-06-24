from typing import Optional
from pydantic import BaseModel, Field

class Group(BaseModel):
    grupo: str = Field(example="gasolina_0", title="Grupo de objetos de licitação")
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida dos objetos do grupo")
    grupo_id: str = Field(example="123", title='Id do grupo representado pelo nome do grupo (coluna "grupo") e a unidade de medida (coluna "dsc_unidade_medida")')
    media: float = Field(example=4.15, title="Média dos valores unitários dos itens do grupo")
    qtd: int = Field(example=200, title="Número de itens do grupo com a unidade de medida correspondente")
    max: float = Field(example=4.50, title="Valor unitário máximo dos itens do grupo")
    min: float = Field(example=3.60, title="Valor unitário mínimo dos itens do grupo")
    mediana: float = Field(example=4.0, title="Mediana dos valores unitários dos itens do grupo")
    desvio_padrao: float = Field(example=0.1, title="Desvio padrão dos valores unitários dos itens do grupo")
    var: float = Field(example=0.1, title="Variância dos valores unitários dos itens do grupo")
    quantil_1: float = Field(example=3.80, title="Primeiro quartil dos valores unitários dos itens do grupo")
    quantil_3: float = Field(example=4.20, title="Terceiro quartil dos valores unitários dos itens do grupo")
    primeiro_termo: str = Field(example="gasolina", title='Primeiro termo das descrições do grupo')
    ruido: int = Field(example=0, title="Se o grupo corresponde a ruído")
