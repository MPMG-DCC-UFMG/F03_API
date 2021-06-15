from sqlalchemy import Column, Integer, String
from src.db.database import Base

class ItemModel(Base):
    __tablename__ = 'f03_items_clusters_train'
    item_id = Column(String)
    seq_dim_licitacao = Column(String)
    outlier = Column(String)
    cluster = Column(String)
    dsc_unidade_medida = Column(String)
    ano = Column(String)
    description = Column(String)
    original = Column(String)
    areas = Column(String)
    price = Column(String)
    first_token = Column(String)
    metadata_trilha_versao = Column(String)
    metadata_trilha_data_execucao = Column(String)
    metadata_nome_trilha = Column(String)
