import os

from src.modules.painel_bi.v2.licitacoes.licitacoes_operations import LicitacaoQuery
from src.modules.painel_bi.v2.licitacoes.licitacoes_operations import get_params_values
from src.modules.painel_bi.v2.model.licitacao import LicitacaoModel
from src.modules.painel_bi.v2.model.licitante import LicitanteModel
from src.modules.painel_bi.v2.model.detalhamento_cnpj import DetalhamentoCnpjModel
from src.modules.painel_bi.v2.model.detalhamento_licitacao import DetalhamentoLicitacaoModel
from src.modules.painel_bi.v2.model.representante_legal import RepresentanteLegalModel
from src.modules.painel_bi.v2.model.representante_servidor import RepresentanteServidorModel
from src.modules.painel_bi.v2.model.sancoes_ceis import SancoesCeisModel

from src.modules.painel_bi.v1.utils.utils import Pageable

from src.db.database import db_session

from sqlalchemy import and_, func

import math

class LicitacaoRepository:


    def get_licitacoes(params: LicitacaoQuery, pageable: Pageable):
        filters = get_params_values(params)
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
            LicitacaoModel.ranking_irregularidades,\
            LicitacaoModel.dsc_objeto,\
            LicitacaoModel.num_exercicio_licitacao,\
            LicitacaoModel.nom_fonte_recurso,\
            LicitacaoModel.cod_modalidade,\
            LicitacaoModel.qtde_licitantes_nao_ativos,\
            LicitacaoModel.qtd_cnpjs_envolvidos_socios_comum,\
            LicitacaoModel.qtd_cnpjs_antes_atividade,\
            LicitacaoModel.qtd_cnpjs_envolvidos_nao_socios_comum,\
            LicitacaoModel.qtd_cnpjs_cnae_incongruente,\
            LicitacaoModel.qtd_cnpjs_restricao_ceis,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_emails,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_tels,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_endereco,\
            LicitacaoModel.qtd_cnpjs_vencedores_frequentes,\
            LicitacaoModel.qtd_cnpjs_perdedores_frequentes,\
            LicitacaoModel.qtd_cnpjs_socio_servidor_publico,\
            LicitacaoModel.flag_lict_unic_com_venc,\
            LicitacaoModel.flag_lict_unic_sem_venc\
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
            LicitacaoModel.ranking_irregularidades,\
            LicitacaoModel.dsc_objeto,\
            LicitacaoModel.num_exercicio_licitacao,\
            LicitacaoModel.nom_fonte_recurso,\
            LicitacaoModel.cod_modalidade,\
            LicitacaoModel.qtde_licitantes_nao_ativos,\
            LicitacaoModel.qtd_cnpjs_envolvidos_socios_comum,\
            LicitacaoModel.qtd_cnpjs_antes_atividade,\
            LicitacaoModel.qtd_cnpjs_envolvidos_nao_socios_comum,\
            LicitacaoModel.qtd_cnpjs_cnae_incongruente,\
            LicitacaoModel.qtd_cnpjs_restricao_ceis,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_emails,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_tels,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_endereco,\
            LicitacaoModel.qtd_cnpjs_vencedores_frequentes,\
            LicitacaoModel.qtd_cnpjs_perdedores_frequentes,\
            LicitacaoModel.qtd_cnpjs_socio_servidor_publico,\
            LicitacaoModel.flag_lict_unic_com_venc,\
            LicitacaoModel.flag_lict_unic_sem_venc)\
           .order_by(LicitacaoModel.ranking_irregularidades.desc())\
           .offset(offset) \
           .limit(limit)

        dict_list = []
        for row in result:
            qtde_licitantes_nao_ativos = row[13]
            qtd_cnpjs_envolvidos_socios_comum = row[14]
            qtd_cnpjs_antes_atividade = row[15]
            qtd_cnpjs_envolvidos_nao_socios_comum = row[16]
            qtd_cnpjs_cnae_incongruente = row[17]
            qtd_cnpjs_restricao_ceis = row[18]
            qtde_de_cnpjs_envolvidos_emails = row[19]
            qtde_de_cnpjs_envolvidos_tels = row[20]
            qtde_de_cnpjs_envolvidos_endereco = row[21]
            qtd_cnpjs_vencedores_frequentes = row[22]
            qtd_cnpjs_perdedores_frequentes = row[23]
            qtd_cnpjs_socio_servidor_publico = row[24]
            flag_lict_unic_com_venc = row[25]
            flag_lict_unic_sem_venc = row[26]
            dict_list.append({
                "seq_dim_licitacao":row[0],
                "nom_entidade":row[1],
                "nom_micro_regiao":row[2],
                "nom_meso_regiao":row[3],
                "nom_comarca":row[4],
                "nom_modalidade":row[5],
                "num_exercicio":row[6],
                "vlr_licitacao":row[7],
                "ranking_irregularidades":row[8],
                "dsc_objeto":row[9],
                "num_exercicio_licitacao":row[10],
                "nom_fonte_recurso":row[11],
                "cod_modalidade":row[12],
                "T01":flag_lict_unic_com_venc*flag_lict_unic_sem_venc,
                "T02":qtde_licitantes_nao_ativos,
                "T03":qtde_de_cnpjs_envolvidos_emails,
                "T04":qtde_de_cnpjs_envolvidos_tels,
                "T05":qtde_de_cnpjs_envolvidos_endereco,
                "T06":qtd_cnpjs_envolvidos_nao_socios_comum,
                "T07":qtd_cnpjs_envolvidos_socios_comum,
                "T08":qtd_cnpjs_vencedores_frequentes,
                "T09":qtd_cnpjs_perdedores_frequentes,
                "T10":qtd_cnpjs_cnae_incongruente,
                "T11":qtd_cnpjs_antes_atividade,
                "T12":qtd_cnpjs_restricao_ceis,
                "T13":qtd_cnpjs_socio_servidor_publico
            })
        heatmap_aggregations  = db_session.query( \
            func.count(LicitacaoModel.seq_dim_licitacao).label('seq_dim_licitacao'), \
            func.max(LicitacaoModel.ranking_irregularidades).label('ranking_irregularidades'), \
            func.max(LicitacaoModel.flag_lict_unic_com_venc).label('flag_lict_unic_com_venc'), \
            func.max(LicitacaoModel.qtde_licitantes_nao_ativos).label('qtde_licitantes_nao_ativos'), \
            func.max(LicitacaoModel.qtde_de_cnpjs_envolvidos_emails).label('qtde_de_cnpjs_envolvidos_emails'), \
            func.max(LicitacaoModel.qtde_de_cnpjs_envolvidos_tels).label('qtde_de_cnpjs_envolvidos_tels'), \
            func.max(LicitacaoModel.qtde_de_cnpjs_envolvidos_endereco).label('qtde_de_cnpjs_envolvidos_endereco'), \
            func.max(LicitacaoModel.qtd_cnpjs_envolvidos_nao_socios_comum).label('qtd_cnpjs_envolvidos_nao_socios_comum'), \
            func.max(LicitacaoModel.qtd_cnpjs_envolvidos_socios_comum).label('qtd_cnpjs_envolvidos_socios_comum'), \
            func.max(LicitacaoModel.qtd_cnpjs_vencedores_frequentes).label('qtd_cnpjs_vencedores_frequentes'), \
            func.max(LicitacaoModel.qtd_cnpjs_perdedores_frequentes).label('qtd_cnpjs_perdedores_frequentes'), \
            func.max(LicitacaoModel.qtd_cnpjs_cnae_incongruente).label('qtd_cnpjs_cnae_incongruente'), \
            func.max(LicitacaoModel.qtd_cnpjs_antes_atividade).label('qtd_cnpjs_antes_atividade'), \
            func.max(LicitacaoModel.qtd_cnpjs_restricao_ceis).label('qtd_cnpjs_restricao_ceis'), \
            func.max(LicitacaoModel.qtd_cnpjs_socio_servidor_publico).label('qtd_cnpjs_socio_servidor_publico'))\
            .filter(and_(*filters))

        filters.append(LicitacaoModel.ranking_irregularidades > 0)

        irregularities  = db_session.query(func.count(LicitacaoModel.ranking_irregularidades).label('ranking_irregularidades'), func.sum(LicitacaoModel.qtde_irregularidades).label('sum_ranking_irregularidades')) \
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
            "T01":heatmap_aggregations[0][2],
            "T02":heatmap_aggregations[0][3],
            "T03":heatmap_aggregations[0][4],
            "T04":heatmap_aggregations[0][5],
            "T05":heatmap_aggregations[0][6],
            "T06":heatmap_aggregations[0][7],
            "T07":heatmap_aggregations[0][8],
            "T08":heatmap_aggregations[0][9],
            "T09":heatmap_aggregations[0][10],
            "T10":heatmap_aggregations[0][11],
            "T11":heatmap_aggregations[0][12],
            "T12":heatmap_aggregations[0][13],
            "T13":heatmap_aggregations[0][14],
          },
          "data": dict_list
        }

        return res

    def find_by_id(id_licitacao: str):
        filters_lictacao = [LicitacaoModel.seq_dim_licitacao == id_licitacao]
        licitacao  = db_session.query(LicitacaoModel).filter(and_(*filters_lictacao))
        dict_licitacao = [row.__dict__ for row in licitacao][0]

        filters_lictante = [LicitanteModel.seq_dim_licitacao == id_licitacao]
        licitantes  = db_session.query(LicitanteModel).filter(and_(*filters_lictante))
        dict_licitantes = [row.__dict__ for row in licitantes]

        t01_licitantes=[]
        t02_licitantes=[]
        t03_vinculo=[]
        t04_vinculo=[]
        t05_vinculo=[]
        t06_vinculo=[]
        t07_vinculo=[]
        t08_licitantes=[]
        t09_licitantes=[]
        t10_licitantes=[]
        t11_licitantes=[]
        t12_licitantes=[]
        t13_licitantes=[]
        for licitante in dict_licitantes:
            filters_det_lictacao = []
            filters_det_lictacao.append(DetalhamentoLicitacaoModel.seq_dim_licitacao == id_licitacao)
            filters_det_lictacao.append(DetalhamentoLicitacaoModel.num_documento == licitante['num_documento'])
            det_licitacao  = db_session.query(DetalhamentoLicitacaoModel).filter(and_(*filters_det_lictacao))
            dict_det_licitacao = [row.__dict__ for row in det_licitacao][0]

            filters_rep_legal = []
            filters_rep_legal.append(RepresentanteLegalModel.id_licitacao == id_licitacao)
            filters_rep_legal.append(RepresentanteLegalModel.cnpj == licitante['num_documento'])
            det_rep_legal  = db_session.query(RepresentanteLegalModel).filter(and_(*filters_rep_legal))
            dict_rep_legal = [row.__dict__ for row in det_rep_legal]            


            representantes_nao_socio=[]
            representantes_socio=[]
            cpf_cnpj_socio=[]
            nome_socio=[]
            for rep_legal in dict_rep_legal:
                cpf_cnpj_socio.append(rep_legal['cpf_cnpj_representante'])
                nome_socio.append(rep_legal['qualificacao_representante'])
                
                if rep_legal['flag_socio']:
                    if (rep_legal['cpf_cnpj_representante'] not in (None, '')) & (rep_legal['cpf_cnpj_representante'] not in t07_vinculo):
                        t07_vinculo.append(rep_legal['cpf_cnpj_representante'])
                    representantes_socio.append((rep_legal['cpf_cnpj_representante'], rep_legal['qualificacao_representante']))
                else:
                    if (rep_legal['cpf_cnpj_representante'] not in (None, '')) & (rep_legal['cpf_cnpj_representante'] not in t06_vinculo):
                        t06_vinculo.append(rep_legal['cpf_cnpj_representante'])
                    representantes_nao_socio.append((rep_legal['cpf_cnpj_representante'], rep_legal['qualificacao_representante']))

            dict_det_licitacao['cpf_cnpj_socio'] = ';'.join(cpf_cnpj_socio)
            dict_det_licitacao['nome_socio'] = ';'.join(nome_socio)
            dict_det_licitacao['representantes_nao_socio'] = representantes_nao_socio
            dict_det_licitacao['representantes_socio'] = representantes_socio
            
            licitante['detalhes'] = dict_det_licitacao

            filters_det_cnpj = []
            filters_det_cnpj.append(DetalhamentoCnpjModel.num_documento == licitante['num_documento'])
            det_cnpj  = db_session.query(DetalhamentoCnpjModel).filter(and_(*filters_det_cnpj))
            dict_det_cnpj = [row.__dict__ for row in det_cnpj]
            licitante['cnpj'] = dict_det_cnpj[0]
            
            if dict_det_licitacao['flag_lict_unic']=="1":
                t01_licitantes.append(licitante['num_documento'])

            if dict_det_licitacao['flag_cnpj_inativo']=="1":
                t02_licitantes.append(licitante['num_documento'])
                
            if (dict_det_licitacao['email'] not in (None, '')) & (dict_det_licitacao['email'] not in t03_vinculo):
                t03_vinculo.append(dict_det_licitacao['email'])

            if (dict_det_licitacao['telefones'] not in (None, '')):
                tels=dict_det_licitacao['telefones'].split(';')
                for t in tels:
                    if (t not in (None, '')) & (t not in t04_vinculo):
                        t04_vinculo.append(t)

            endereco = dict_det_licitacao['descricao_tipo_logradouro'] + ' ' +\
                        dict_det_licitacao['logradouro'] + ' ' +\
                        dict_det_licitacao['numero'] + ' ' +\
                        dict_det_licitacao['complemento']
            if (endereco not in (None, '')) & (endereco not in t05_vinculo):
                t05_vinculo.append(endereco)

            if dict_det_licitacao['flag_vencedor_frequente']=="1":
                t08_licitantes.append(licitante['num_documento'])

            if dict_det_licitacao['flag_perdedor_frequente']=="1":
                t09_licitantes.append(licitante['num_documento'])

            if dict_det_licitacao['flag_perdedor_frequente']=="1":
                t10_licitantes.append({
                    "cpf_cnpj":licitante['num_documento'],
                    "cnaes":[
                        {
                            "codigo":licitante['cnpj']["cnae_desc"],
                            "flag_cnae_primario":1,
                            "descricao": licitante['cnpj']["cnae_fiscal"]
                        }
                    ]
                })

            if dict_det_licitacao['flag_licitante_antes_atividade']=="1":
                t11_licitantes.append({
                    "cpf_cnpj":licitante['num_documento'],
                    "data_inicio_atividade": dict_det_licitacao['data_inicio_atividade'],
                    "data_licitacao": dict_det_licitacao['data_habilitacao']
                })

            if dict_det_licitacao['flag_licitante_penalidade_ceis']=="1":
                filters_ceis = []
                filters_ceis.append(SancoesCeisModel.id_licitacao == id_licitacao)
                filters_ceis.append(SancoesCeisModel.num_documento == licitante['num_documento'])
                det_ceis  = db_session.query(SancoesCeisModel).filter(and_(*filters_ceis))
                dict_ceis = [row.__dict__ for row in det_ceis]  
                
                sancoes_ceis = []
                for c in dict_ceis:
                    sancoes_ceis.append({
                        "tipo_sancao":c["tipo_sancao"],
                        "nome_orgao_sancionador":c["nome_orgao_sancionador"],
                        "cod_fundamentacao_legal":c["cod_fundamentacao_legal"],
                        "desc_fundamentacao_legal":c["desc_fundamentacao_legal"],
                        "data_inicio_sancao_show":c["data_inicio_sancao_show"],
                        "data_final_sancao_show":c["data_final_sancao_show"]
                    })
                t12_licitantes.append({
                    "cpf_cnpj":licitante['num_documento'],
                    "sancoes_ceis":sancoes_ceis
                })

            if dict_det_licitacao['flag_licitante_servidor_publico']=="1":
                filters_rep_serv = []
                filters_rep_serv.append(RepresentanteServidorModel.id_licitacao == id_licitacao)
                filters_rep_serv.append(RepresentanteServidorModel.num_documento == licitante['num_documento'])
                det_rep_serv  = db_session.query(RepresentanteServidorModel).filter(and_(*filters_rep_serv))
                dict_rep_serv = [row.__dict__ for row in det_rep_serv] 

                rep_serv = []
                for r in dict_rep_serv:
                    rep_serv.append({
                        "cpf_cnpj":dict_rep_serv["cpf_socio_servidor"],
                        "vinculo":dict_rep_serv["vinculo_socio_servidor"]
                    })
            
                t13_licitantes.append({
                    "cpf_cnpj":licitante['num_documento'],
                    "representantes_servidor":rep_serv
                })

        t03_licitantes=[]
        t04_licitantes=[]
        t05_licitantes=[]
        t06_licitantes=[]
        t07_licitantes=[]
        for licitante in dict_licitantes:
            emails = []
            if licitante['detalhes']["email"] not in (None, ''):
                emails.append({
                    "email":licitante['detalhes']["email"],
                    "grupo":t03_vinculo.index(licitante['detalhes']["email"])+1
                })

            t03_licitantes.append({
                "cpf_cnpj":licitante['num_documento'],
                "emails":emails
            })
            
            t04_info=[]
            if (licitante['detalhes']['telefones'] not in (None, '')):
                tels=licitante['detalhes']['telefones'].split(';')
                for t in tels:
                    t04_info.append({
                        "telefone":t,
                        "grupo":t04_vinculo.index(t)+1
                    })
            t04_licitantes.append({
                "cpf_cnpj":licitante['num_documento'],
                "telefones":t04_info
            })

            endereco = licitante['detalhes']['descricao_tipo_logradouro'] + ' ' +\
            licitante['detalhes']['logradouro'] + ' ' +\
            licitante['detalhes']['numero'] + ' ' +\
            licitante['detalhes']['complemento']
            t05_licitantes.append({
                "cpf_cnpj":licitante['num_documento'],
                "enderecos":[
                    {
                        "endereco":endereco,
                        "grupo":t05_vinculo.index(endereco)+1
                    }
                ]
            })

            t06_info = []
            for r in licitante['detalhes']['representantes_nao_socio']:
                t06_info.append({
                        "cpf_cnpj":r[0],
                        "qualificacao_representante":r[1],
                        "grupo":t06_vinculo.index(r[0])+1
                    })
            t06_licitantes.append({
                "cpf_cnpj":licitante['num_documento'],
                "representantes_nao_socio":t06_info
            })

            t07_info = []
            for r in licitante['detalhes']['representantes_socio']:
                t07_info.append({
                        "cpf_cnpj":r[0],
                        "qualificacao_representante":r[1],
                        "grupo":t07_vinculo.index(r[0])+1
                    })
            t07_licitantes.append({
                "cpf_cnpj":licitante['num_documento'],
                "representantes_socio":t07_info
            })
            
            del licitante['detalhes']['representantes_nao_socio']
            del licitante['detalhes']['representantes_socio']


        dict_licitacao["grafos"]=[]
        
        t01_flag = dict_licitacao["flag_lict_unic_com_venc"]+dict_licitacao["flag_lict_unic_sem_venc"]
        if t01_flag > 1:
            t01_flag = 1
        
        dict_licitacao["trilhas"] = {
            "T01":{
                "descricao":"Licitantes únicos",
                "flag_possui_irregularidade":t01_flag,
                "qtde_licitantes_envolvidos":t01_flag,
                "qtde_irregularidades":t01_flag,
                "info":{
                    "flag_lict_unic_com_venc":dict_licitacao["flag_lict_unic_com_venc"],
                    "flag_lict_unic_sem_venc":dict_licitacao["flag_lict_unic_sem_venc"],
                    "licitantes":t01_licitantes
                }
            },
            "T02":{
                "descricao": "Licitantes com CNPJ inativo",
                "flag_possui_irregularidade":dict_licitacao["flag_existe_licitante_nao_ativo"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtde_licitantes_nao_ativos"],
                "qtde_irregularidades":dict_licitacao["qtde_licitantes_nao_ativos"],
                "info":{
                    "licitantes":t02_licitantes
                }
            },
            "T03":{
                "descricao": "Licitantes com e-mails em comum",
                "flag_possui_irregularidade":dict_licitacao["flag_existe_email_em_comum"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtde_de_cnpjs_envolvidos_emails"],
                "qtde_irregularidades":dict_licitacao["qtde_emails_que_repetem"],
                "info":{
                    "qtd_grupos":len(t03_vinculo),
                    "licitantes":t03_licitantes
                }
            },
            "T04":{
                "descricao": "Licitantes com telefones em comum",
                "flag_possui_irregularidade":dict_licitacao["flag_existe_tel_em_comum"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtde_de_cnpjs_envolvidos_tels"],
                "qtde_irregularidades":dict_licitacao["qtde_tels_que_repetem"],
                "info":{
                    "qtd_grupos":len(t04_vinculo),
                    "licitantes":t04_licitantes
                }
            },
            "T05":{
                "descricao": "Licitantes com endereços em comum",
                "flag_possui_irregularidade":dict_licitacao["flag_lograd_nro_compl_comum"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtde_de_cnpjs_envolvidos_endereco"],
                "qtde_irregularidades":dict_licitacao["qtd_lograd_nro_compl_comum"],
                "info":{
                    "qtd_grupos":len(t05_vinculo),
                    "licitantes":t05_licitantes
                }
            },
            "T06":{
                "descricao": "Licitantes com representantes legal não-sócios em comum",
                "flag_possui_irregularidade":dict_licitacao["flag_nao_socios_comum"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_envolvidos_nao_socios_comum"],
                "qtde_irregularidades":dict_licitacao["qtd_nao_socios_comum"],
                "info":{
                    "qtd_grupos":len(t06_vinculo),
                    "licitantes":t06_licitantes
                }
            },
            "T07":{
                "descricao": "Licitantes com representantes sócios em comum",
                "flag_possui_irregularidade":dict_licitacao["flag_socios_comum"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_envolvidos_socios_comum"],
                "qtde_irregularidades":dict_licitacao["qtd_socios_comum"],
                "info":{
                    "qtd_grupos":len(t07_vinculo),
                    "licitantes":t07_licitantes
                }
            },
            "T08":{
                "descricao": "Licitantes vencedores frequentes",
                "flag_possui_irregularidade":dict_licitacao["flag_possui_vencedor_frequente"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_vencedores_frequentes"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_vencedores_frequentes"],
                "info":{
                    "licitantes":t08_licitantes
                }
            },
            "T09":{
                "descricao": "Licitantes perdedores frequentes",
                "flag_possui_irregularidade":dict_licitacao["flag_possui_perdedor_frequente"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_perdedores_frequentes"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_perdedores_frequentes"],
                "info":{
                    "licitantes":t09_licitantes
                }
            },
            "T10":{
                "descricao": "Licitantes com CNAE incongruente",
                "flag_possui_irregularidade":dict_licitacao["flag_licitante_cnae_incongruente"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_cnae_incongruente"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_cnae_incongruente"],
                "info":{
                    "licitantes":t10_licitantes
                }
            },
            "T11":{
                "descricao": "Licitantes antes do início das atividades",
                "flag_possui_irregularidade":dict_licitacao["flag_licitante_antes_atividade"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_antes_atividade"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_antes_atividade"],
                "info":{
                    "licitantes":t11_licitantes
                }
            },
            "T12":{
                "descricao": "Licitantes com restrição no CEIS",
                "flag_possui_irregularidade":dict_licitacao["flag_licitante_restricao_ceis"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_restricao_ceis"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_restricao_ceis"],
                "info":{
                    "licitantes":t12_licitantes
                }
            },
            "T13":{
                "descricao": "Licitantes cujos sócios são ou têm vínculo com servidores públicos",
                "flag_possui_irregularidade":dict_licitacao["flag_licitante_servidor_publico"],
                "qtde_licitantes_envolvidos":dict_licitacao["qtd_cnpjs_socio_servidor_publico"],
                "qtde_irregularidades":dict_licitacao["qtd_cnpjs_socio_servidor_publico"],
                "info":{
                    "licitantes":t13_licitantes
                }
            }
          }

        res = {
          "licitacao": dict_licitacao,
          "licitantes": dict_licitantes
        }
        return res
 