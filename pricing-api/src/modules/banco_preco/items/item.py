from sqlalchemy import Column, BigInteger, String, Float
from src.db.database import Base



class ItemModel(Base):
    __tablename__ = 'banco_precos_itens'
    ano = Column(String)
    cnpj_vencedor = Column(String)
    count = Column(BigInteger)
    data = Column(String)
    dsc_unidade_medida = Column(String)
    id_item = Column(BigInteger, primary_key=True)
    mes = Column(String)
    modalidade = Column(String)
    municipio = Column(String)
    natureza_objeto = Column(String)
    nome_vencedor = Column(String)
    orgao = Column(String)
    original = Column(String)
    original_dsc = Column(String)
    preco = Column(Float)
    preco_show = Column(Float)
    qtde_item = Column(Float)
    qtde_item_show = Column(Float)
    regiao_imediata = Column(String)
    regiao_intermediaria = Column(String)
    tipo_licitacao = Column(String)
    tipo_orgao = Column(String)
    tipo_vencedor = Column(String)

    class Config:
        arbitrary_types_allowed = True