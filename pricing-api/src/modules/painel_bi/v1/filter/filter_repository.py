import os

from src.modules.painel_bi.v1.model.licitacao import LicitacaoModel

from src.db.database import db_session

from sqlalchemy import func

class FilterRepository:



    def get_filters():

        nom_entidade  = db_session.query(LicitacaoModel.nom_entidade).distinct()
        nom_entidade = [r for r, in nom_entidade]

        nom_meso_regiao  = db_session.query(LicitacaoModel.nom_meso_regiao).distinct()
        nom_meso_regiao = [r for r, in nom_meso_regiao]

        nom_micro_regiao  = db_session.query(LicitacaoModel.nom_micro_regiao).distinct()
        nom_micro_regiao = [r for r, in nom_micro_regiao]

        nom_modalidade  = db_session.query(LicitacaoModel.nom_modalidade).distinct()
        nom_modalidade = [r for r, in nom_modalidade]

        nom_comarca  = db_session.query(LicitacaoModel.nom_comarca).distinct()
        nom_comarca = [r for r, in nom_comarca]

        infoGerais  = db_session.query(\
        func.min(LicitacaoModel.num_exercicio_licitacao).label('ano_min'), \
        func.max(LicitacaoModel.num_exercicio_licitacao).label('ano_max'), \
        func.min(LicitacaoModel.vlr_licitacao).label('vlr_min'),\
        func.max(LicitacaoModel.vlr_licitacao).label('vlr_max')\
        )

        res = {
            "municipios": nom_entidade,
            "mesorregiao": nom_meso_regiao,
            "microrregiao": nom_micro_regiao,
            "modalidades": nom_modalidade,
            "comarca": nom_comarca,
            "ano": {
                "min": infoGerais[0][0],
                "max": infoGerais[0][1]
            },
            "valor": {
                "min": infoGerais[0][2],
                "max": infoGerais[0][3]
            }
        }

        return res
