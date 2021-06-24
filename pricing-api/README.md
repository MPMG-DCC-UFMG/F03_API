### Executando o projeto
```
uvicorn main:app --reload
```

#### Estrutura do projeto

```
src/db - conexão com o banco de dados
src/modules          - módulos divididos entre as entidades do projeto
src/modules/entity/entity_controller - especificação de endpoints e suas validações
src/modules/entity/entity_service - regras de negócio
src/modules/entity/entity_repository - consultas ao banco de dados
```
