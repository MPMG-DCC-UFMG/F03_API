from typing import Optional
from pydantic import BaseModel, Field

class Item(BaseModel):
    id_item: int = Field(example=11442433, title='Identificador do item')
    dsc_unidade_medida: str = Field(example="caixa", title="Unidade de medida do objeto na licitação correspondente")
    original: str = Field(example="GASOLINA COMUM 05 LITROS", title='Descrição do objeto na licitação correspondente')
    original_dsc: str = Field(example="gasolina comum 5 litros", title='Descrição padronizada do objeto na licitação correspondente')
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    mes: int = Field(example=3, title="Mês em que a licitação foi homologada")
    qtde_item: int = Field(example=10, title='Quantidade de itens homologados')
    preco: float = Field(example=16.9, title="Valor do item licitado")
    cnpj_vencedor: str = Field(example="00874929000140", title='CPF/CNPJ do licitante vencedor')
    nome_vencedor: str = Field(example="MED CENTER COMERCIAL LTDA", title='Nome do licitante vencedor')
    tipo_vencedor: str = Field(example="J", title='Tipo do licitante vencedor')
    orgao: str = Field(example="PREFEITURA MUNICIPAL DE ITANHANDU", title='Órgão responsável por iniciar o processo de licitação')
    tipo_orgao: str = Field(example="PREFEITURA MUNICIPAL", title='Tipo do órgão responsável por iniciar o processo de licitação')
    municipio: str = Field(example="ITANHANDU", title='Município em que a licitação ocorreu')
    regiao_imediata: str = Field(example="SAO LOURENCO", title='Região imediata em que a licitação ocorreu')
    regiao_intermediaria: str = Field(example="POUSO ALEGRE", title='Região intermediária em que a licitação ocorreu')
    modalidade: str = Field(example="PREGAO PRESENCIAL", title='Modalidade da licitação')
    tipo_licitacao: str = Field(example="MENOR PRECO", title='Tipo da licitação')
    natureza_objeto: str = Field(example="COMPRAS E OUTROS SERVICOS", title='Natureza do objeto da licitação')
    data: Optional[str] = Field(example="2015-03-02", title='Data em que a licitação foi homologada')