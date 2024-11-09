def dobro(n):
    return n * 2

lista_1 = [1,2,3,4,5]

resultado_1 = map(dobro, lista_1)
print(list(resultado_1))

resultado_2 = map(lambda x: x ** 3, lista_1)
print(list(resultado_2))