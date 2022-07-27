from typing import List, Optional

from fastapi import Query

class LicitacaoQuery:
    def __init__(
        self,
        ano: Optional[List[int]] = Query(None, description="Ano de exercicio da licitação"),
        comarca: Optional[List[str]] = Query(None, description="Comarca do órgão licitante"),
        mesorregiao: Optional[List[str]] = Query(None, description="Mesorregiao do órgão licitante"),
        microrregiao: Optional[List[str]] = Query(None, description="Microrregiao do órgão licitante"),
        modalidades: Optional[List[str]] = Query(None, description="Modalidades do órgão licitante"),
        municipios: Optional[List[str]] = Query(None, description="Município do órgão licitante"),
        valor: Optional[List[float]] = Query(None, description="Valor da licitação")
    ):
        self.ano = ano
        self.comarca = comarca
        self.mesorregiao = mesorregiao
        self.microrregiao = microrregiao
        self.modalidades = modalidades
        self.municipios = municipios
        self.valor = valor

        # add filter conditions in a list
        filters = []
        if bool(params.municipios):
            filters.append(LicitacaoModel.nom_entidade.in_(params.municipios))
        if bool(params.microrregiao):
            filters.append(LicitacaoModel.nom_micro_regiao.in_(params.microrregiao))
        if bool(params.mesorregiao):
            filters.append(LicitacaoModel.nom_meso_regiao.in_(params.mesorregiao))
        if bool(params.comarca):
            filters.append(LicitacaoModel.nom_comarca.in_(params.comarca))
        if bool(params.modalidades):
            filters.append(LicitacaoModel.nom_modalidade.in_(params.modalidades))

        if bool(params.ano):
            filters.append(LicitacaoModel.num_exercicio <= params.ano[0])
        if bool(params.ano):
            filters.append(LicitacaoModel.num_exercicio >= params.ano[1])

        if bool(params.valor):
            filters.append(LicitacaoModel.vlr_licitacao <= params.valor[0])
        if bool(params.valor):
            filters.append(LicitacaoModel.vlr_licitacao >= params.valor[1])
