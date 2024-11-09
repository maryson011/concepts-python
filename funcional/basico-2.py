def somar(a):
    def finalizar_soma(b):
        return a + b
    return finalizar_soma

print(somar(3)(2))

SALARIO_BASE = 2333.5
somar_com_salario_base = somar(SALARIO_BASE)

print(somar_com_salario_base(320.4))