from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class DetalhamentoCnpjModel(Base):
    __tablename__ = 'painel_bi_detalhamento_cnpj'

    num_documento = Column(String, primary_key=True)
    bairro = Column(String)
    cep = Column(String)
    cnae_desc = Column(String)
    cnae_fiscal = Column(String)
    codigo_municipio = Column(String)
    complemento = Column(String)
    correio_eletronico = Column(String)
    data_inicio_atividade = Column(Date)
    ddd_telefone_1 = Column(String)
    ddd_telefone_2 = Column(String)
    descricao_tipo_logradouro = Column(String)
    ind_tipo_pessoa = Column(String)
    logradouro = Column(String)
    municipio = Column(String)
    nome_fantasia = Column(String)
    numero = Column(String)
    qtde_socios = Column(Integer)
    razao_social = Column(String)
    uf = Column(String)

    class Config:
        arbitrary_types_allowed = True
