import datetime

from sqlalchemy import Column, BigInteger, String, Float, Date
from src.db.database import Base
from pydantic.dataclasses import dataclass


class ItemModel(Base):
    __tablename__ = 'banco_precos_itens'
    # __time = Column(Date)
    ano = Column(String)
    cnpj_vencedor = Column(String)
    count = Column(BigInteger)
    data = Column(Date)
    dsc_unidade_medida = Column(String)
    flag_cpf_cnpj_valido = Column(BigInteger)
    grupo = Column(String)
    grupo_ruido = Column(BigInteger)
    id_grupo = Column(BigInteger)
    id_item = Column(BigInteger, primary_key=True)
    id_licitacao = Column(BigInteger)
    item_ruido = Column(BigInteger)
    mes = Column(String)
    mesorregiao = Column(String)
    microrregiao = Column(String)
    modalidade = Column(String)
    municipio = Column(String)
    natureza_objeto = Column(String)
    nome_vencedor = Column(String)
    orgao = Column(String)
    original = Column(String)
    original_dsc = Column(String)
    preco = Column(Float)
    preco_show = Column(Float)
    primeiro_termo = Column(String)
    qtde_item = Column(Float)
    qtde_item_show = Column(Float)
    regiao_imediata = Column(String)
    regiao_intermediaria = Column(String)
    regiao_planejamento = Column(String)
    tipo_licitacao = Column(String)
    tipo_orgao = Column(String)
    tipo_vencedor = Column(String)

    class Config:
        arbitrary_types_allowed = True