import os

pasta_atual = os.path.dirname(__file__)
caminho_arq = os.path.join(
    pasta_atual, 'legendas', 'legendas_03.srt'
)


# with open(caminho_arq, 'r') as arquivo:
#     conteudo_do_arq = arquivo.read()
#     print(conteudo_do_arq)

# with open(caminho_arq, 'r') as arquivo:
#     linha = arquivo.readline()
#     while linha:
#         partes = linha.split()
#         inicio = partes[0] if partes else ""
# 
#         print(inicio, end=", ")
# 
#         linha = arquivo.readline()

with open(caminho_arq, 'r') as arquivo:
    for linha in arquivo:
        print(linha[:5], end="*")