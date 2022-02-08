from sqlalchemy import Column, Integer, String, Float
from typing import Any, List
from src.db.database import Base

class GroupModel(Base):
    __tablename__ = 'banco_precos_grupos'
    grupo_id = Column(String, primary_key=True)
    grupo = Column(String)
    dsc_unidade_medida =  Column(String)
    media =  Column(String)
    qtd =  Column(Integer)
    max =  Column(Integer)
    min =  Column(Integer)
    mediana =  Column(Float)
    desvio_padrao =  Column(Float)
    var =  Column(String)
    quantil_1 =  Column(Float)
    quantil_3 =  Column(Float)
    primeiro_termo =  Column(String)
    ruido =  Column(Integer)
    # metadata_trilha_versao =  Column(String)
    # metadata_trilha_data_execucao =  Column(String)
    # metadata_nome_trilha =  Column(String)
