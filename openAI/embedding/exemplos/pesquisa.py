from utils import cliente
import numpy as np # type: ignore

def criar_embedding(texto):
    resposta = cliente.embeddings.create(
        input = "texto",
        model = "text-embedding-3-small"
    )

    return resposta.data[0].embedding

textos = ['cachorro', 'vaca', 'gato', 'pato', 'galinha', 'porco', 'ovelha', 'coelho', 'papagaio']

dados = [{'texto': texto, 'embedding': criar_embedding(texto)} for texto in textos]

ponto_interesse = criar_embedding('leão')

def similaridade_cosseno(p1, p2):
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

similares = [{'similaridade': similaridade_cosseno(item['embedding'],
ponto_interesse), 'texto': item['texto']} for item in dados]

similares = sorted(similares, key=lambda x: x['similaridade'], reverse=True)

print([item['texto'] for item in similares])