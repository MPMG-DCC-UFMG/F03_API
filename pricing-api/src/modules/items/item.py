from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.sql.sqltypes import Date, Float, Boolean
from src.db.database import Base

class ItemModel(Base):
    __tablename__ = 'banco_precos_itens'
    id_item = Column(BigInteger, primary_key=True)
    grupo = Column(String) # Talvez incluir a relação já no ORM, para retornar as informações do grupo já na consulta ao item
    id_grupo = Column(BigInteger)
    dsc_unidade_medida = Column(String)
    grupo_ruido = Column(Integer)
    item_ruido = Column(Integer)
    original = Column(String)
    id_licitacao = Column(BigInteger)
    original_dsc = Column(String)
    primeiro_termo = Column(String)
    ano = Column(String)
    mes = Column(String)
    qtde_item = Column(Float)
    preco = Column(Float)
    cnpj_vencedor = Column(String)
    flag_cpf_cnpj_valido = Column(Boolean)
    nome_vencedor = Column(String)
    tipo_vencedor = Column(String)
    orgao = Column(String)
    tipo_orgao = Column(String)
    regiao_planejamento = Column(String)
    municipio = Column(String)
    microrregiao = Column(String)
    mesorregiao = Column(String)
    regiao_imediata = Column(String)
    regiao_intermediaria = Column(String)
    modalidade = Column(String)
    tipo_licitacao = Column(String)
    natureza_objeto = Column(String)
    data = Column(Date)
