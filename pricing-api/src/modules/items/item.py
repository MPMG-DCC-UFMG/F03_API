from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date, Float, Boolean
from src.db.database import Base

class ItemModel(Base):
    __tablename__ = 'f03_banco_precos_itens_temp'
    item_id = Column(String, primary_key=True)
    grupo = Column(String) # Talvez incluir a relação já no ORM, para retornar as informações do grupo já na consulta ao item
    grupo_id = Column(String)
    dsc_unidade_medida = Column(String)
    grupo_ruido = Column(String)
    item_ruido = Column(String)
    original = Column(String)
    licitacao = Column(String)
    licitacao_item = Column(String)
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
