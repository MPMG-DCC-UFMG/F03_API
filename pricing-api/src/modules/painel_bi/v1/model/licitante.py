from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class LicitanteModel(Base):
    __tablename__ = 'painel_bi_detalhamento_licitante'

    num_documento = Column(String, primary_key=True)
    seq_dim_licitacao = Column(BigInteger)
    ind_venceu = Column(String)
    numero_de_itens = Column(Integer)
    participacao_itens_licitacao = Column(Float)
    participacao_licitacao = Column(Float)
    soma_recurso_alocado = Column(Float)


    class Config:
        arbitrary_types_allowed = True
