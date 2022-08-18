import os

from src.modules.painel_bi.v1.licitacoes.licitacoes_operations import LicitacaoQuery
from src.modules.painel_bi.v1.licitacoes.licitacoes_operations import get_params_values
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
        return {
          "current_page": 0,
          "last_page": 1,
          "total": {
            "ranking_irregularidades": 12,
            "sum_ranking_irregularidades": 13,
            "count": 2
          },
          "heatmap_numbers": {
            "count": 2,
            "ranking_irregularidades": 12,
            "T01":0,
            "T06":1,
            "T10":1,
            "T05":1,
            "T09":1,
            "T11":1,
            "T02":1,
            "T03":1,
            "T04":1,
            "T07":1,
            "T08":1,
            "T12":2,
            "T13":1
          },
          "data": [
            {
              "seq_dim_licitacao": "88142",
              "nom_entidade": "Felício dos Santos",
              "nom_micro_regiao": "PREGAO PRESENCIAL",
              "nom_meso_regiao": 1430299.596,
              "nom_comarca": 6,
              "nom_modalidade": "PREGAO PRESENCIAL",
              "num_exercicio": 2,
              "vlr_licitacao": 1430299.596,
              "ranking_irregularidades": 12,
              "dsc_objeto": "CONTRATACAO DE PESSOA JURIDICA E/OU FISICA PARA PRESTACAO DE SERVICO DE TRANSPORTE ESCOLAR NO MUNICIPIO DE FELICIO DOS SAN",
              "num_exercicio_licitacao": 2017,
              "nom_fonte_recurso": "RECEITAS DE IMPOSTOS E DE TRANSFERENCIAS DE IMPOSTOS VINCULADOS A EDUCACAO, TRANSFERENCIAS DE RECURSOS DO FNDE REFERENTES AO PROGRAMA NACIONAL DE APOIO AO TRANSPORTE ESCOLAR (PNATE), TRANSFERENCIAS DO FUNDEB PARA APLICACAO EM OUTRAS DESPESAS DA EDUCACAO BASICA",
              "cod_modalidade": 5,
              "T01":0,
              "T06":1,
              "T10":1,
              "T05":1,
              "T09":1,
              "T11":1,
              "T02":1,
              "T03":1,
              "T04":1,
              "T07":1,
              "T08":1,
              "T12":2,
              "T13":1
              
            }
          ]
        }
        
    def find_by_id(id_licitacao: str):
        return {
          "licitacao": [
            {
              "seq_dim_licitacao": "88142",
              "dat_publicacao_edital_veiculo_2": "",
              "ind_esfera": "M",
              "nom_reg_patrimonio_publico": "DIAMANTINA",
              "cod_micro_regiao": 31010,
              "dat_recebimento_doc": "2017-03-31",
              "nom_comarca": "DIAMANTINA",
              "num_exercicio": 2017,
              "vlr_latitude": -18.07,
              "cod_modalidade": 5,
              "dsc_objeto": "CONTRATACAO DE PESSOA JURIDICA E/OU FISICA PARA PRESTACAO DE SERVICO DE TRANSPORTE ESCOLAR NO MUNICIPIO DE FELICIO DOS SAN",
              "num_exercicio_licitacao": 2017,
              "num_modalidade": 22,
              "vlr_licitacao": 1430299.596,
              "dat_abertura": "2017-03-15",
              "dsc_objeto_busca": "CONTRATACAO DE PESSOA JURIDICA E/OU FISICA PARA PRESTACAO DE SERVICO DE TRANSPORTE ESCOLAR NO MUNICIPIO DE FELICIO DOS SAN",
              "nom_entidade": "Felício dos Santos",
              "num_processo_licitatorio": "33",
              "vlr_longitude": -43.24,
              "dat_edital_convite": "2017-03-15",
              "nom_fonte_recurso": "RECEITAS DE IMPOSTOS E DE TRANSFERENCIAS DE IMPOSTOS VINCULADOS A EDUCACAO, TRANSFERENCIAS DE RECURSOS DO FNDE REFERENTES AO PROGRAMA NACIONAL DE APOIO AO TRANSPORTE ESCOLAR (PNATE), TRANSFERENCIAS DO FUNDEB PARA APLICACAO EM OUTRAS DESPESAS DA EDUCACAO BASICA",
              "ranking_irregularidades": 12,
              "dat_publicacao_edital_do": "2017-03-18",
              "nom_meso_regiao": "Jequitinhonha",
              "seq_dim_entidade": 3125408,
              "cod_meso_regiao": 3103,
              "dat_publicacao_edital_veiculo_1": "2017-03-18",
              "funcoes": "EDUCACAO",
              "nom_micro_regiao": "Diamantina",
              "nom_modalidade": "PREGAO PRESENCIAL",
              "grafos":[],
              "trilhas": {
                "T01":{
                    "descricao":"Licitantes únicos",
                    "flag_possui_irregularidade":0,
                    "qtde_licitantes_envolvidos":0,
                    "qtde_irregularidades":0,
                    "info":{
                        "flag_lict_unic_com_venc":0,
                        "flag_lict_unic_sem_venc":0,
                        "licitantes":""
                    }
                },
                "T02":{
                    "descricao": "Licitantes com CNPJ inativo",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes":["15416313000100"]
                    }
                },
                "T03":{
                    "descricao": "Licitantes com e-mails em comum",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":2,
                    "qtde_irregularidades":1,
                    "info":{
                        "qtd_grupos":1,
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "emails":[
                                    {
                                        "email":"baracho@citel1.com.br",
                                        "grupo":1
                                    }
                                ]
                            },
                            {
                                "cpf_cnpj":"16499349000150",
                                "emails":[
                                    {
                                        "email":"baracho@citel1.com.br",
                                        "grupo":1
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T04":{
                    "descricao": "Licitantes com telefones em comum",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":2,
                    "qtde_irregularidades":2,
                    "info":{
                        "qtd_grupos":2,
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "telefones":[
                                    {
                                        "telefone":"3835311296",
                                        "grupo":1
                                    },
                                    {
                                        "telefone":"3888130405",
                                        "grupo":2
                                    }
                                ]
                            },
                            {
                                "cpf_cnpj":"16499349000150",
                                "telefones":[
                                    {
                                        "telefone":"3835311296",
                                        "grupo":1
                                    },
                                    {
                                        "telefone":"3888130405",
                                        "grupo":2
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T05":{
                    "descricao": "Licitantes com endereços em comum",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":2,
                    "qtde_irregularidades":1,
                    "info":{
                        "qtd_grupos":1,
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "enderecos":[
                                    {
                                        "endereco":"RUA FRANCISCO CANUTO 100 CENTRO FELICIO DOS SANTOS MG",
                                        "grupo":1
                                    }
                                ]
                            },
                            {
                                "cpf_cnpj":"16499349000150",
                                "enderecos":[
                                    {
                                        "endereco":"RUA FRANCISCO CANUTO 100 CENTRO FELICIO DOS SANTOS MG",
                                        "grupo":1
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T06":{
                    "descricao": "Licitantes com representantes legal não-sócios em comum",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":2,
                    "qtde_irregularidades":1,
                    "info":{
                        "qtd_grupos":1,
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "representantes_nao_socio":[
                                    {
                                        "cpf_cnpj":"41499891687",
                                        "qualificacao_representante":"TITULAR PESSOA FÍSICA RESIDENTE OU DOMICILIADO NO BRASIL",
                                        "grupo":1
                                    }
                                ]
                            },
                            {
                                "cpf_cnpj":"16499349000150",
                                "representantes_nao_socio":[
                                    {
                                        "cpf_cnpj":"41499891687",
                                        "qualificacao_representante":"TITULAR PESSOA FÍSICA RESIDENTE OU DOMICILIADO NO BRASIL",
                                        "grupo":1
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T07":{
                    "descricao": "Licitantes com representantes sócios em comum",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":2,
                    "qtde_irregularidades":1,
                    "info":{
                        "qtd_grupos":1,
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "representantes_socio":[
                                    {
                                        "cpf_cnpj":"11057443611",
                                        "qualificacao_representante":"SÓCIO",
                                        "grupo":1
                                    }
                                ]
                            },
                            {
                                "cpf_cnpj":"16499349000150",
                                "representantes_socio":[
                                    {
                                        "cpf_cnpj":"11057443611",
                                        "qualificacao_representante":"SÓCIO",
                                        "grupo":1
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T08":{
                    "descricao": "Licitantes vencedores frequentes",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes":["15416313000100"]
                    }
                },
                "T09":{
                    "descricao": "Licitantes perdedores frequentes",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes":["16499349000150"]
                    }
                },
                "T10":{
                    "descricao": "Licitantes com CNAE incongruente",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "cnaes":[
                                    {
                                        "codigo":"4921301",
                                        "flag_cnae_primario":1,
                                        "descricao": "TRANSPORTE RODOVIÁRIO COLETIVO DE PASSAGEIROS, COM ITINERÁRIO FIXO, MUNICIPAL"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T11":{
                    "descricao": "Licitantes antes do início das atividades",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "data_inicio_atividade": "2022-04-23",
                                "data_licitacao": "2017-03-15"
                            }
                        ]
                    }
                },
                "T12":{
                    "descricao": "Licitantes com restrição no CEIS",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":2,
                    "info":{
                        "licitantes":[
                            {
                                "cpf_cnpj":"15416313000100",
                                "sancoes_ceis":[
                                    {
                                        "tipo_sancao":"Suspensão - Legislação Estadual",
                                        "nome_orgao_sancionador":"Governo do Estado da Bahia",
                                        "cod_fundamentacao_legal":"Art. 186, inciso II, Lei 9433/2005",
                                        "desc_fundamentacao_legal":"Ao candidato a cadastramento, ao licitante e ao contratado, que incorram nas faltas previstas nesta Lei, aplicam-se, segundo a natureza e a gravidade da falta, assegurada a defesa prévia, as seguintes sanções: II- suspensão temporária de participação em li",
                                        "data_inicio_sancao_show":"16/09/2014",
                                        "data_final_sancao_show":"27/01/2024"
                                    },
                                    {
                                        "tipo_sancao":"Suspensão - Legislação Estadual",
                                        "nome_orgao_sancionador":"Governo do Estado da Bahia",
                                        "cod_fundamentacao_legal":"Art. 186, inciso II, Lei 9433/2005",
                                        "desc_fundamentacao_legal":"Ao candidato a cadastramento, ao licitante e ao contratado, que incorram nas faltas previstas nesta Lei, aplicam-se, segundo a natureza e a gravidade da falta, assegurada a defesa prévia, as seguintes sanções: II- suspensão temporária de participação em li",
                                        "data_inicio_sancao_show":"23/01/2014",
                                        "data_final_sancao_show":"23/10/2030"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "T13":{
                    "descricao": "Licitantes cujos sócios são ou têm vínculo com servidores públicos",
                    "flag_possui_irregularidade":1,
                    "qtde_licitantes_envolvidos":1,
                    "qtde_irregularidades":1,
                    "info":{
                        "licitantes": [
                            {
                                "cpf_cnpj":"15416313000100" ,
                                "representantes_servidor":[
                                    {
                                        "cpf_cnpj":"03555398610",
                                        "vinculo":"SERVIDOR"
                                    }
                                ]
                            }
                        ]
                    }
                }
              }
            }
          ],
          "licitantes": [
            {
              "seq_dim_licitacao": "88142",
              "ind_venceu": "S",
              "numero_de_itens": "1",
              "participacao_licitacao": 0.03,
              "num_documento": "15416313000100",
              "participacao_itens_licitacao": 0.05,
              "soma_recurso_alocado": 39204,
              "detalhes": [
                {
                  "nome_socio": "TITULAR PESSOA FÍSICA RESIDENTE OU DOMICILIADO NO BRASIL;SÓCIO-ADMINISTRADOR;SÓCIO",                
                  "cpf_cnpj_socio": "41499891687;03555398610;11057443611",             
                  "num_documento": "15416313000100",
                  "descricao_logradouro_numero_soundex": "r000f652100   ",
                  "descricao_logradouro_soundex": "r000f652",
                  "email": "baracho@citel1.com.br",
                  "flag_lict_unic": "0",
                  "logradouro": "FRANCISCO CANUTO",
                  "numero": "100   ",
                  "seq_dim_licitacao": "88142",
                  "complemento": "",
                  "descricao_logradouro_numero_complemento_soundex": "r000f652100   N000",
                  "descricao_tipo_logradouro": "RUA",
                  "flag_cnpj_inativo": "1",
                  "ind_tipo_pessoa": "J",
                  "telefones": "3835311296;3888130405",
                  "flag_vencedor_frequente":1,
                  "flag_perdedor_frequente":0
                }
              ],
              "cnpj": {
                "cnae_fiscal": "4921301",
                "descricao_tipo_logradouro": "RUA",
                "uf": "MG",
                "codigo_municipio": "4507",
                "ind_tipo_pessoa": "J",
                "complemento": "",
                "logradouro": "FRANCISCO CANUTO",
                "correio_eletronico": "baracho@citel1.com.br",
                "municipio": "FELICIO DOS SANTOS",
                "bairro": "CENTRO",
                "data_inicio_atividade": "2012-04-23",
                "nome_fantasia": "",
                "num_documento": "15416313000100",
                "ddd_telefone_1": "3835311296",
                "numero": "100   ",
                "cep": "39180000",
                "ddd_telefone_2": "3888130405",
                "qtde_socios": "3",
                "cnae_desc": "TRANSPORTE RODOVIÁRIO COLETIVO DE PASSAGEIROS, COM ITINERÁRIO FIXO, MUNICIPAL",
                "razao_social": "RAIMUNDO FRANCISCO VIEIRA CPF33197865987"
              }
            },
            {
              "seq_dim_licitacao": "88142",
              "ind_venceu": "S",
              "numero_de_itens": "1",
              "participacao_licitacao": 0.06,
              "num_documento": "16499349000150",
              "participacao_itens_licitacao": 0.05,
              "soma_recurso_alocado": 84068.16,
              "detalhes": [
                {
                  "nome_socio": "TITULAR PESSOA FÍSICA RESIDENTE OU DOMICILIADO NO BRASIL;SÓCIO",                
                  "cpf_cnpj_socio": "41499891687;11057443611",
                  "num_documento": "16499349000150",
                  "descricao_logradouro_numero_soundex": "r000s532238   ",
                  "descricao_logradouro_soundex": "r000s532",
                  "email": "baracho@citel1.com.br",
                  "flag_lict_unic": "0",
                  "logradouro": "FRANCISCO CANUTO",
                  "numero": "100   ",
                  "seq_dim_licitacao": "88142",
                  "complemento": "",
                  "descricao_logradouro_numero_complemento_soundex": "r000f652100   N000",
                  "descricao_tipo_logradouro": "RUA",
                  "flag_cnpj_inativo": "0",
                  "ind_tipo_pessoa": "J",
                  "telefones": "3835311296;3888130405",
                  "flag_vencedor_frequente":0,
                  "flag_perdedor_frequente":1
                }
              ],
              "cnpj": {
                "cnae_fiscal": "4924800",
                "descricao_tipo_logradouro": "RUA",
                "uf": "MG",
                "codigo_municipio": "4507",
                "ind_tipo_pessoa": "J",
                "complemento": "",
                "logradouro": "FRANCISCO CANUTO",
                "correio_eletronico": "baracho@citel1.com.br",
                "municipio": "FELICIO DOS SANTOS",
                "bairro": "CENTRO",
                "data_inicio_atividade": "2012-07-17",
                "nome_fantasia": "",
                "num_documento": "16499349000150",
                "ddd_telefone_1": "3835311296",
                "numero": "100   ",
                "cep": "39180000",
                "ddd_telefone_2": "3888130405",
                "qtde_socios": "2",
                "cnae_desc": "TRANSPORTE ESCOLAR",
                "razao_social": "ALCIVANDER DA SILVA 06176212685"
              }
            }
          ]
        }

    
    def old_get_licitacoes(params: LicitacaoQuery, pageable: Pageable):
        filters = get_params_values(params)
        limit = pageable.get_limit()
        offset = pageable.get_offset()

        count = db_session.query(LicitacaoModel.seq_dim_licitacao) \
                           .filter(and_(*filters)) \
                           .count()

        result = db_session.query(
            LicitacaoModel.seq_dim_licitacao,\
            LicitacaoModel.nom_entidade,\
            LicitacaoModel.nom_modalidade,\
            LicitacaoModel.vlr_licitacao,\
            LicitacaoModel.ranking_irregularidades, \
            LicitacaoModel.qtde_de_cnpjs_envolvidos_emails,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_tels,\
            LicitacaoModel.qtd_lograd_nro_comum,\
            LicitacaoModel.dsc_objeto,\
            LicitacaoModel.flag_socios_comum,\
            LicitacaoModel.qtde_licitantes_nao_ativos,\
            LicitacaoModel.qtde_licitantes_nao_ativos_vencedores,\
            LicitacaoModel.flag_lict_unic_com_venc,\
            LicitacaoModel.num_exercicio_licitacao,\
            LicitacaoModel.nom_fonte_recurso,\
            LicitacaoModel.cod_modalidade,\
            LicitacaoModel.qtd_lograd_nro_compl_comum
            )\
           .filter(and_(*filters)) \
           .group_by( \
            LicitacaoModel.seq_dim_licitacao,\
            LicitacaoModel.nom_entidade,\
            LicitacaoModel.nom_modalidade,\
            LicitacaoModel.vlr_licitacao,\
            LicitacaoModel.ranking_irregularidades, \
            LicitacaoModel.qtde_de_cnpjs_envolvidos_emails,\
            LicitacaoModel.qtde_de_cnpjs_envolvidos_tels,\
            LicitacaoModel.qtd_lograd_nro_comum,\
            LicitacaoModel.dsc_objeto,\
            LicitacaoModel.flag_socios_comum,\
            LicitacaoModel.qtde_licitantes_nao_ativos,\
            LicitacaoModel.qtde_licitantes_nao_ativos_vencedores,\
            LicitacaoModel.flag_lict_unic_com_venc,\
            LicitacaoModel.num_exercicio_licitacao,\
            LicitacaoModel.nom_fonte_recurso,\
            LicitacaoModel.cod_modalidade,\
            LicitacaoModel.qtd_lograd_nro_compl_comum)\
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
                "ranking_irregularidades":row[8],
                
            "seq_dim_licitacao":row[0],
            "nom_entidade":row[1],
            "nom_modalidade":row[2],
            "vlr_licitacao":row[3],
            "ranking_irregularidades":row[4],
            "qtde_de_cnpjs_envolvidos_emails":row[5],
            "qtde_de_cnpjs_envolvidos_tels":row[6],
            "qtd_lograd_nro_comum":row[7],
            "dsc_objeto":row[8],
            "flag_socios_comum":row[9],
            "qtde_licitantes_nao_ativos":row[10],
            "qtde_licitantes_nao_ativos_vencedores":row[11],
            "flag_lict_unic_com_venc":row[12],
            "num_exercicio_licitacao":row[13],
            "nom_fonte_recurso":row[14],
            "cod_modalidade":row[15],
            "qtd_lograd_nro_compl_comum":row[16]
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

    def old_find_by_id(id_licitacao: str):
        filters_lictacao = [LicitacaoModel.seq_dim_licitacao == id_licitacao]
        licitacao  = db_session.query(LicitacaoModel).filter(and_(*filters_lictacao))
        dict_licitacao = [row.__dict__ for row in licitacao]

        filters_lictante = [LicitanteModel.seq_dim_licitacao == id_licitacao]
        licitantes  = db_session.query(LicitanteModel).filter(and_(*filters_lictante))
        dict_licitantes = [row.__dict__ for row in licitantes]

        for licitante in dict_licitantes:
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
 