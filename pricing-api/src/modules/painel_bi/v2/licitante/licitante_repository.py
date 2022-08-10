import os

from src.modules.painel_bi.v1.model.licitacao import LicitacaoModel
from src.modules.painel_bi.v1.model.licitante import LicitanteModel
from src.modules.painel_bi.v1.model.detalhamento_cnpj import DetalhamentoCnpjModel
from src.modules.painel_bi.v1.model.detalhamento_licitacao import DetalhamentoLicitacaoModel

from src.db.database import db_session

from sqlalchemy import and_, or_, func

import math

class LicitanteRepository:



    def find_by_id(id_licitante: str):

        filters_det_cnpj = []
        filters_det_cnpj.append(DetalhamentoCnpjModel.num_documento == id_licitante)
        det_cnpj  = db_session.query(DetalhamentoCnpjModel).filter(and_(*filters_det_cnpj))
        dict_det_cnpj = [row.__dict__ for row in det_cnpj]
        infos = dict_det_cnpj

        filters_det_lictacao = []
        filters_det_lictacao.append(DetalhamentoLicitacaoModel.num_documento == id_licitante)
        det_licitacao  = db_session.query(DetalhamentoLicitacaoModel).filter(and_(*filters_det_lictacao))
        dict_det_licitacao = [row.__dict__ for row in det_licitacao]
        licitacoes = dict_det_licitacao

        filterLics = [];
        listLics=[];

        for l in licitacoes:
          listLics.append(l['seq_dim_licitacao'])
        
        
        filterLics.append(LicitacaoModel.seq_dim_licitacao.in_(listLics))
        infoGerais  = db_session.query(LicitacaoModel).filter(and_(*filterLics))
        dict_infoGerais = [row.__dict__ for row in infoGerais]

        for l in licitacoes:
            geral = None
            for g in dict_infoGerais:
                if g['seq_dim_licitacao'] == l['seq_dim_licitacao']:
                    geral = g
            
            if geral is not None:
                l['vlr_latitude'] = geral['vlr_latitude']
                l['vlr_longitude'] = geral['vlr_longitude']
                l['nom_entidade'] = geral['nom_entidade']
                l['ranking_irregularidades'] = geral['ranking_irregularidades']
            else:
                l['vlr_latitude'] = None
                l['vlr_longitude'] = None
                l['nom_entidade'] = None
                l['ranking_irregularidades'] = None

        socios = []
        if((len(licitacoes)>0) and (licitacoes[0]['nome_socio'])):
            nomes = licitacoes[0]['nome_socio'].split(";");
            cpf = licitacoes[0]['cpf_cnpj_socio'].split(";");

            for n,c in zip(nomes, cpf):
                socios.append({
                    "nome": n.strip(),
                    "cpf_cnpj": c.strip()
                })

        res = {
            "infos": infos,
            "licitacoes": licitacoes,
            "socios": socios
        }
        return res

    def search(query: str):

        busca = query;
        busca = busca.replace(".", "");
        busca = busca.replace("/", "");
        busca = busca.replace("-", "");

        filters_det_cnpj = []
        filters_det_cnpj.append(DetalhamentoCnpjModel.nome_fantasia.ilike(busca))
        filters_det_cnpj.append(DetalhamentoCnpjModel.razao_social.ilike(busca))
        filters_det_cnpj.append(DetalhamentoCnpjModel.num_documento.ilike(busca))
        det_cnpj  = db_session.query(DetalhamentoCnpjModel).filter(or_(*filters_det_cnpj)).limit(5)
        dict_det_cnpj = [row.__dict__ for row in det_cnpj]
        resultados = dict_det_cnpj

        return resultados
