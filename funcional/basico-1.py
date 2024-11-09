def repetir(func, qtde=2):
    for _ in range(qtde):
        func()

def bom_dia():
    print('Bom dia')

bom_dia()

repetir(bom_dia, 10)