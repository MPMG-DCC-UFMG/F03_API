from pyhive import hive
import random
import os
import pandas as pd

schema = 'trilhas'
nome_trilha = 'F03_PRECIFICACAO_ITEM_LICITACAO'

host='localhost'
port=10000
username='trilhasgsi'
password=os.environ["API_HIVE_PASSWORD"]
database='default'
auth='CUSTOM'


def GetGroupByName(name: str, **kwargs) -> dict:

    hive_connection = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    table = "f03_cluster_prices_statistics_year"
    table_from = schema+'.'+table

    query = "SELECT                \
                cluster as grupo,   \
                dsc_unidade_medida as unidade_medida,   \
                ano,    \
                mean as preco_medio,    \
                count as qtde_itens \
     FROM {0}   \
     WHERE outlier = 0 AND cluster = %(name)s ".format(table_from)

    cursor = hive_connection.cursor()
    cursor.execute(query,
        {
            "name": name
        }
    )

    group = cursor.fetchone()
    hive_connection.close()
    if not group:
        return dict()
    else:
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, group))


def GetGroupsByItem(item: str, offset: int = 0, limit: int = 10, **kwargs):

    hive_connection = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    table = "f03_cluster_prices_statistics_year"
    table_from = schema+'.'+table

    query = "SELECT                \
                cluster as grupo,   \
                dsc_unidade_medida as unidade_medida,   \
                ano,    \
                mean as preco_medio,    \
                count as qtde_itens \
     FROM {0} \
     WHERE outlier = 0 AND first_token = %(first_token)s  \
     LIMIT %(offset)i,%(limit)i".format(table_from)
    
    cursor = hive_connection.cursor()
    cursor.execute(query, 
        {
            "first_token": item,
            "limit": limit,
            "offset": offset
        }
    )

    groups = cursor.fetchall()
    hive_connection.close()
    if not groups:
        return dict()
    else:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, group)) for group in groups]


def GetGroups(offset: int = 0, limit: int = 10, **kwargs):

    hive_connection = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    table = "f03_cluster_prices_statistics_year"
    table_from = schema+'.'+table

    query = "SELECT     \
                cluster as grupo,   \
                dsc_unidade_medida as unidade_medida,   \
                ano,    \
                mean as preco_medio,    \
                count as qtde_itens \
     FROM {0} \
     WHERE outlier = '0'  \
     LIMIT %(offset)i,%(limit)i".format(table_from)

    cursor = hive_connection.cursor()
    cursor.execute(query, 
        {
            "offset": offset,
            "limit": limit
        }
    )
    groups = cursor.fetchall()
    hive_connection.close()
    if not groups:
        return dict()
    else:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, group)) for group in groups]