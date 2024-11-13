from utils import cliente

resposta = cliente.embeddings.create(
    input = "texto",
    model = "text-embedding-3-small",
    dimensions = 100
)

print(resposta.data[0].embedding)