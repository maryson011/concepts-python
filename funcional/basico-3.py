def remover_nome(nome):
    def removar_na_lista(lista):
        return [n for n in lista if n != nome]
    return removar_na_lista

remover_maria = remover_nome("Maria")
remover_joao = remover_nome('João')

lista_1 = ['Ana', 'Pedro', 'Maria', 'João', 'Maria']
lista_2 = ['Gui', 'Lucas', 'Sergiao', 'CArlos', 'Maria']

print(remover_maria(lista_1))
print(remover_joao(lista_1))
print(remover_maria(lista_2))