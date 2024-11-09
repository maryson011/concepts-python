lista_nomes = ['Ana', 'Pedro', 'Maria', 'João', 'REbeca']
lista_idades = [23, 48, 32, 34]
lista_estados = ['SP', 'CE', 'RJ', 'RS']

r = zip(lista_nomes, lista_idades, lista_estados)
# print(dict(r)) # consome o zip
# print(list(r))

for nome, idade, estado in r:
    print(f'{nome} tem {idade} e mora em {estado}')