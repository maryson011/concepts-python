from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

total = 0

for n in numeros:
    total += n

print(total)

total = reduce(lambda a, b: a + b, numeros)

print(total)