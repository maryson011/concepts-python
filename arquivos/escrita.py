import os

pasta_atual = os.path.dirname(__file__)
caminho_arq = os.path.join(
    pasta_atual, 'textos', 'texto_01.txt'
)

with open(caminho_arq, 'w') as arquivo:
    arquivo.write('Olá, estou criando um arquivo com python')

linhas = [
    "Escrevendo multiplas linhas ",
    "em um arquivo de texto ",
    "com python"
]

# with open(caminho_arq, 'w') as arquivo:
with open(caminho_arq, 'a') as arquivo:
    arquivo.writelines("\n" + linha for linha in linhas)
#     for linha in linhas:
#         arquivo.writelines(f"{linha}\n")