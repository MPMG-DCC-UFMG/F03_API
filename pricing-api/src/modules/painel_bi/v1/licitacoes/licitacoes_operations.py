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
        self.filters = []
        if bool(self.municipios):
            self.filters.append(LicitacaoModel.nom_entidade.in_(self.municipios))
        if bool(self.microrregiao):
            self.filters.append(LicitacaoModel.nom_micro_regiao.in_(self.microrregiao))
        if bool(self.mesorregiao):
            self.filters.append(LicitacaoModel.nom_meso_regiao.in_(self.mesorregiao))
        if bool(self.comarca):
            self.filters.append(LicitacaoModel.nom_comarca.in_(self.comarca))
        if bool(self.modalidades):
            self.filters.append(LicitacaoModel.nom_modalidade.in_(self.modalidades))

        if bool(self.ano):
            self.filters.append(LicitacaoModel.num_exercicio <= self.ano[0])
        if bool(self.ano):
            self.filters.append(LicitacaoModel.num_exercicio >= self.ano[1])

        if bool(self.valor):
            self.filters.append(LicitacaoModel.vlr_licitacao <= self.valor[0])
        if bool(self.valor):
            self.filters.append(LicitacaoModel.vlr_licitacao >= self.valor[1])
