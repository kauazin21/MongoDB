# CRUD com MongoDB Atlas e Python

## Descrição
Exemplo de operações CRUD (Create, Read, Update, Delete) em MongoDB Atlas usando Python e `pymongo`.  
Inclui funções para inserir, ler, atualizar e deletar documentos.

## Pré-requisitos
- Python 3.7 ou superior
- Biblioteca `pymongo`
- Conta no MongoDB Atlas

## Instalação
1. Instale o `pymongo`:

## USO
- Criei funções usando def para para fazer o CRUD

```bash
python -m pip install pymongo

git clone <URL_DO_REPOSITORIO>

uri = "mongodb+srv://<usuario>:<senha>@<seu_cluster>.mongodb.net/?retryWrites=true&w=majority"

# Criar documentos
create_document({"nome": "Cebolinha", "idade": 18})
create_many_documents([{"nome": "Mônica", "idade": 19}, {"nome": "Cascão", "idade": 18}])

# Ler documentos
read_all()
read_filtered({"idade": 18})

# Atualizar documentos
update_one({"nome": "Cebolinha"}, {"idade": 20})
update_many({"idade": 18}, {"jogo": "Minecraft"})

# Deletar documentos
delete_one({"nome": "Cebolinha"})
delete_many({"idade": 18})

Observações:
Testa a conexão antes de operar no banco.
Use apenas para fins didáticos.
