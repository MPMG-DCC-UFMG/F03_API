from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class RepresentanteLegalModel(Base):
    __tablename__ = 'painel_bi_representante_legal_dev'

    id_licitacao = Column(String, primary_key=True)
    cnpj = Column(String, primary_key=True)
    cpf_cnpj_representante = Column(String, primary_key=True)
    qualificacao_representante = Column(String)
    flag_socio = Column(String)

    class Config:
        arbitrary_types_allowed = True