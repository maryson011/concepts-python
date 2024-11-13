import inspect
import os
from . import requisicoes

def formatar_caminho(nome_arquivo='output.txt', nome_pasta='output', posicao_stack=1):
    quen_chamou = inspect.stack()[posicao_stack].filename
    pasta_exemplos = os.path.dirname(quen_chamou)
    pasta_principal = os.path.dirname(pasta_exemplos)
    caminho_final = os.path.join(pasta_principal, nome_pasta, nome_arquivo)
    return caminho_final

def salvar_imagem(url, caminho):
    caminho_atualizado = formatar_caminho(caminho, posicao_stack=2)
    dados = requisicoes.get(url)
    with open(caminho_atualizado, 'wb') as arquivo:
        arquivo.write(dados)