from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date, Float
from src.db.database import Base

class ItemModel(Base):
    __tablename__ = 'f03_banco_precos_itens_temp'
    item_id = Column(String, primary_key=True)
    grupo_id = Column(String)
    grupo = Column(String) # Talvez incluir a relação já no ORM, para retornar as informações do grupo já na consulta ao item
    grupo_ruido = Column(String)
    item_ruido = Column(String)
    preco = Column(String)
    dsc_unidade_medida = Column(String)
    original = Column(String)
    licitacao = Column(String)
    licitacao_item = Column(String)
    ano = Column(String)
    original_dsc = Column(String)
    primeiro_termo = Column(String)
    metadata_trilha_versao = Column(String)
    metadata_trilha_data_execucao = Column(String)
    metadata_nome_trilha = Column(String)
    mes = Column(String)
    data = Column(Date)
    municipio = Column(String)
    regiao = Column(String)
    orgao = Column(String)
    forma_pagamento = Column(String)
    nome_homologado = Column(String)
    num_cpf_cnpj_homologado = Column(String)
    modalidade = Column(String)
    vlr_unitario = Column(Float)
    vlr_unitario_cotado = Column(Float)
    qtde_item_homologado = Column(Float)
    
