from typing import Optional, List
from fastapi import Query
from datetime import date
from src.modules.utils.utils import get_params_values, check_params_values
from pydantic import BaseModel

class ListItemsQuery(BaseModel):
    limit: int = Query(10, description="Query limit")
    offset: int = Query(0, description="Query offset")
    sort: Optional[str] = Query(None, description="Atributo de ordenação")
    order: Optional[str] = Query("desc", description="Critério de ordenação", regex="^asc|desc$")
    city: Optional[List[str]] = Query(None, description="Município do órgão licitante", example="RIO POMBA")
    microregion: Optional[List[str]] = Query(None, description="Microrregião do licitante", example="UBA")
    mesoregion: Optional[List[str]] = Query(None, description="Mesorregião do licitante", example="ZONA DA MATA")
    plan_region: Optional[List[str]] = Query(None, description="Região de planejamento do licitante")
    imediate_region: Optional[List[str]] = Query(None, description="Região imediata do licitante")
    inter_region: Optional[List[str]] = Query(None, description="Região intermediária do licitante")
    year: Optional[List[str]] = Query(None, description="Ano de exercício", example="2020")
    month: Optional[List[str]] = Query(None, description="Mês de exercício", example="01")
    before: Optional[date] = Query(None, description="Limite superior de data", example="2014-01-01")
    after: Optional[date] = Query(None, description="Limite inferior de data", example="2022-05-04")
    description: str = Query(None, min_length=3, description="Texto na descrição original do item", example="clips")
    unit_measure: Optional[str] = Query(None, description="Unidade de medida do item")
    group: Optional[str] = Query(None, description="Nome do grupo do item")
    first_token: Optional[str] = Query(None, description="Primeiro termo do item")
    body: Optional[str] = Query(None, description="Órgão da licitação", example="PREFEITURA MUNICIPAL DE RIO POMBA")
    body_type: Optional[str] = Query(None, description="Tipo do órgão da licitação", example="PREFEITURA MUNICIPAL")
    modality: Optional[str] = Query(None, description="Modalidade de licitação", example="PREGAO PRESENCIAL")
    procurement_type: Optional[str] = Query(None, description="Tipo de licitação", example="MENOR PRECO")
    bidder_name: Optional[str] = Query(None, description="Nome do licitante", example="SEVEN COPY COMERCIAL LTDA")
    bidder_type: Optional[str] = Query(None, description="Tipo do licitante", example="J")
    bidder_document: Optional[str] = Query(None, description="Documento do licitante (CPF/CNPJ)", example="07416432000127")
    min_amount: Optional[int] = Query(None, description="Quantidade mínima de itens homologados", example=1)
    max_amount: Optional[int] = Query(None, description="Quantidade máxima de itens homologados", example=200)
    min_homolog_price: Optional[float] = Query(None, description="Valor mínimo dos itens homologados", example=1.0)
    max_homolog_price: Optional[float] = Query(None, description="Valor máximo dos itens homologados", example=5.5)
    object_nature: Optional[str] = Query(None, description="Natureza do item", example="COMPRAS E OUTROS SERVICOS")
