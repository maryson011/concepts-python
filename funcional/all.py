lista = [True, True, 'False', '', True]
r = all(lista)
print(r)

lista_2 = [1,2,3,4,5,6,67,7]
r = all(n %2 == 0 for n in lista_2)
print(r)