numeros = [1,2,3,4,5,6,7,8,9,10]

r1 = filter(lambda n: n % 2 == 0, numeros)
print(list(r1))

r2 = filter(lambda n: n < 100, numeros)
print(list(r2))

r3 = filter(lambda n: n > 100, numeros)
print(list(r3))