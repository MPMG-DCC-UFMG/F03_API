from sqlalchemy import Column, BigInteger, String, Float
from src.db.database import Base



class ItemModel(Base):
    __tablename__ = 'banco_precos_itens'
    ano = Column(String)
    cnpj_vencedor = Column(String)
    count = Column(BigInteger)
    data = Column(String)
    desvio_padrao_grupo = Column(Float)
    dsc_unidade_medida = Column(String)
    grupo = Column(String)
    grupo_ruido = Column(BigInteger)
    grupo_unidade_medida = Column(String)
    id_grupo = Column(BigInteger)
    id_item = Column(BigInteger, primary_key=True)
    id_licitacao = Column(BigInteger)
    mes = Column(String)
    modalidade = Column(String)
    municipio = Column(String)
    natureza_objeto = Column(String)
    nome_vencedor = Column(String)
    num_modalidade = Column(BigInteger)
    num_processo = Column(BigInteger)
    orgao = Column(String)
    original = Column(String)
    original_dsc = Column(String)
    preco = Column(Float)
    preco_medio_grupo = Column(Float)
    primeiro_termo = Column(Float)
    qtd_grupo = Column(Float)
    qtde_item = Column(Float)
    regiao_imediata = Column(String)
    regiao_intermediaria = Column(String)
    tipo_licitacao = Column(String)
    tipo_orgao = Column(String)
    tipo_vencedor = Column(String)

    class Config:
        arbitrary_types_allowed = True