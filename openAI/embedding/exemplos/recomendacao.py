from utils import cliente
import numpy as np # type: ignore

def criar_embedding(texto):
    resposta = cliente.embeddings.create(
        input = "texto",
        model = "text-embedding-3-small"
    )

    return resposta.data[0].embedding

def similaridade_cosseno(p1, p2):
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))


desc_itens = [
    'Faca de chef para cortar vegetais e carnes',
    'Tábua de corte de bombu',
    'Tábua de corte de vidro',
    'Panela de aço inoxidável',
    'Colher de madeira',
    'Estátula de silicone resistente ao calor',
    'Espátula de silicone',
    'Medidor de copos e colheres',
    'Tigela de mistura grande',
    'Ralador de queijo'
]

embeddings = [criar_embedding(item) for item in desc_itens]

def recomendar(input, qtde_rec=3):
    input_embedding = criar_embedding(input)
    similares = [similaridade_cosseno(input_embedding, desc) for desc in embeddings]
    top_indices = np.argsort(similares)[::-1][0:qtde_rec]
    return [(desc_itens[i], similares[i]) for i in top_indices]

input_usuario = input('O que você precisa?')
recomendacoes = recomendar(input_usuario)

print('\n Recomendações para: ', input_usuario)
for item, pontuacao in recomendacoes:
    print(f'{item} ({pontuacao:.2f})')