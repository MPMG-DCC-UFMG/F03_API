from fastapi import HTTPException

from src.modules.banco_preco.items.item import ItemModel
from warnings import warn
import pandas as pd #Remover


def get_params_values(params):
    filters = []

    # filtros demográficos
    if bool(params.city):
        filters.append(ItemModel.municipio.in_(params.city))
    if bool(params.microregion):
        filters.append(ItemModel.microrregiao.in_(params.microregion))
    if bool(params.mesoregion):
        filters.append(ItemModel.mesorregiao.in_(params.mesoregion))
    if bool(params.plan_region):
        filters.append(ItemModel.regiao_planejamento.in_(params.plan_region))
    if bool(params.imediate_region):
        filters.append(ItemModel.regiao_imediata.in_(params.imediate_region))
    if bool(params.inter_region):
        filters.append(ItemModel.regiao_intermediaria.in_(params.inter_region))

    # # filtros relacionados aos itens
    if bool(params.group):
        filters.append(ItemModel.grupo.__eq__(params.group))
    if bool(params.object_nature):
        filters.append(ItemModel.natureza_objeto.__eq__(params.object_nature))
    if bool(params.max_amount):
        filters.append(ItemModel.qtde_item <= params.max_amount)
    if bool(params.min_amount):
        filters.append(ItemModel.qtde_item >= params.min_amount)
    if bool(params.max_homolog_price):
        filters.append(ItemModel.preco <= params.max_homolog_price)
    if bool(params.min_homolog_price):
        filters.append(ItemModel.preco >= params.min_homolog_price)

    # # filtros relacionados à licitação
    if bool(params.modality):
        filters.append(ItemModel.modalidade.__eq__(params.modality))
    if bool(params.procurement_type):
        filters.append(ItemModel.tipo_licitacao.__eq__(
            params.procurement_type))
    if bool(params.body):
        filters.append(ItemModel.orgao.__eq__(params.body))
    if bool(params.body_type):
        filters.append(ItemModel.tipo_orgao.__eq__(params.body_type))
    if bool(params.bidder_type):
        filters.append(ItemModel.tipo_vencedor.__eq__(params.bidder_type))

    # filtros relacionados aos licitantes
    if bool(params.bidder_name):
        filters.append(ItemModel.nome_vencedor.__eq__(params.bidder_name))
    if bool(params.bidder_document):
        filters.append(ItemModel.cnpj_vencedor.__eq__(params.bidder_document))

    # # filtros de data
    if bool(params.year):
        filters.append(ItemModel.ano.in_(params.year))
    if bool(params.month):
        filters.append(ItemModel.mes.in_(params.month))
    if bool(params.before):
        filters.append(ItemModel.data <= str(params.before))
    if bool(params.after):
        filters.append(ItemModel.data >= str(params.after))
    if bool(params.first_token):
        filters.append(ItemModel.primeiro_termo.__eq__(params.first_token))

    # Recupera apenas os itens que não são ruído.

    return filters


def get_range(params, min_field, max_field):
    l = {}
    if params[min_field]:
        l["gte"] = params[min_field]
    if params[max_field]:
        l["lte"] = params[max_field]
    return l


item_terms_translation = {
    "city": "municipio",
    "microregion": "microrregiao",
    "mesoregion": "mesorregiao",
    "plan_region": "regiao_planejamento",
    "imediate_region": "regiao_imediata",
    "inter_region": "regiao_intermediaria",
    "year": "ano",
    "month": "mes",
}

item_term_translation = {
    # "description": "original_dsc",
    "unit_measure": "dsc_unidade_medida",
    "group": "grupo",
    "first_token": "primeiro_termo",
    "body": "orgao",
    "body_type": "tipo_orgao",
    "modality": "modalidade",
    "procurement_type": "tipo_licitacao",
    "bidder_name": "nome_vencedor",
    "bidder_type": "tipo_vencedor",
    "bidder_document": "cnpj_vencedor",
    "object_nature": "natureza_objeto",
    "group_by_overprice": "grupo_unidade_medida"
}

pricing_translate = {
    "group_by_description": "original_raw",
    "group_by_unit_metric": "dsc_unidade_medida",
    "group_by_year": "ano",
    "group_by_cluster": "grupo",
}


def get_filter(params):
    """
    Gera os filtros do ElasticSearch
    """
    filters = []
    for param in params:
        value = params[param]
        if not value:
            continue
        if param in item_terms_translation:
            portuguese_name = item_terms_translation[param]
            filters.append({"terms": {f"{portuguese_name}.keyword": value}})
        elif param in item_term_translation:
            portuguese_name = item_term_translation[param]
            filters.append({"term": {f"{portuguese_name}.keyword": value}})
    return filters


def get_item_query_smart(params: dict):
    """
    Gera a query para a listagem de items
    """
    filters = get_filter(params)

    if params["before"]:
        pass
    if params["after"]:
        pass
    if params["min_amount"] or params["max_amount"]:
        l = get_range(params, min_field="min_amount", max_field="max_amount")
        filters.append({"range": {"qtde_item": l}})
    if params["min_homolog_price"] or params["max_homolog_price"]:
        l = get_range(params, min_field="min_homolog_price", max_field="max_homolog_price")
        filters.append({"range": {"preco": l}})

    QUERY = {
        "bool": {
            "must": [
                *filters,
                {
                    "match": {
                        "original": {
                            "query": params["description"],
                            "minimum_should_match": "70%",
                            "analyzer": "analyzer_plural_acentos"
                        }
                    }
                }
            ],
        }
    }

    return QUERY

def get_item_query_anywhere(params: dict):
    """
    Gera a query para a listagem de items
    """
    filters = get_filter(params)

    if params["before"]:
        pass
    if params["after"]:
        pass
    if params["min_amount"] or params["max_amount"]:
        l = get_range(params, min_field="min_amount", max_field="max_amount")
        filters.append({"range": {"qtde_item": l}})
    if params["min_homolog_price"] or params["max_homolog_price"]:
        l = get_range(params, min_field="min_homolog_price", max_field="max_homolog_price")
        filters.append({"range": {"preco": l}})

    QUERY = {
        "bool": {
            "must": [
                *filters,
                {
                    "match_phrase": {
                        "original": {
                            "query": params["description"],
                            "analyzer": "analyzer_plural_acentos"
                        }
                    }
                }
            ],
        }
    }

    return QUERY

def get_item_query_exact(params: dict):
    """
    Gera a query para a listagem de items
    """
    filters = get_filter(params)

    if params["before"]:
        pass
    if params["after"]:
        pass
    if params["min_amount"] or params["max_amount"]:
        l = get_range(params, min_field="min_amount", max_field="max_amount")
        filters.append({"range": {"qtde_item": l}})
    if params["min_homolog_price"] or params["max_homolog_price"]:
        l = get_range(params, min_field="min_homolog_price", max_field="max_homolog_price")
        filters.append({"range": {"preco": l}})

    QUERY = {
        "bool": {
            "must": [
                *filters,
                {"term": {"original_raw.keyword": params["description"].upper()}}
            ]
        }
    }

    return QUERY

def get_autocomplete_query(description):
    """
    Gera a query do autocomple
    """
    QUERY = {
        "suggest-exact": {
            "prefix": description,
            "completion": {
                "field": "original_prep",
                "skip_duplicates": True,
                "size": 5
            }
        }
    }

    return QUERY


def get_id_query(id: str):
    """
    Gera a query para a busca por id
    """
    QUERY = {
        "bool": {
            "must": [
                {"term": {"id_item": id}}
            ]
        }
    }

    return QUERY

#############
# WARNING Equipe vai usar o druid para os grupos
group_terms_translation = {
    "first_token": "primeiro_termo"
}


def get_group_query(params):
    filters = []

    for filter in group_terms_translation:
        if filter in params and params[filter]:
            portuguese = group_terms_translation[filter]
            filters.append({"term": {portuguese: params[filter]}})

    query = {
        "query": {
            "bool": {
                "must": [*filters]
            }
        },

    }
    return query
#########


def get_groupby_single(column, from_value, size_value):
    """
    Monta a parte do agrupamento da consulta com agregação
    """
    
    order_by = {}
    max_score = {"max": {"field": "_score"}}
    if column[0] == 'group_by_description':
        order_by = {"max_score": "desc"}
        max_score = {"max": {"script": "_score"}}
    else:
        order_by = {"_key": "asc"}
    
    aggs = {
        "group_by_script": {
            "terms": {
                "field": f"{pricing_translate[column[0]]}.keyword",
                "size": 999999,
                "order": order_by
            },
            "aggs": {
                "max_preco": {"max": {"field": "preco"}},
                "min_preco": {"min": {"field": "preco"}},
                "avg_preco": {"avg": {"field": "preco"}},
                "sum_qtde_item": {"sum": {"field": "qtde_item"}},
                "max_score": max_score,
                "commits_bucket_sort": {
                    "bucket_sort": {
                        "from": from_value,
                        "size": size_value
                    }
                }
                
            }
        },
        # "all_buckets": {
        #     "stats_bucket": {
        #         "buckets_path": "group_by_script._count"
        #     }
        # }
    }

    return aggs

def get_groupby(columns, from_value, size_value):
    """
    Monta a parte do agrupamento da consulta com agregação
    """
    h = ""
    order_by = {}
    max_score = {"max": {"field": "_score"}}
    if any(x == 'group_by_description' for x in columns):
        order_by = {"max_score": "desc"}
        max_score = {"max": {"script": "_score"}}
        h +=  "def original = '';if (doc.containsKey('original_raw.keyword') && !doc['original_raw.keyword'].empty) {original = doc['original_raw.keyword'].value;} return original"
        
        if len(columns) > 1:
            for c in columns[1:]:
                h += " + '__!@#$%__' + doc['" + f"{pricing_translate[c]}.keyword" + "'].value"
        h += ';'
    else:
        order_by = {"_key": "asc"}
        h += "return doc['"+ f"{pricing_translate[columns[0]]}.keyword" + "'].value" + [';', " + '__!@#$%__' + doc['" + f"{pricing_translate[columns[1]]}.keyword" + "'].value;"][len(columns) == 2]
    
    aggs = {
        "group_by_script": {
            "terms": {
                "script": h,
                "size": 999999,
                "order": order_by
            },
            "aggs": {
                "max_preco": {"max": {"field": "preco"}},
                "min_preco": {"min": {"field": "preco"}},
                "avg_preco": {"avg": {"field": "preco"}},
                "sum_qtde_item": {"sum": {"field": "qtde_item"}},
                "max_score": max_score,
                "commits_bucket_sort": {
                    "bucket_sort": {
                        "from": from_value,
                        "size": size_value
                    }
                }
            }
        }, 
        # "all_buckets": {
        #     "stats_bucket": {
        #         "buckets_path": "group_by_script._count"
        #     }
        # }
    }
    return aggs


def get_princing_query(params, columns, pageable, search_type):
    """
    Gera a query para a precificação
    """
    
    if search_type == "smart":
        QUERY = get_item_query_smart(params)
    
    elif search_type == "anywhere":
        QUERY = get_item_query_anywhere(params)
    
    elif search_type == "exact":
        QUERY = get_item_query_exact(params)
    
    if len(columns) == 1:
        groupby = get_groupby_single(columns, pageable.get_page()
                              * pageable.get_size(), pageable.get_size())        
    else:
        groupby = get_groupby(columns, pageable.get_page() * pageable.get_size(), pageable.get_size())
    
    body = {
        # "track_total_hits": True,
        "size": 0,
        'query': QUERY,
        'aggs': groupby,

    }

    return body


def get_group_by_columns(group_by_description, group_by_unit_metric, group_by_year, group_by_cluster):
    columns = []

    if group_by_description:
        columns.append("group_by_description")
    if group_by_unit_metric:
        columns.append("group_by_unit_metric")
    if group_by_year:
        columns.append("group_by_year")
    if group_by_cluster:
        columns.append("group_by_cluster")

    if len(columns) == 0:
        columns.append("group_by_description")

    columns = tuple(columns)
    return columns


def check_params_values(params):
    warn('This service is deprecated.', DeprecationWarning, stacklevel=1)
    # if (bool(params.after) or bool(params.before)) and (bool(params.year) or bool(params.month)):
    #     raise HTTPException(status_code=422, detail="Não é possível realizar consultas com período e " +
    #                                                 "ano/mês de exercício definidos. Favor especificar apenas um período ou ano/mês" +
    #                                                 "de exercício desejado.")

    # if (bool(params.month) and not bool(params.year)):
    #     raise HTTPException(status_code=422, detail="Necessário especificar o ano de exercício para " +
    #                         "realizar a consulta")

    # if (bool(params.min_amount) and not bool(params.max_amount)) or (
    #         not bool(params.min_amount) and bool(params.max_amount)):
    #     raise HTTPException(status_code=422, detail="Ao buscar pela quantidade de itens cotados, é" +
    #                                                 "necessário especificar um valor mínimo e máximo.")

    # if (bool(params.min_homolog_price) and not bool(params.max_homolog_price)) or (
    #         not bool(params.min_homolog_price) and bool(params.max_homolog_price)):
    #     raise HTTPException(status_code=422, detail="Ao buscar pelo valor homologado, é" +
    #                                                 "necessário especificar um valor mínimo e máximo.")

def get_groupby_overprice(from_value, size_value):
    """
    Monta a parte do agrupamento da consulta com agregação do sobrepreço
    """
    
    aggs = {
        "group_by_grupo-agg": {
            "terms": {
                "field": f"{item_term_translation['group_by_overprice']}.keyword",
                "order": {"_term": "asc" }, 
                "size": 999999
            },
            "aggs": {
                "avg_preco": {"avg": {"field": "preco"}},
                "sum_qtde_item": {"sum": {"field": "qtde_item"}},
                "sum_overprincing": {"sum": {"script" : "if (doc['preco_medio_grupo'].size()==0 || doc['desvio_padrao_grupo'].size()==0) {return 0;} else if (doc['preco'].value > (doc['preco_medio_grupo'].value + doc['desvio_padrao_grupo'].value)) {return 1;} else {return 0;}"}},
                "agg_bucket_sort": {
                    "bucket_sort": {
                        "sort": [{"sum_overprincing": {"order": "desc"}}], "from": from_value, 
                        "size": size_value
                    }
                },
                "top_grupo_hits": {
                  "top_hits": {
                    "sort": [
                      {
                        "preco": {
                          "order": "desc"
                        }
                      }
                    ],
                    "_source": {
                      "includes": [ "id_licitacao", "municipio", "orgao", "num_processo", 
                      "num_modalidade", "modalidade", "ano", "original", "original_dsc", 
                      "dsc_unidade_medida", "preco", "qtde_item", "id_grupo", "grupo", 
                      "qtde_grupo", "preco_medio_grupo" ]
                    },
                    "size": 5
                  }
                }
            }
        }
    }
    return aggs


def get_overprincing_query(params, pageable, search_type):
    """
    Gera a query para a precificação
    """
    
    if search_type == "smart":
        QUERY = get_item_query_smart(params)
    
    elif search_type == "anywhere":
        QUERY = get_item_query_anywhere(params)
    
    elif search_type == "exact":
        QUERY = get_item_query_exact(params)
    
    groupby = get_groupby_overprice(pageable.get_page() * pageable.get_size(), pageable.get_size())   
    
    body = {
        "track_total_hits": True,
        "size": 0,
        'query': QUERY,
        'aggs': groupby,
    }
    
    return body
  
class Pageable:
    def __init__(self, page: int, size: int, sort: str, order: str, search_type: str):
        self._page = page
        self._size = size
        self._sort = sort
        self._order = order
        self._search_type = search_type

    def get_page(self):
        return self._page

    def get_size(self):
        return self._size

    def get_sort(self):
        return self._sort

    def get_order(self):
        return self._order

    def get_search_type(self):
        return self._search_type

    def __str__(self):
        return str({
            "page": self._page,
            "size": self._size,
            "sort": self._sort,
            "order": self._order,
            "search_type": self._search_type
        })
