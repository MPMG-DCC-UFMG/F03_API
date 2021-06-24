from typing import Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    item_id: str = Field(example="123", title='Identificador do item')
    licitacao: str = Field(example="123", title='Identificador da licitaçao')
    grupo_ruido: int = Field(example=0, title="Se o grupo a qual o item faz parte é um grupo de ruído")
    item_ruido: int = Field(example=0, title="Se o item corresponde a um ruído para o grupo em que faz parte")
    grupo: str = Field(example="gasolina_0", title="Grupo a qual o item faz parte")
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida do objeto na licitação correspondente")
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    mes: int = Field(example=12, title="Mês em que a licitação foi homologada")
    data: str = Field(example="10/12/2015", title='Data em que a licitação foi homologada')
    municipio: str = Field(example="Belo Horizonte", title='Município em que a licitação ocorreu')
    orgao: str = Field(example="Prefeitura de Belo Horizonte", title='Órgão responsável por iniciar o processo de licitação')
    original: str = Field(example="GASOLINA COMUM 05 LITROS", title='Descrição do objeto na licitação correspondente')
    original_dsc: str = Field(example="gasolina comum 5 litros", title='Descrição padronizada do objeto na licitação correspondente')
    preco: float = Field(example=20.50, title="Valor unitário do objeto na licitação correspondente")
    primeiro_termo: str = Field(example="gasolina", title='Primeiro termo da descrição do item')
