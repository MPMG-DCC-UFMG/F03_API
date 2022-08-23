import os

from src.modules.painel_bi.v2.model.licitacao import LicitacaoModel

from src.db.database import db_session

from sqlalchemy import func

class FiltersRepository:



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
            },
            "riscos": [
                {
                    "descricao":"Alto",
                    "ordem":3,
                    "trilhas":[
                        {
                            "identificador":"T02",
                            "nome":"Licitações contendo licitantes com CNPJ inativo",
                            "descricao":"Se o CNPJ está inativo a empresa não deveria estar operando, e consequente não deveria estar licitando."
                        },
                        {
                            "identificador":"T07",
                            "nome":"Licitações contendo licitantes com representantes sócios em comum",
                            "descricao":"O principal motivo de fraude encontrado são empresas dos mesmos sócios licitando juntas."
                        },
                        {
                            "identificador":"T11",
                            "nome":"Licitações contendo licitantes antes do início das atividades",
                            "descricao":"Se a empresa ainda não iniciou suas atividades, ela não deveria estar licitando."
                        }
                    ]
                },
                {
                    "descricao":"Médio",
                    "ordem":2,
                    "trilhas":[
                        {
                            "identificador":"T06",
                            "nome":"Licitações contendo licitantes com representantes não-sócios em comum",
                            "descricao":"Conluio entre licitantes é o principal motivo de fraude dentre os dados encontrados. Porém existem qualificações dos representantes legais que não se enquadram na categoria de sócios ou proprietários. Portanto essa trilha é uma forma de investigar, indiretamente, o conluio."
                        },
                        {
                            "identificador":"T10",
                            "nome":"Licitações contendo licitantes com CNAE incongruente",
                            "descricao":"Licitantes que possuem CNAE’s incongruentes com o tipo de produto / serviço que estão oferecendo são suspeitos. Quando essa trilha for aprimorada para avaliar se o CNAE do licitante é congruente com o item da licitação, o alerta dessa trilha pode ser considerado risco alto."
                        },
                        {
                            "identificador":"T12",
                            "nome":"Licitações com licitantes com restrição no CEIS",
                            "descricao":"Na base do CEIS encontram- se as empresas que estão sofrendo uma sanção legal que as impede de licitar, portanto uma empresa licitando com uma sanção vigente seria um risco alto de fraude. Porém, na base presente no MPMG, não há o nível de abrangência da sanção, então por exemplo, uma empresa sancionada por um órgão de São Paulo, poderia licitar sem problemas no estado de Minas Gerais caso a abrangência da sanção seja apenas estadual, por esse motivo essa trilha foi considerada de médio risco."
                        }
                    ]
                },
                {
                    "descricao":"Baixo",
                    "ordem":1,
                    "trilhas":[
                        {
                            "identificador":"T01",
                            "nome":"Licitações contendo licitantes únicos",
                            "descricao":"Licitações contendo licitantes únicos."
                        },
                        {
                            "identificador":"T03",
                            "nome":"Licitações contendo licitantes com e-mails em comum",
                            "descricao":"Algumas empresas que usam serviços de escritório de contabilidade, acabam cadastrando, junto a receita federal, o email do escritório ao invés do email da empresa, isso gera um certo ruído no resultado dessa trilha."
                        },
                        {
                            "identificador":"T04",
                            "nome":"Licitações contendo licitantes com telefones em comum",
                            "descricao":"Algumas empresas que usam serviços de escritório de contabilidade, acabam cadastrando, junto a receita federal, o telefone do escritório ao invés do telefone da empresa, isso gera um certo ruído no resultado dessa trilha."
                        },
                        {
                            "identificador":"T05",
                            "nome":"Licitações contendo licitantes com endereços em comum",
                            "descricao":"Algumas empresas que usam serviços de escritório de contabilidade, acabam cadastrando, junto a receita federal, o endereço do escritório ao invés do endereço da empresa, isso gera um certo ruído no resultado dessa trilha."
                        },
                        {
                            "identificador":"T08",
                            "nome":"Licitações contendo licitantes vencedores frequentes",
                            "descricao":"A presença de licitantes vencedores frequentes, por si só, não é um forte indício de fraude."
                        },
                        {
                            "identificador":"T09",
                            "nome":"Licitações contendo licitantes perdedores frequentes",
                            "descricao":"A presença de licitantes perdedores frequentes, por si só, não é um forte indício de fraude."
                        },
                        {
                            "identificador":"T13",
                            "nome":"Licitações com licitantes cujos sócios são ou têm vínculo com servidores públicos",
                            "descricao":"A presença de licitantes perdedores frequentes, por si só, não é um forte indício de fraude."
                        }
                    ]
                }
            ]
        }

        return res
