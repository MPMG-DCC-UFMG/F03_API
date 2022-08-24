from src.db.database import Base
from sqlalchemy import Column, BigInteger, Integer, String, Float, Date

class RepresentanteServidorModel(Base):
    __tablename__ = 'painel_bi_representante_servidor_dev'

    id_licitacao = Column(String, primary_key=True)
    num_documento = Column(String, primary_key=True)
    cpf_socio_servidor = Column(String, primary_key=True)
    vinculo_socio_servidor = Column(String)

    class Config:
        arbitrary_types_allowed = True


