from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from src.db.database import Base

class ItemModel(Base):
    __tablename__ = 'f03_banco_precos_itens'
    item_id = Column(String, primary_key=True)
    grupo = Column(String)
    grupo_ruido = Column(String)
    item_ruido = Column(String)
    preco = Column(String)
    dsc_unidade_medida = Column(String)
    original = Column(String)
    licitacao = Column(String)
    ano = Column(String)
    original_dsc = Column(String)
    primeiro_termo = Column(String)
    metadata_trilha_versao = Column(String)
    metadata_trilha_data_execucao = Column(String)
    metadata_nome_trilha = Column(String)
    mes = Column(String)
    data = Column(Date)
    municipio = Column(String)
    orgao = Column(String)
    
