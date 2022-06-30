from sqlalchemy import Column, BigInteger, String, Float
from src.db.database import Base

class GroupModel(Base):
    __tablename__ = 'banco_precos_grupos'
    desvio_padrao =  Column(Float)
    dsc_unidade_medida =  Column(String)
    grupo = Column(String)
    grupo_id = Column(BigInteger, primary_key=True)
    max =  Column(Float)
    media =  Column(Float)
    mediana =  Column(Float)
    min =  Column(Float)
    primeiro_termo =  Column(String)
    qtd = Column(BigInteger)
    quantil_1 =  Column(Float)
    quantil_3 =  Column(Float)
    ruido = Column(BigInteger)
    var = Column(Float)
