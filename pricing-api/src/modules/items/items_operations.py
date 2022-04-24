from typing import Optional, List
from fastapi import Query
from datetime import date

from pydantic import BaseModel


class ListItemsQuery(BaseModel):
    city: Optional[List[str]] = Query(None, description="Município do órgão licitante")
    microregion: Optional[List[str]] = Query(None, description="Microrregião do licitante")
    mesoregion: Optional[List[str]] = Query(None, description="Mesorregião do licitante")
    plan_region: Optional[List[str]] = Query(None, description="Região de planejamento do licitante")
    imediate_region: Optional[List[str]] = Query(None, description="Região imediata do licitante")
    inter_region: Optional[List[str]] = Query(None, description="Região intermediária do licitante")
    year: Optional[List[int]] = Query(None, description="Ano de exercício")
    month: Optional[List[int]] = Query(None, description="Mês de exercício")
    before: Optional[date] = Query(None, description="Limite superior de data")
    after: Optional[date] = Query(None, description="Limite inferior de data")
    description: str = Query(None, min_length=3, description="Texto na descrição original do item")
    unit_measure: Optional[str] = Query(None, min_length=1, description="Unidade de medida do item")
    group: Optional[str] = Query(None, description="Nome do grupo do item")
    first_token: Optional[str] = Query(None, description="Primeiro termo do item")
    body: Optional[str] = Query(None, description="Órgão da licitação")
    body_type: Optional[str] = Query(None, description="Tipo do órgão da licitação")
    modality: Optional[str] = Query(None, description="Modalidade de licitação")
    procurement_type: Optional[str] = Query(None, description="Tipo de licitação")
    bidder_name: Optional[str] = Query(None, description="Nome do licitante")
    bidder_type: Optional[str] = Query(None, description="Tipo do licitante")
    bidder_document: Optional[str] = Query(None, description="Documento do licitante (CPF/CNPJ)")
    min_amount: Optional[int] = Query(None, description="Quantidade mínima de itens homologados")
    max_amount: Optional[int] = Query(None, description="Quantidade máxima de itens homologados")
    min_homolog_price: Optional[float] = Query(None, description="Valor mínimo dos itens homologados")
    max_homolog_price: Optional[float] = Query(None, description="Valor máximo dos itens homologados")
    object_nature: Optional[str] = Query(None, description="Natureza do item")

    class Config:
        arbitrary_types_allowed = True