import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from listar import listar_aarquivos

def ler_arquivos(pasta, arquivos):
    conteudo = []

    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        with open(caminho, 'r') as file:
            conteudo.extend(file.read().splitlines())

    return conteudo

def remover_numero(linhas):
    return [linha for linha in linhas if not linha.isdigit()]

def remover_tempos(linhas):
    return [linha for linha in linhas if "-->" not in linha]

def contar_palavras(linhas):
    palavras = {}
    for linha in linhas:
        linha = linha.translate(
            str.maketrans('', '', '"$&?!./0123456789%<>[]()-')
        )

        for palavra in linha.split():
            palavra = palavra.lower()
            palavras[palavra] = palavras.get(palavra, 0) + 1

    palavras = sorted(palavras.items(), key=lambda item: item[1], reverse=True)
    return palavras

def main():
    pasta = os.path.join(
        os.path.dirname(__file__), '../legendas'
    )

    legendas = listar_aarquivos(pasta, 'srt')
    linhas = ler_arquivos(pasta, legendas)
    linhas = remover_numero(linhas)
    linhas = remover_tempos(linhas)
    palavras = contar_palavras(linhas)
    print(palavras)


main()