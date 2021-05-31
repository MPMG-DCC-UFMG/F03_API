"""This module implements the HiveConnection class."""
import os
import os.path
import importlib
from threading import Thread
from typing import Union, Iterable, Callable, Dict
from pyhive import hive


class HiveConnection:
    """HiveConnection class acts as the hive database server."""

    def __init__(self, username='trilhasgsi', password='UFMGtrilhas2020'):
        """Initialise the parameters to be used to connect to the database."""
        self.schema = 'trilhas'
        self.nome_trilha = 'F03_PRECIFICACAO_ITEM_LICITACAO'
        self.host = 'localhost'
        self.port = 10000
        self.database = 'default'
        self.auth = 'CUSTOM'
        self.username = username
        self.password = password
        self.conn = None


    def connect(self) -> None:
        """Connects to the hive database."""
        self.conn = hive.Connection(host=self.host,
                                          port=self.port,
                                          username=self.username,
                                          password=self.password,
                                          database=self.database,
                                          auth=self.auth)

    def ready(self) -> bool:
        """Returns whether the hive connection is active."""
        pass


hive_connection = HiveConnection()
hive_connection.connect()
