from pymongo import MongoClient

# CONFIGURAÇÃO DO MONGODB ATLAS
uri = "mongodb+srv://admin:Ka16022005@clustercrud.1rh41wt.mongodb.net/?retryWrites=true&w=majority&appName=Clustercrud"
client = MongoClient(uri)

# Teste de conexão
try:
    client.admin.command('ping')
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro na conexão:", e)

# SELEÇÃO DE BANCO E COLEÇÃO
db = client["meu_banco"]
colecao = db["minha_colecao"]

# CREATE - Inserir documentos
def create_document(doc):
    resultado = colecao.insert_one(doc)
    print("Documento inserido com ID:", resultado.inserted_id)

def create_many_documents(docs):
    resultado = colecao.insert_many(docs)
    print("Documentos inseridos com IDs:", resultado.inserted_ids)

# READ - Ler documentos
def read_all():
    print("Todos os documentos:")
    for doc in colecao.find():
        print(doc)

def read_filtered(filtro):
    print(f"Documentos filtrados por {filtro}:")
    for doc in colecao.find(filtro):
        print(doc)

# UPDATE - Atualizar documentos
def update_one(filtro, novo_valor):
    colecao.update_one(filtro, {"$set": novo_valor})
    print(f"Documento atualizado com filtro {filtro} para {novo_valor}")

def update_many(filtro, novo_valor):
    colecao.update_many(filtro, {"$set": novo_valor})
    print(f"Documentos atualizados com filtro {filtro} para {novo_valor}")


# DELETE - Deletar documentos
def delete_one(filtro):
    colecao.delete_one(filtro)
    print(f"Documento deletado com filtro {filtro}")

def delete_many(filtro):
    colecao.delete_many(filtro)
    print(f"Documentos deletados com filtro {filtro}")

# EXEMPLO DE USO
if __name__ == "__main__":
    # Criar documentos
    create_document({"nome": "Cebolinha", "idade": 18, "jogo": "Free Fire"})
    create_many_documents([
        {"nome": "Mônica", "idade": 19},
        {"nome": "Cascão", "idade": 18}
    ])

    # Ler documentos
    read_all()
    read_filtered({"idade": 18})

    # Atualizar documentos
    update_one({"nome": "Cebolinha"}, {"idade": 20})
    update_many({"idade": 18}, {"jogo": "Minecraft"})

    # Deletar documentos
    delete_one({"nome": "Cebolinha"})
    delete_many({"idade": 18})
