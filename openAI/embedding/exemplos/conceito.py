# embedding é uma representação de uma palavra por números
import numpy as np # type: ignore
import math
import matplotlib.pyplot as plt # type: ignore

dados = [{'texto': 'cachorro', 'embedding': [0.03166140243411064, -0.037310533225536346]}, {'texto': 'vaca', 'embedding': [0.04572691768407822, -0.02735820785164833]}, {'texto': 'gato', 'embedding': [-0.0016545362304896116, -0.03518657013773918]}, {'texto': 'pato', 'embedding': [-0.0020623914897441864, -0.018762286752462387]}, {'texto': 'galinha', 'embedding': [0.06420667469501495, 0.0063107805326581]}, {'texto': 'cavalo', 'embedding': [0.023837734013795853, -0.0060332166031003]}, {'texto': 'porco', 'embedding': [-0.01081775687634945, -0.03103143349289894]}, {'texto': 'ovelha', 'embedding': [0.015235383063554764, -0.006357718724757433]}, {'texto': 'coelho', 'embedding': [0.025240516290068626, -0.005859405733644962]}, {'texto': 'papagaio', 'embedding': [0.07924540340900421, -0.007652528118342161]}]

ponto_interesse = dados[2]

def gerar_grafico(nome_arquivo="grafico.png"):
    plt.figure(figsize=(10, 10))
    for dado in dados:
        x = dado['embedding'][0]
        y = dado['embedding'][1]
        plt.scatter(x, y)
        plt.annotate(dado["texto"],
                     xy=(x, y),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
        plt.savefig('grafico.png')

# gerar_grafico()

def distancia_euclidiana(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def distancia_manthattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def distancia_cosseno(p1, p2):
    return np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

def mostraSimilares(funcao_distancia, ponto):
    similares = [{'distancia': funcao_distancia(dado["embedding"], ponto), 'texto':dado["texto"]} for dado in dados]
    similares = sorted(similares, key=lambda x: x['distancia'])
    print([similares["texto"] for similares in similares])
    for item in similares:
        print(f"DistÃ¢ncia entre {ponto_interesse['texto']} e {item['texto']}: {round(item['distancia'],5)}")

print ("DistÃ¢ncia euclidiana")
mostraSimilares(distancia_euclidiana, ponto_interesse["embedding"])

print("DistÃ¢ncia manthattan")
mostraSimilares(distancia_manthattan, ponto_interesse["embedding"])

print("DistÃ¢ncia cosseno")
mostraSimilares(distancia_cosseno, ponto_interesse["embedding"])