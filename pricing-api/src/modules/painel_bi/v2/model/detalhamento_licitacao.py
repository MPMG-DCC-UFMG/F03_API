from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class DetalhamentoLicitacaoModel(Base):
    __tablename__ = 'painel_bi_detalhamento_licitacao_dev'

    num_documento = Column(String, primary_key=True)
    seq_dim_licitacao = Column(BigInteger, primary_key=True)
    complemento = Column(String)
    descricao_logradouro_numero_complemento_soundex = Column(String)
    descricao_logradouro_numero_soundex = Column(String)
    descricao_logradouro_soundex = Column(String)
    descricao_tipo_logradouro = Column(String)
    email = Column(String)
    flag_cnpj_inativo = Column(Integer)
    flag_lict_unic = Column(Integer)
    ind_tipo_pessoa = Column(String)
    logradouro = Column(String)
    numero = Column(Integer)
    telefones = Column(String)
    data_habilitacao = Column(Date)
    data_inicio_atividade = Column(Date)
    flag_licitante_antes_atividade = Column(Integer)
    flag_licitante_penalidade_ceis = Column(Integer)
    flag_licitante_servidor_publico = Column(Integer)
    flag_perdedor_frequente = Column(Integer)
    flag_vencedor_frequente = Column(Integer)




    class Config:
        arbitrary_types_allowed = True
