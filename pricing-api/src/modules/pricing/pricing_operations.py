from typing import List, Optional
from fastapi import Query
from datetime import date
from .utils import get_params_values, check_params_values


class PricingQueryParams:
    def __init__(
        self,
        limit: int = Query(10, description="Query limit"),
        offset: int = Query(15, description="Query offset"),
        sort: Optional[str] = Query("count", description="Atributo de ordenação"),
        order: Optional[str] = Query("desc", description="Critério de ordenação", regex="^asc|desc$"),
        city: Optional[str] = Query(None,description="Município do órgão licitante"),
        region: Optional[str] = Query(None,description="Região do licitante"),
        year: Optional[List[str]] = Query(None, description="Ano de exercício"),
        month: Optional[List[str]] = Query(None, description="Mês de exercício"),
        before: Optional[date] = Query(None, description="Limite superior de data"),
        after: Optional[date] = Query(None, description="Limite inferior de data"),
        description: Optional[str] = Query(None, min_length=3, description="Texto na descrição original do item"),
        group: Optional[str] = Query(None, description="Nome do grupo do item"),
        first_token: Optional[str] = Query(None, description="Primeiro termo do item"),
        body: Optional[str] = Query(None, description="Órgão da licitação"),
        payment_method: Optional[str] = Query(None, description="Forma de pagamento"),
        modality: Optional[str] = Query(None, description="Modalidade de licitação"),
        bidder_name: Optional[str] = Query(None, description="Nome do licitante"),
        bidder_document: Optional[str] = Query(None, description="Documento do licitante (CPF/CNPJ)"),
        min_amount: Optional[int] = Query(None, description="Quantidade mínima de itens cotados"),
        max_amount: Optional[int] = Query(None, description="Quantidade máxima de itens cotados"),
        min_price: Optional[float] = Query(None, description="Valor mínimo dos itens cotados"),
        max_price: Optional[float] = Query(None, description="valor máximo dos itens cotados"),
        min_homolog_price: Optional[float] = Query(None, description="Valor mínimo dos itens homologados"),
        max_homolog_price: Optional[float] = Query(None, description="Valor máximo dos itens homologados"),
        units_of_measure: Optional[List[str]] = Query(None, description="Selected units of measure")
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.order = order
        self.city = city
        self.region = region
        self.year = year
        self.month = month
        self.before = before
        self.after = after
        self.description = description
        self.group = group
        self.first_token = first_token
        self.body = body
        self.payment_method = payment_method
        self.modality = modality
        self.bidder_name = bidder_name
        self.bidder_document = bidder_document
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.min_price = min_price
        self.max_price = max_price
        self.min_homolog_price = min_homolog_price
        self.max_homolog_price = max_homolog_price
        self.units_of_measure = units_of_measure

        # check if all filter values are valid
        check_params_values(self, )

        # add filter conditions in a list
        self.filters = get_params_values(self, )
