from pydantic import BaseModel, Field

class Filter(BaseModel):
    licitacao: str = Field(example="123", title='Identificador da licitaçao')
    grupo: str = Field(example="gasolina_0", title="Grupo a qual o item faz parte")
    dsc_unidade_medida: str = Field(example="litro", title="Unidade de medida do objeto na licitação correspondente")
    ano: int = Field(example=2015, title="Ano em que a licitação foi homologada")
    municipio: str = Field(example="Belo Horizonte", title='Município em que a licitação ocorreu')
    orgao: str = Field(example="Prefeitura de Belo Horizonte", title='Órgão responsável por iniciar o processo de licitação')
    primeiro_termo: str = Field(example="gasolina", title='Primeiro termo da descrição do item')
