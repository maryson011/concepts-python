from utils import cliente
import json

while True:
    mensagem = input('Mensagem: ')
    if mensagem.lower() == 'salir':
        break
    resposta = cliente.moderations.create(input=mensagem)
    improprio = resposta.results[0].flagged
    print(f'o texto {mensagem} é impróprio? {improprio}')
    if improprio:
        categorias = json.loads(resposta.results[0].categories.to_json())
        print('O texto é impróprio por: ', end='')
        for chave, valor in categorias.items():
            if valor:
                print(f'{chave}', end='')
        print()