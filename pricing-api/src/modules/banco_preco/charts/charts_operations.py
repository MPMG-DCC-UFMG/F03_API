from typing import List, Optional
from fastapi import Query
from datetime import date
from src.modules.banco_preco.utils.utils import (
    get_params_values,
    check_params_values
)


class ChartsQueryParams:
    def __init__(
        self,
        limit: int = Query(10, description="Query limit"),
        offset: int = Query(0, description="Query offset"),
        sort: Optional[str] = Query(None, description="Atributo de ordenação"),
        order: Optional[str] = Query(
            "desc", description="Critério de ordenação", regex="^asc|desc$"),
        city: Optional[List[str]] = Query(
            None, description="Município do órgão licitante"),
        microregion: Optional[List[str]] = Query(
            None, description="Microrregião do licitante"),
        mesoregion: Optional[List[str]] = Query(
            None, description="Mesorregião do licitante"),
        plan_region: Optional[List[str]] = Query(
            None, description="Região de planejamento do licitante"),
        imediate_region: Optional[List[str]] = Query(
            None, description="Região imediata do licitante"),
        inter_region: Optional[List[str]] = Query(
            None, description="Região intermediária do licitante"),
        year: Optional[List[str]] = Query(
            None, description="Ano de exercício"),
        month: Optional[List[str]] = Query(
            None, description="Mês de exercício"),
        before: Optional[date] = Query(
            None, description="Limite superior de data"),
        after: Optional[date] = Query(
            None, description="Limite inferior de data"),
        description: str = Query(
            None, min_length=3, description="Texto na descrição original do item"),
        unit_measure: Optional[str] = Query(
            None, min_length=1, description="Unidade de medida do item"),
        group: Optional[str] = Query(
            None, description="Nome do grupo do item"),
        first_token: Optional[str] = Query(
            None, description="Primeiro termo do item"),
        body: Optional[str] = Query(None, description="Órgão da licitação"),
        body_type: Optional[str] = Query(
            None, description="Tipo do órgão da licitação"),
        modality: Optional[str] = Query(
            None, description="Modalidade de licitação"),
        procurement_type: Optional[str] = Query(
            None, description="Tipo de licitação"),
        bidder_name: Optional[str] = Query(
            None, description="Nome do licitante"),
        bidder_type: Optional[str] = Query(
            None, description="Tipo do licitante"),
        bidder_document: Optional[str] = Query(
            None, description="Documento do licitante (CPF/CNPJ)"),
        min_amount: Optional[int] = Query(
            None, description="Quantidade mínima de itens homologados"),
        max_amount: Optional[int] = Query(
            None, description="Quantidade máxima de itens homologados"),
        min_homolog_price: Optional[float] = Query(
            None, description="Valor mínimo dos itens homologados"),
        max_homolog_price: Optional[float] = Query(
            None, description="Valor máximo dos itens homologados"),
        object_nature: Optional[str] = Query(
            None, description="Natureza do item")
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.order = order
        self.city = city
        self.microregion = microregion
        self.mesoregion = mesoregion
        self.plan_region = plan_region
        self.imediate_region = imediate_region
        self.inter_region = inter_region
        self.year = year
        self.month = month
        self.before = before
        self.after = after
        self.description = description
        self.unit_measure = unit_measure
        self.group = group
        self.first_token = first_token
        self.body = body
        self.modality = modality
        self.procurement_type = procurement_type
        self.bidder_name = bidder_name
        self.bidder_document = bidder_document
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.min_homolog_price = min_homolog_price
        self.max_homolog_price = max_homolog_price
        self.body_type = body_type
        self.bidder_type = bidder_type
        self.object_nature = object_nature

        # check if all filter values are valid
        check_params_values(self, )

        # add filter conditions in a list
        self.filters = get_params_values(self, )
