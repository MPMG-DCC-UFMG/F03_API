from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class DetalhamentoLicitacaoModel(Base):
    __tablename__ = 'painel_bi_detalhamento_licitacao'

    num_documento = Column(String, primary_key=True)
    seq_dim_licitacao = Column(BigInteger)
    complemento = Column(String)
    cpf_cnpj_socio = Column(String)
    descricao_logradouro_numero_complemento_soundex = Column(String)
    descricao_logradouro_numero_soundex = Column(String)
    descricao_logradouro_soundex = Column(String)
    descricao_tipo_logradouro = Column(String)
    email = Column(String)
    flag_cnpj_inativo = Column(Integer)
    flag_lict_unic = Column(Integer)
    ind_tipo_pessoa = Column(String)
    logradouro = Column(String)
    nome_socio = Column(String)
    numero = Column(Integer)
    telefones = Column(String)

    class Config:
        arbitrary_types_allowed = True
