from pyhive import hive
import os

schema = 'trilhas'
nome_trilha = 'F03_PRECIFICACAO_ITEM_LICITACAO'

host='localhost'
port=10000
username='trilhasgsi'
password=os.environ["API_HIVE_PASSWORD"]
database='default'
auth='CUSTOM'

def GetItemById(id: str, **kwargs):
    schema = "trilhas"
    table = "f03_items_clusters_train"
    table_from = schema+'.'+table
    conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    query = """
    SELECT item_id as id, cluster as group_id, description, ano as year, dsc_unidade_medida as unit_metric 
    FROM {0}
    WHERE item_id = %(id)s""".format(table_from)
    cursor = conn.cursor()
    cursor.execute(query, 
        {
            "id": id
        }
    )
    item = cursor.fetchone()
    conn.close()
    if not item:
        return dict()
    else:
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, item)) #TODO: Add group to item body?

def GetItemsByFirstToken(first_token: str, offset: int = 0, limit: int = 10, **kwargs):
    schema = "trilhas"
    table = "f03_items_clusters_train"
    table_from = schema+'.'+table
    conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    query = """
    SELECT item_id as id, cluster as group_id, description, ano as year, dsc_unidade_medida as unit_metric 
    FROM {0} 
    WHERE first_token = %(first_token)s
    LIMIT %(offset)i,%(limit)i
    """.format(table_from)
    cursor = conn.cursor()
    cursor.execute(query, 
        {
            "first_token": first_token,
            "offset": offset,
            "limit": limit
        }
    )
    items = cursor.fetchall()
    conn.close()
    if not items:
        return dict()
    else: 
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, item)) for item in items] #TODO: Add group to item bodies?

def GetItemByDescription(description: str, year: int, **kwargs):
    schema = "trilhas"
    table = "f03_items_clusters_train"
    table_from = schema+'.'+table
    conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    query = """
    SELECT item_id as id, cluster as group_id, description, ano as year, dsc_unidade_medida as unit_metric 
    FROM {0} 
    WHERE description = %(description)s AND ano = %(year)s
    """.format(table_from)
    cursor = conn.cursor()
    cursor.execute(query, 
        {
            "description": description,
            "year": year
        }
    )
    item = cursor.fetchone()
    conn.close()
    if not item:
        return dict()
    else:
        columns = [column[0] for column in cursor.description] 
        return dict(zip(columns, item)) #TODO: Add group to item body?

def GetItemsByDescription(description: str, offset: int = 0, limit: int = 10, **kwargs):
    schema = "trilhas"
    table = "f03_items_clusters_train"
    table_from = schema+'.'+table
    conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    description = "%" + description + "%"
    query = """
    SELECT item_id as id, cluster as group_id, description, ano as year, dsc_unidade_medida as unit_metric 
    FROM {0} 
    WHERE description LIKE %(description)s
    LIMIT %(offset)i,%(limit)i
    """.format(table_from)
    cursor = conn.cursor()
    cursor.execute(query, 
        {
            "description": description,
            "offset": offset,
            "limit": limit
        }
    )
    items = cursor.fetchall()
    conn.close()
    if not items:
        return dict()
    else:
        columns = [column[0] for column in cursor.description] 
        return [dict(zip(columns, item)) for item in items] #TODO: Add group to item bodies?

def GetItems(offset: int = 0, limit: int = 10, **kwargs):
    schema = "trilhas"
    table = "f03_items_clusters_train"
    table_from = schema+'.'+table
    conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
            auth=auth)

    query = """
    SELECT item_id as id, cluster as group_id, description, ano as year, dsc_unidade_medida as unit_metric 
    FROM {0}
    LIMIT %(offset)i,%(limit)i
    """.format(table_from)
    cursor = conn.cursor()
    cursor.execute(query, 
        {
            "offset": offset,
            "limit": limit
        }
    )
    items = cursor.fetchall()
    conn.close()
    if not items:
        return dict()
    else:
        columns = [column[0] for column in cursor.description] 
        return [dict(zip(columns, item)) for item in items] #TODO: Add group to item bodies?