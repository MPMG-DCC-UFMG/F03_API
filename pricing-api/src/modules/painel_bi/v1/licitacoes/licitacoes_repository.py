import os

from src.modules.painel_bi.v1.licitacoes.licitacoes_operations import LicitacaoQuery
from src.modules.painel_bi.v1.model.licitacao import LicitacaoModel
from src.modules.painel_bi.v1.model.licitante import LicitanteModel
from src.modules.painel_bi.v1.model.detalhamento_cnpj import DetalhamentoCnpjModel
from src.modules.painel_bi.v1.model.detalhamento_licitacao import DetalhamentoLicitacaoModel

from src.modules.painel_bi.v1.utils.utils import Pageable

from src.db.database import db_session

from sqlalchemy import and_, func

import math

class LicitacaoRepository:


    def get_licitacoes(params: LicitacaoQuery, pageable: Pageable):
        filters = params.filters
        limit = pageable.get_limit()
        offset = pageable.get_offset()

        count = db_session.query(LicitacaoModel.seq_dim_licitacao) \
                           .filter(and_(*filters)) \
                           .count()

        result = db_session.query(
            LicitacaoModel.seq_dim_licitacao,\
            LicitacaoModel.nom_entidade,\
            LicitacaoModel.nom_micro_regiao,\
            LicitacaoModel.nom_meso_regiao,\
            LicitacaoModel.nom_comarca,\
            LicitacaoModel.nom_modalidade,\
            LicitacaoModel.num_exercicio,\
            LicitacaoModel.vlr_licitacao,\
            LicitacaoModel.ranking_irregularidades \
            )\
           .filter(and_(*filters)) \
           .group_by( \
            LicitacaoModel.seq_dim_licitacao,\
            LicitacaoModel.nom_entidade,\
            LicitacaoModel.nom_micro_regiao,\
            LicitacaoModel.nom_meso_regiao,\
            LicitacaoModel.nom_comarca,\
            LicitacaoModel.nom_modalidade,\
            LicitacaoModel.num_exercicio,\
            LicitacaoModel.vlr_licitacao,\
            LicitacaoModel.ranking_irregularidades)\
           .order_by(LicitacaoModel.ranking_irregularidades.desc())\
           .offset(offset) \
           .limit(limit)

        dict_list = []
        for row in result:
            dict_list.append({
                "seq_dim_licitacao":row[0],
                "nom_entidade":row[1],
                "nom_micro_regiao":row[2],
                "nom_meso_regiao":row[3],
                "nom_comarca":row[4],
                "nom_modalidade":row[5],
                "num_exercicio":row[6],
                "vlr_licitacao":row[7],
                "ranking_irregularidades":row[8]
            })

        heatmap_aggregations  = db_session.query( \
            func.count(LicitacaoModel.seq_dim_licitacao).label('seq_dim_licitacao'), \
            func.max(LicitacaoModel.ranking_irregularidades).label('ranking_irregularidades'), \
            func.max(LicitacaoModel.qtde_de_cnpjs_envolvidos_emails).label('qtde_de_cnpjs_envolvidos_emails'), \
            func.max(LicitacaoModel.qtd_lograd_nro_compl_comum).label('qtd_lograd_nro_compl_comum'), \
            func.max(LicitacaoModel.qtd_lograd_nro_comum).label('qtd_lograd_nro_comum'), \
            func.max(LicitacaoModel.qtde_licitantes_nao_ativos).label('qtde_licitantes_nao_ativos'), \
            func.max(LicitacaoModel.qtde_licitantes_nao_ativos_vencedores).label('qtde_licitantes_nao_ativos_vencedores'), \
            func.max(LicitacaoModel.flag_lict_unic_com_venc).label('flag_lict_unic_com_venc'), \
            func.max(LicitacaoModel.flag_socios_comum).label('flag_socios_comum'), \
            func.max(LicitacaoModel.qtde_de_cnpjs_envolvidos_tels).label('qtde_de_cnpjs_envolvidos_tels'))\
            .filter(and_(*filters))

        filters.append(LicitacaoModel.ranking_irregularidades > 0)

        irregularities  = db_session.query(func.count(LicitacaoModel.ranking_irregularidades).label('ranking_irregularidades'), func.sum(LicitacaoModel.ranking_irregularidades).label('sum_ranking_irregularidades')) \
                                    .filter(and_(*filters))

        res = {
          "current_page": pageable.get_page(),
          "last_page": math.ceil(count/pageable.get_per_page()),
          "total": {
            "ranking_irregularidades":	irregularities[0][0],
            "sum_ranking_irregularidades":	irregularities[0][1],
            "count":count
          },
          "heatmap_numbers": {
            "count":heatmap_aggregations[0][0],
            "ranking_irregularidades":heatmap_aggregations[0][1],
            "qtde_de_cnpjs_envolvidos_emails":heatmap_aggregations[0][2],
            "qtd_lograd_nro_compl_comum":heatmap_aggregations[0][3],
            "qtd_lograd_nro_comum":heatmap_aggregations[0][4],
            "qtde_licitantes_nao_ativos":heatmap_aggregations[0][5],
            "qtde_licitantes_nao_ativos_vencedores":heatmap_aggregations[0][6],
            "flag_lict_unic_com_venc":heatmap_aggregations[0][7],
            "flag_socios_comum":heatmap_aggregations[0][8],
            "qtde_de_cnpjs_envolvidos_tels":heatmap_aggregations[0][9]
          },
          "data": dict_list
        }

        return res

    def find_by_id(id_licitacao: str):
        filters_lictacao = [LicitacaoModel.seq_dim_licitacao == id_licitacao]
        licitacao  = db_session.query(LicitacaoModel).filter(and_(*filters_lictacao))
        dict_licitacao = [row.__dict__ for row in licitacao]

        filters_lictante = [LicitanteModel.seq_dim_licitacao == id_licitacao]
        licitantes  = db_session.query(LicitanteModel).filter(and_(*filters_lictante))
        dict_licitantes = [row.__dict__ for row in licitantes]

        for licitante in dict_licitantes:
            print(licitante)
            filters_det_lictacao = []
            filters_det_lictacao.append(DetalhamentoLicitacaoModel.seq_dim_licitacao == id_licitacao)
            filters_det_lictacao.append(DetalhamentoLicitacaoModel.num_documento == licitante['num_documento'])
            det_licitacao  = db_session.query(DetalhamentoLicitacaoModel).filter(and_(*filters_det_lictacao))
            dict_det_licitacao = [row.__dict__ for row in det_licitacao]
            licitante['detalhes'] = dict_det_licitacao

            filters_det_cnpj = []
            filters_det_cnpj.append(DetalhamentoCnpjModel.num_documento == licitante['num_documento'])
            det_cnpj  = db_session.query(DetalhamentoCnpjModel).filter(and_(*filters_det_cnpj))
            dict_det_cnpj = [row.__dict__ for row in det_cnpj]
            licitante['cnpj'] = dict_det_cnpj[0]

        res = {
          "licitacao": dict_licitacao,
          "licitantes": dict_licitantes
        }
        return res
 