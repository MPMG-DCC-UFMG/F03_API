from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class SancoesCeisModel(Base):
    __tablename__ = 'painel_bi_sancoes_ceis_dev'

    id_licitacao = Column(String, primary_key=True)
    num_documento = Column(String, primary_key=True)
    tipo_sancao = Column(String, primary_key=True)
    nome_orgao_sancionador = Column(String, primary_key=True)
    cod_fundamentacao_legal = Column(String)
    desc_fundamentacao_legal = Column(String)
    data_inicio_sancao_show = Column(String)
    data_final_sancao_show = Column(String)

    class Config:
        arbitrary_types_allowed = True


