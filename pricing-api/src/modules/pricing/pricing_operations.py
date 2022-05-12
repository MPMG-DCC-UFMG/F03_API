from datetime import date
from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel


class PricingQuery(BaseModel):
    group_by_description: bool = Query(None, description="Considerar as descrições para o agrupamento de dados.")
    group_by_unit_metric: bool = Query(None, description="Considerar as unidades de medida para o agrupamento de dados.")
    group_by_year: bool = Query(None, description="Considerar os anos das licitações para o agrupamento de dados.")
    city: Optional[List[str]] = Query(None, description="Município do órgão licitante")
    microregion: Optional[List[str]] = Query(None, description="Microrregião do licitante")
    mesoregion: Optional[List[str]] = Query(None, description="Mesorregião do licitante")
    plan_region: Optional[List[str]] = Query(None, description="Região de planejamento do licitante")
    imediate_region: Optional[List[str]] = Query(None, description="Região imediata do licitante")
    inter_region: Optional[List[str]] = Query(None, description="Região intermediária do licitante")
    year: Optional[List[str]] = Query(None, description="Ano de exercício")
    month: Optional[List[str]] = Query(None, description="Mês de exercício")
    before: Optional[date] = Query(None, description="Limite superior de data")
    after: Optional[date] = Query(None, description="Limite inferior de data")
    group: Optional[str] = Query(None, description="Nome do grupo do item")
    description: str = Query(None, min_length=3, description="Texto na descrição original do item")
    first_token: Optional[str] = Query(None, description="Primeiro termo do item")
    body: Optional[str] = Query(None, description="Órgão da licitação")
    body_type: Optional[str] = Query(None, description="Tipo do órgão da licitação")
    modality: Optional[str] = Query(None, description="Modalidade de licitação")
    procurement_type: Optional[str] = Query(None, description="Tipo de licitação")
    bidder_name: Optional[str] = Query(None, description="Nome do licitante")
    bidder_type: Optional[str] = Query(None, description="Tipo do licitante")
    bidder_document: Optional[str] = Query(None, description="Documento do licitante (CPF/CNPJ)")
    min_amount: Optional[int] = Query(None, description="Quantidade mínima de itens cotados")
    max_amount: Optional[int] = Query(None, description="Quantidade máxima de itens cotados")
    min_homolog_price: Optional[float] = Query(None, description="Valor mínimo dos itens homologados")
    max_homolog_price: Optional[float] = Query(None, description="Valor máximo dos itens homologados")
    object_nature: Optional[float] = Query(None, description="Natureza do item")
    units_of_measure: Optional[List[str]] = Query(None, description="Selected units of measure")

    
